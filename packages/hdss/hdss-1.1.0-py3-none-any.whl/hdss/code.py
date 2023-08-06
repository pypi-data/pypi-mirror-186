# Jan-15-2023
# code.py

import os
import cv2 as cv
import numpy as np
import random


# main parameters
# -----------------------------
image_size = 0
n_shapes = 0
perspective_flag = False
bezier_noise_param = 0
line_color = (0, 0, 0)
line_thickness = 0
# -----------------------------

# Perspective transform
# Points order: top-right, top-left, bottom-left, bottom-right
# -----------------------------
x_tr_in = 0
y_tr_in = 0
x_tl_in = 0
y_tl_in = 0
x_bl_in = 0
y_bl_in = 0
x_br_in = 0
y_br_in = 0

x_tr_out = 0
y_tr_out = 0
x_tl_out = 0
y_tl_out = 0
x_bl_out = 0
y_bl_out = 0
x_br_out = 0
y_br_out = 0
# -----------------------------


def set_params(
        _shape_size,
        _number_of_shapes,
        _perspective_flag,
        _bezier_noise_param,
        _line_color,
        _line_thickness):

    global image_size
    global n_shapes
    global perspective_flag
    global bezier_noise_param
    global line_color
    global line_thickness

    image_size = _shape_size
    n_shapes = _number_of_shapes
    perspective_flag = _perspective_flag
    bezier_noise_param = _bezier_noise_param
    line_color = _line_color
    line_thickness = _line_thickness


def create_shapes(shape_name, *curves):

    global n_shapes

    for number_of_shape in range(n_shapes):
        create_shape(number_of_shape, shape_name, *curves)


def create_shape(number_of_shape, shape_name, *curves):

    global image_size, perspective_flag

    # ---------------------------------------------------------
    height = image_size
    width = image_size
    channels = 3
    background = 255
    image = np.empty((height, width, channels), dtype=np.uint8)
    image.fill(background)
    # ---------------------------------------------------------
    scale_factor = np.float32(image_size) / np.float32(100)

    M_perspective = (3, 3)
    M_perspective = np.zeros(M_perspective, dtype=np.float32)

    if perspective_flag:
        M_perspective = set_persp_transform()
    # ---------------------------------------------------------
    for path_curve in curves:

        control_points = np.loadtxt(path_curve, delimiter=',')
        n_control_points = control_points.shape[0]

        control_points = scale_factor * control_points
        # -----------------------------------------------------

        # Perspective Transform
        # -----------------------------------------------------
        if perspective_flag:

            for n in range(n_control_points):
                x_in = control_points[n, 0]
                y_in = control_points[n, 1]

                x_out, y_out = point_persp_transform(M_perspective, x_in, y_in)

                control_points[n, 0] = x_out
                control_points[n, 1] = y_out
        # -----------------------------------------------------

        # Random Noise
        # -----------------------------------------------------
        if bezier_noise_param != 0:
            for n in range(n_control_points):
                control_points[n, 0] = control_points[n, 0] + random_noise(scale_factor)
                control_points[n, 1] = control_points[n, 1] + random_noise(scale_factor)
        # -----------------------------------------------------

        bezier_image(image, control_points)

    shape_dir = set_shape_directory(shape_name)
    path_shape = shape_dir + '/' + shape_name + '_' + str(number_of_shape) + '.png'
    cv.imwrite(path_shape, image)


def set_persp_transform():

    global image_size, perspective_flag
    global x_tr_in, y_tr_in, x_tl_in, y_tl_in, x_bl_in, y_bl_in, x_br_in, y_br_in
    global x_tr_out, y_tr_out, x_tl_out, y_tl_out, x_bl_out, y_bl_out, x_br_out, y_br_out

    if not perspective_flag:

        x_tr_in = image_size
        y_tr_in = 0

        x_tl_in = 0
        y_tl_in = 0

        x_bl_in = 0
        y_bl_in = image_size

        x_br_in = image_size
        y_br_in = image_size

        M = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]

        return M

    # Points order: top-right, top-left, bottom-left, bottom-right

    # IN
    # -----------------------------------------------------
    random.seed(None)

    x_tr_in = image_size + random_perspective_shift()
    y_tr_in = -random_perspective_shift()

    x_tl_in = -random_perspective_shift()
    y_tl_in = -random_perspective_shift()

    x_bl_in = -random_perspective_shift()
    y_bl_in = image_size + random_perspective_shift()

    x_br_in = image_size + random_perspective_shift()
    y_br_in = image_size + random_perspective_shift()
    # -----------------------------------------------------

    # OUT
    # ---------------------------------------------------------
    x_tr_out = image_size
    y_tr_out = 0

    x_tl_out = 0
    y_tl_out = 0

    x_bl_out = 0
    y_bl_out = image_size

    x_br_out = image_size
    y_br_out = image_size
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    pts1 = np.float32([[x_tr_in, y_tr_in], [x_tl_in, y_tl_in],
                       [x_bl_in, y_bl_in], [x_br_in, y_br_in]])

    pts2 = np.float32([[x_tr_out, y_tr_out], [x_tl_out, y_tl_out],
                       [x_bl_out, y_bl_out], [x_br_out, y_br_out]])

    M = cv.getPerspectiveTransform(pts1, pts2)
    # ---------------------------------------------------------

    return M


def random_perspective_shift():

    global image_size

    return random.uniform(0.0, image_size / 2.0)


def point_persp_transform(M, x_in, y_in):
    x_out = M[0, 0] * x_in + M[0, 1] * y_in + M[0, 2]
    y_out = M[1, 0] * x_in + M[1, 1] * y_in + M[1, 2]
    z_out = M[2, 0] * x_in + M[2, 1] * y_in + M[2, 2]

    x_out = x_out / z_out
    y_out = y_out / z_out

    return x_out, y_out


def random_noise(scale_factor):

    global bezier_noise_param

    half = scale_factor * bezier_noise_param / 2.0

    return random.uniform(-half, half)


def bezier_image(image, points):

    global line_color, line_thickness

    curve = evaluate_bezier(points, 15)

    px, py = curve[:, 0], curve[:, 1]

    # Draw current curve
    # ---------------------------------------------------------
    for i in range(1, px.size):

        x1 = int(round(px[i-1]))
        y1 = int(round(py[i-1]))

        x2 = int(round(px[i]))
        y2 = int(round(py[i]))

        cv.line(image,
                (x1, y1), (x2, y2),
                line_color,
                line_thickness)
    # ---------------------------------------------------------


def remove_shape_directory(shape_name):

    cwd = os.getcwd()

    shape_dir = cwd + '/' + shape_name

    if os.path.isdir(shape_dir):
        for f in os.listdir(shape_dir):
            os.remove(os.path.join(shape_dir, f))
        os.rmdir(shape_dir)


def set_shape_directory(shape_name):

    cwd = os.getcwd()

    shape_dir = cwd + '/' + shape_name

    if not os.path.isdir(shape_dir):
        os.mkdir(shape_dir)

    return shape_dir


"""
    Omar Aflak  May 9, 2020.
    https://towardsdatascience.com/bézier-interpolation-8033e9a262c2
    
    Thanks, Omar!!!
"""


# find the a & b points
def get_bezier_coef(points):
    # since the formulas work given that we have n+1 points
    # then n must be this:
    n = len(points) - 1

    # build coefficents matrix
    C = 4 * np.identity(n)
    np.fill_diagonal(C[1:], 1)
    np.fill_diagonal(C[:, 1:], 1)
    C[0, 0] = 2
    C[n - 1, n - 1] = 7
    C[n - 1, n - 2] = 2

    # build points vector
    P = [2 * (2 * points[i] + points[i + 1]) for i in range(n)]
    P[0] = points[0] + 2 * points[1]
    P[n - 1] = 8 * points[n - 1] + points[n]

    # solve system, find a & b
    A = np.linalg.solve(C, P)
    B = [0] * n
    for i in range(n - 1):
        B[i] = 2 * points[i + 1] - A[i + 1]
    B[n - 1] = (A[n - 1] + points[n]) / 2

    return A, B


# returns the general Bezier cubic formula given 4 control points
def get_cubic(a, b, c, d):
    return lambda t: np.power(1 - t, 3) * a + 3 * np.power(1 - t, 2) * t * b + 3 * (1 - t) * np.power(t, 2) * c + np.power(t, 3) * d


# return one cubic curve for each consecutive points
def get_bezier_cubic(points):
    A, B = get_bezier_coef(points)
    return [
        get_cubic(points[i], A[i], B[i], points[i + 1])
        for i in range(len(points) - 1)
    ]


# evalute each cubic curve on the range [0, 1] sliced in n points
def evaluate_bezier(points, n):
    curves = get_bezier_cubic(points)
    return np.array([fun(t) for fun in curves for t in np.linspace(0, 1, n)])
