"""
The Headmouse module provides an interface by opening the web camera and 
detecting the user's face to control the mouse by tilting the head using 
the tip of the nose as reference point.
It can also be customized to trigger different functions instead of a mouse
click when the user winks.
To use the module it's necessary to have the file shape_predictor_68_face_landmarks.dat
Compressed: 
http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

Uncompressed:
https://github.com/rfontalva/dlib_shape_predictor_68_face_landmarks/tree/master
"""

import cv2
import numpy as np
import dlib
from typing import TypeVar
from .headmouse_singleton import HeadmouseSingleton
from .headmouse_utils import eye_aspect_ratio, get_closest_face
from .controller import MouseController
from .controller import AbstractController

AbstractController_ = TypeVar('AbstractController_', bound=AbstractController)

class Headmouse(metaclass=HeadmouseSingleton):
    """
    Parameters:

    sensitivity (int): Determines how fast and precisely the mouse pointer
    will move, default is 0.3.
    camera_path: if there are multiple cameras connected, select which one opens.
    """
    def __init__(self, predictor_path, sensitivity=None, camera_path=None):
        self.detector = dlib.get_frontal_face_detector()
        self.cap = cv2.VideoCapture(0)
        if camera_path:
            self.cap.open(camera_path)
        if not self.cap.isOpened():
            raise Exception('No camera available')
        self.predictor = dlib.shape_predictor(predictor_path)
        self.is_calibrated = False
        self.nose_y = 0
        self.nose_x = 0
        self.center = [self.nose_x, self.nose_y]
        self.y_offset = 10
        self.coef_sens = sensitivity or 0.3
        self.controller = MouseController(self.coef_sens)
        self.thresh_x = 20
        self.thresh_y = 25
        self.right_eye_points = list(range(42, 48))
        self.left_eye_points = list(range(36, 42))
        self.nose_point = 34
        self.mouth_right_points = [54, 64]
        self.ear_thresh = 0.2
        self.ear_consec_frames = 4
        self.right_counter = 0
        self.left_counter = 0
        self.mouth_twitch_debounce = False
        self.twitch_thresh_inactive = 11
        self.twitch_thresh_active = 15
        self.first_mouth_position_set = False
        self.disable_warnings = False
        self.size = 200
        self.too_close = False
        self.too_far = False
        self.test = 0

    @classmethod
    def get_instance(cls):
        try:
            return cls._instances[cls]
        except Exception as e:
            raise Exception("No instances of Headmouse have been created. ")

    def refresh(self):
        """
        Updates the position of the nose and the face features (size, eyes and mouth position)
        It should be called at least at the same frequency at which the web camera 
        refreshes.
        """
        ret, self.frame = self.cap.read()
        self.frame = cv2.flip(self.frame, 1)
        if ret:
            gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            rects = self.detector(gray, 0)
            try:
                rect = get_closest_face(rects)
            except IndexError:
                rect = None
            if rect:
                landmarks = np.matrix(
                    [[p.x, p.y] for p in self.predictor(self.frame, rect).parts()])
                self._update_size(landmarks)
                self._update_nose_position(landmarks)
                if self.is_calibrated == False:
                    self.center = [self.nose_x, self.nose_y]
                    self.is_calibrated = True
                self._mouth_processing(landmarks)
                self._eye_processing(landmarks)
                self._update_position()

    def quit(self):
        self.cap.release()

    def calibrate(self):
        """
        The next time self.refresh gets called, the point of reference from which
        the pointer is moved will be readjusted to where the user's nose is. 
        """
        self.is_calibrated = False

    def override_controller(self, controller: AbstractController_):
        """
        Controller must be an object of a class that implements the
        AbstractController interface.
        """
        if not isinstance(controller, AbstractController):
            raise Exception("controller object must implement AbstractController interface")
        self.controller = controller

    def _mouth_processing(self, landmarks):
        """
        rcp: right corner points
        rel: relative
        """
        mouth_right_corner = landmarks[self.mouth_right_points][0]
        coords_mouth = (mouth_right_corner.item(0), mouth_right_corner.item(1))
        if not self.first_mouth_position_set:
            self.distance_x = self.nose_x - coords_mouth[0]
            self.distance_y = self.nose_y - coords_mouth[1]
            self.first_mouth_position_set = True
        else:
            finishing_point = (self.nose_x - self.distance_x, self.nose_y - self.distance_y)
            distance = ((finishing_point[0].item(0) - coords_mouth[0])**2 + (finishing_point[1].item(0) - coords_mouth[1])**2)**0.5
            if distance > self.twitch_thresh_active and not self.mouth_twitch_debounce:
                self.controller.mouth_twitch()
                self.mouth_twitch_debounce = True
            if distance < self.twitch_thresh_inactive:
                self.mouth_twitch_debounce = False

    def _update_position(self):
        rel_x_mov = self.nose_x - self.center[0]
        rel_y_mov = self.nose_y - self.center[1]
        right_condition = rel_x_mov > self.thresh_x
        left_condition = rel_x_mov < -self.thresh_x
        up_condition = rel_y_mov < -self.thresh_y
        down_condition = rel_y_mov > (self.thresh_y - self.y_offset)
        if right_condition:
            self.controller.right(self.nose_x, self.center)
        #left
        if left_condition:
            self.controller.left(self.nose_x, self.center)
        #down
        if down_condition:
            self.controller.down(self.nose_y, self.center)
        #up
        if up_condition:
            self.controller.up(self.nose_y, self.center)
        elif not up_condition and not down_condition and not right_condition and not left_condition:
            self.controller.center() #allows to debounce and perform discrete actions

    def _eye_processing(self, landmarks):
        """
        ear: eye aspect ratio
        """
        right_eye = landmarks[self.right_eye_points]
        left_eye = landmarks[self.left_eye_points]
        [right_winked, self.right_counter] = self._wink_count(right_eye, self.right_counter)
        [left_winked, self.left_counter] = self._wink_count(left_eye, self.left_counter)
        if right_winked:
            self.controller.right_wink()
        #right wink has priority over left
        elif left_winked:
            self.controller.left_wink()       
        
    def _wink_count(self, eye, counter):
        has_winked = False
        ear = eye_aspect_ratio(eye)
        if self.size > 250:
            ear += self.size/22000
        elif self.size < 160:
            ear -= self.size/1600
        if ear < self.ear_thresh:
            counter += 1
        else:
            if counter >= self.ear_consec_frames:
                has_winked = True
            counter = 0
        return [has_winked, counter]

    def _update_nose_position(self, landmarks):
        nose = landmarks[self.nose_point]
        nose_position = nose[0]
        self.nose_x = nose_position[:, 0]
        self.nose_y = nose_position[:, 1]

    def _update_size(self, landmarks):
        self.too_close = False
        self.too_far = False
        bottom = landmarks[8]
        top = landmarks[27]
        self.size = bottom.item(1) - top.item(1)
        msg = None
        if self.size > 200:
            msg = "Move away from the camera"
            self.too_close = True
        elif self.size < 160:
            msg = "Move closer to the camera"
            self.too_far = True
        if not self.disable_warnings and msg is not None:
            print(f"WARNING: {msg}")

    def show_image(self, show_thresh=True):
        if show_thresh:
            start = (int(self.center[0] - self.thresh_x), int(self.center[1] - self.thresh_y))
            end = (int(self.center[0] + self.thresh_x), int(self.center[1] + self.thresh_y + - self.y_offset))
            cv2.circle(self.frame, (self.nose_x[0,0], self.nose_y[0,0]), 3, (255,0,0), 1)
            cv2.rectangle(self.frame, start, end, (255,0,0), 1)
        cv2.imshow('My window', self.frame)

    def get_frame(self, show_thresh=True):
        if show_thresh:
            start = (int(self.center[0] - self.thresh_x), int(self.center[1] - self.thresh_y))
            end = (int(self.center[0] + self.thresh_x), int(self.center[1] + self.thresh_y + - self.y_offset))
            if isinstance(self.nose_x, np.matrix) and isinstance(self.nose_y, np.matrix):
                cv2.circle(self.frame, (self.nose_x[0,0], self.nose_y[0,0]), 3, (255,0,0), 1)
                cv2.rectangle(self.frame, start, end, (255,0,0), 1)
        return self.frame

    def destroy_window(self):
        cv2.destroyAllWindows()

    def update_threshold(self, value_x, value_y, y_offset=None):
        """
        Defines how much the user has to move from the reference
        point for the movement to be valid
        """
        self.thresh_x = value_x
        self.thresh_y = value_y
        if y_offset is not None and y_offset > 0:
            self.y_offset = y_offset

    def update_y_offset(self, y_offset=None):
        """
        Modifies y axis offset. Y offset is used
        to make it easier to move down than up, since that's a harder neck move
        down_condition = rel_y_mov > (self.thresh_y - self.y_offset)
        """
        if y_offset > 0:
            self.y_offset = y_offset

    def update_coef_sens(self, value):
        self.coef_sens = value
        self.controller.update_coef_sens(self.coef_sens)

    def update_mouth_thresh(self, value_inactive, value_active):
        self.twitch_thresh_inactive = value_inactive
        self.twitch_thresh_active = value_active

    def update_mouth_active_thresh(self, value_active):
        self.twitch_thresh_active = value_active

    def update_mouth_thresh(self, value_inactive):
        self.twitch_thresh_inactive = value_inactive

    def get_size_info(self):
        if self.too_far:
            return "too far"
        if self.too_close:
            return "too close"
        return "ok"
