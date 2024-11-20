import cv2
import numpy as np

# Translation
def translate(image, tx, ty):
    rows, cols, _ = image.shape
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    return cv2.warpAffine(image, translation_matrix, (cols, rows))

# Scaling
def scale(image, sx, sy):
    rows, cols, _ = image.shape
    scaling_matrix = np.float32([[sx, 0, 0], [0, sy, 0]])
    return cv2.warpAffine(image, scaling_matrix, (int(cols * sx), int(rows * sy)))

# Rotation
def rotate(image, angle):
    rows, cols, _ = image.shape
    center = (cols // 2, rows // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)
    return cv2.warpAffine(image, rotation_matrix, (cols, rows))

# Shearing
def shear(image, shear_factor):
    rows, cols, _ = image.shape
    shear_matrix = np.float32([[1, shear_factor, 0], [0, 1, 0]])
    return cv2.warpAffine(image, shear_matrix, (cols, rows))
