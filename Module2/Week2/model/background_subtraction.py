import numpy as np


def compute_difference(bg_img, inp_img):
    diff_single_channel = abs(bg_img - inp_img)
    return diff_single_channel


def compute_binary_mask(diff_single_channel):
    diff_binary = np.where(diff_single_channel == 0, 0, 1)
    return diff_binary


def replace_background(bg_img, new_bg_img, inp_img):
    diff_single_channel = compute_difference(bg_img, inp_img)
    binary_mask = compute_binary_mask(diff_single_channel)
    output = np.where(binary_mask, inp_img, new_bg_img)
    return output


