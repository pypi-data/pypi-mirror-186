from __future__ import division

import random

import numpy as np


def coloring(img, w_i, h_i, check_w, check_h, color_n, color1, color2):
    if color_n % 2 == 0:
        c = color1
    else:
        c = color2
    max_w, max_h = img.shape[:2]
    w_s = check_w * w_i
    w_e = check_w * (w_i + 1)
    if w_e > max_w:
        w_e = max_w
    h_s = check_h * h_i
    h_e = check_h * (h_i + 1)
    if h_e > max_h:
        h_e = max_h

    img[w_s:w_e, h_s:h_e, :] = c
    return img


def generate_single_color_texture(size_wh=(300, 300)):
    w, h = list(map(int, size_wh))
    color = [np.random.randint(0, 255), np.random.randint(
        0, 255), np.random.randint(0, 255)]
    np_img = np.array([color for _ in range(w*h)]).astype(np.uint8)
    np_img = np.reshape(np_img, (w, h, 3))
    return np_img


def generate_check_texture(size_wh=(300, 300)):
    w, h = list(map(int, size_wh))
    np_img = np.zeros([w, h, 3]).astype(np.uint8)
    color_n = 0
    color1 = [np.random.randint(0, 255), np.random.randint(
        0, 255), np.random.randint(0, 255)]
    color2 = [np.random.randint(0, 255), np.random.randint(
        0, 255), np.random.randint(0, 255)]
    check_w = np.random.randint(1, w / 2)
    check_h = np.random.randint(1, h / 2)
    w_iter = int(w / check_w)
    h_iter = int(h / check_h)
    for wi in range(w_iter + 1):
        for hi in range(h_iter + 1):
            np_img = coloring(np_img, wi, hi, check_w,
                              check_h, color_n, color1, color2)
            color_n += 1
    return np_img


def generate_gradation_texture(size_wh=(300, 300)):
    w, h = list(map(int, size_wh))
    np_img = np.zeros([w, h, 3]).astype(np.uint8)
    color1 = [np.random.randint(0, 255), np.random.randint(
        0, 255), np.random.randint(0, 255)]
    color2 = [np.random.randint(0, 255), np.random.randint(
        0, 255), np.random.randint(0, 255)]
    color3 = [np.random.randint(0, 255), np.random.randint(
        0, 255), np.random.randint(0, 255)]
    w_colors = np.array(
        [np.interp(np.arange(w), [0, w],
                   [color1[i], color2[i]]) for i in range(3)])
    h_colors = np.array(
        [np.interp(np.arange(h), [0, h],
                   [color1[i], color3[i]]) for i in range(3)])

    for wi in range(w):
        for hi in range(h):
            c = (w_colors[:, wi] + h_colors[:, hi]) / 2
            c = c.astype(np.uint8)
            np_img[wi, hi] = c
    return np_img


def generate_synthetic_texture(size_wh=(300, 300), style=None):
    valid_style = ['single', 'gradation', 'check']
    if style is None:
        style = random.choice(
            valid_style)

    if style == 'single':
        return generate_single_color_texture(size_wh)
    elif style == 'check':
        return generate_check_texture(size_wh)
    elif style == 'gradation':
        return generate_gradation_texture(size_wh)
    else:
        raise RuntimeError('Invalid style, {}.'
                           'Valid styles are {}.'
                           .format(style, valid_style))
