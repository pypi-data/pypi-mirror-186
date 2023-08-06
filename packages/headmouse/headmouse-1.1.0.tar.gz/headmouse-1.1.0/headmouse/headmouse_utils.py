from scipy.spatial import distance as dist
from dlib import rectangle
import numpy as np

def eye_aspect_ratio(eye):
    try:
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])
        C = dist.euclidean(eye[0], eye[3])
        ear = (A + B) / (2.0 * C)
        return ear
    except ValueError:
        updated_eye = []
        for i, mat in enumerate(eye):
            updated_eye.append(np.array(mat).flatten())
        A = dist.euclidean(updated_eye[1], updated_eye[5])
        B = dist.euclidean(updated_eye[2], updated_eye[4])
        C = dist.euclidean(updated_eye[0], updated_eye[3])
        ear = (A + B) / (2.0 * C)
        return ear

def get_closest_face(rects: rectangle)-> rectangle: 
    closest = 0
    for index, rect in enumerate(rects):
        if rect.area() > rects[closest].area():
            closest = index
    return rects[closest]
    
