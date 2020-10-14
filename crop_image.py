import os
import cv2
import numpy as np
from show_image import plot_image
from save_image_to_file import print_image


def crop(img, x, y, h, w,path_to_output='',output_fileName='',mode='plot'):
    """Crop image.
       Inputs:
       img       = RGB, grayscale, or hyperspectral image data
       x         = X coordinate of starting point
       y         = Y coordinate of starting point
       h         = Height
       w         = Width
       Returns:
       cropped   = cropped image
       :param img: numpy.ndarray
       :param x: int
       :param y: int
       :param h: int
       :param w: int
       :return cropped: numpy.ndarray
       """

    # Check if the array data format
    if len(np.shape(img)) > 2 and np.shape(img)[-1] > 3:
        ref_img = img[:, :, [0]]
        ref_img = np.transpose(np.transpose(ref_img)[0])
        cropped = img[y:y + h, x:x + w, :]
    else:
        ref_img = np.copy(img)
        cropped = img[y:y + h, x:x + w]
    if mode != "save_crop":
        # Create the rectangle contour vertices
        pt1 = (x, y)
        pt2 = (x + w - 1, y + h - 1)

        ref_img = cv2.rectangle(img=ref_img, pt1=pt1, pt2=pt2, color=(0, 0, 255), thickness=6)

    if mode == "print":
        # If debug is print, save the image to a file
        print_image(ref_img, os.path.join(path_to_output, "originalWithCrop_"+ output_fileName))
    elif mode == "plot":
        # If debug is plot, print to the plotting device
        plot_image(ref_img)
    elif mode == "save_crop":
        print_image(cropped, os.path.join(path_to_output, "crop_"+ output_fileName))

    return cropped