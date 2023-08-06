# Jan-18-2023
# code.py

import cv2 as cv
import numpy as np


def vc_filter(image):

    # convert color image to grayscale
    if len(image.shape) != 2:
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # check image size
    border = 4
    rows, cols = image.shape
    if rows < border or cols < border:
        image[:, :] = 0
        return image    # image is too small

    image_max_size = max(rows, cols)
    size_dft = 256
    while image_max_size > size_dft:
        size_dft *= 2

    width_dft = size_dft
    height_dft = size_dft

    """  Filter (Sobel based)  """
    # ---------------------------------------------------------
    dft_filter_accum = sobel_accum(height_dft, width_dft)
    # ---------------------------------------------------------

    """  Image  """
    # ---------------------------------------------------------
    array_image = np.zeros((height_dft, width_dft), dtype='float32')

    x0 = (width_dft - cols) // 2
    y0 = (height_dft - rows) // 2

    array_image[y0:y0 + rows, x0:x0 + cols] = image[0::, 0::]

    dft_image = cv.dft(array_image, flags=cv.DFT_COMPLEX_OUTPUT)

    # DFT{Image}
    dft_image_shift = np.fft.fftshift(dft_image)
    # ---------------------------------------------------------

    """  DFT{Filter} * DFT{Image}  """
    # -----------------------------------------
    dft_product_shift = np.empty((height_dft, width_dft, 2), dtype='float32')

    x1 = dft_filter_accum[:, :, 0]
    y1 = dft_filter_accum[:, :, 1]

    x2 = dft_image_shift[:, :, 0]
    y2 = dft_image_shift[:, :, 1]

    dft_product_shift[:, :, 0] = (x1 * x2) - (y1 * y2)
    dft_product_shift[:, :, 1] = (x1 * y2) + (x2 * y1)
    # -----------------------------------------

    """  Inverse DFT """
    # -----------------------------------------
    inverse_dft = cv.idft(dft_product_shift)

    re = inverse_dft[:, :, 0]

    re[re < 0.0] = 0.0
    # -----------------------------------------

    #  Get filtered image
    # -----------------------------------------
    image_array = np.empty((rows, cols), dtype='float32')

    x0 = (width_dft - cols) // 2
    y0 = (height_dft - rows) // 2

    image_array[::, ::] = re[y0:y0 + rows, x0:x0 + cols]
    # -----------------------------------------

    #  Remove "border noise"
    # -----------------------------------------
    image_array[0:border, 0:cols] = 0.0
    image_array[rows - border:rows, 0:cols] = 0.0
    image_array[0:rows, 0:border] = 0.0
    image_array[0:rows, cols - border:cols] = 0.0
    # -----------------------------------------

    #  Normalization
    # -----------------------------------------
    min_value = np.amin(image_array)
    max_value = np.amax(image_array)

    if min_value < max_value:
        coeff = 255.0 / (max_value - min_value)
        image_array = coeff * (image_array - min_value)
        image_array[image_array < 0.0] = 0.0
        image_array[image_array > 255.0] = 255.0
    else:
        image_array[:, :] = 0.0

    image_array_8u = np.uint8(image_array)
    # -----------------------------------------

    #  Both flips
    image_edges = cv.flip(image_array_8u, -1)

    return image_edges


def sobel_accum(height_dft, width_dft):

    # Simple Sobel
    # ---------------------------------------------------------
    array_filter = sobel_kernel(height_dft, width_dft)

    dft_filter = cv.dft(array_filter, flags=cv.DFT_COMPLEX_OUTPUT)

    # DFT{Filter}
    dft_filter_shift = np.fft.fftshift(dft_filter)
    # ---------------------------------------------------------

    # Accumulate
    # ---------------------------------------------------------
    dft_filter_accum = np.zeros((height_dft, width_dft, 2), dtype='float32')

    # The value 12 was obtained experimentally in the visual cortex study.
    angle_step = 12

    for angle in range(0, 180, angle_step):

        if angle > 0:
            dft_filter_shift_rot = dft_rotate(
                dft_filter_shift,
                height_dft, width_dft,
                angle)

            dft_filter_accum[:, :, 0] += dft_filter_shift_rot[:, :, 0]
            dft_filter_accum[:, :, 1] += dft_filter_shift_rot[:, :, 1]
        else:
            dft_filter_accum[:, :, 0] += dft_filter_shift[:, :, 0]
            dft_filter_accum[:, :, 1] += dft_filter_shift[:, :, 1]
    # ---------------------------------------------------------

    return dft_filter_accum


def sobel_kernel(height_dft, width_dft):

    array_filter = np.zeros((height_dft, width_dft), dtype='float32')

    array_filter[0, 0] = 1
    array_filter[0, 1] = 2
    array_filter[0, 2] = 1

    array_filter[1, 0] = 0
    array_filter[1, 1] = 0
    array_filter[1, 2] = 0

    array_filter[2, 0] = -1
    array_filter[2, 1] = -2
    array_filter[2, 2] = -1

    return array_filter


def dft_rotate(dft, height_dft, width_dft, angle):

    re = dft[:, :, 0]
    im = dft[:, :, 1]

    M = cv.getRotationMatrix2D((width_dft / 2, height_dft / 2), angle, 1)

    re_rot = cv.warpAffine(re, M, (width_dft, height_dft))
    im_rot = cv.warpAffine(im, M, (width_dft, height_dft))

    dft_rot = cv.merge([re_rot, im_rot])

    return dft_rot
