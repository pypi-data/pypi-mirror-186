import cv2
import numpy as np


class ColorFilter(object):

    def __init__(self):
        pass


class HSVColorFilter(ColorFilter):

    def __init__(self,
                 h_max=360, h_min=0,
                 s_max=256, s_min=0,
                 v_max=256, v_min=0):
        super(HSVColorFilter, self).__init__()
        self.update_condition(
            h_max, h_min, s_max, s_min, v_max, v_min)

    def update_condition(
            self, h_max=None, h_min=None,
            s_max=None, s_min=None, v_max=None, v_min=None):
        if h_min is not None:
            self.h_min = h_min
        if h_max is not None:
            self.h_max = h_max
        if s_min is not None:
            self.s_min = s_min
        if s_max is not None:
            self.s_max = s_max
        if v_min is not None:
            self.v_min = v_min
        if v_max is not None:
            self.v_max = v_max
        if self.s_max < self.s_min:
            self.s_max, self.s_min = self.s_min, self.s_max
        if self.v_max < self.v_min:
            self.v_max, self.v_min = self.v_min, self.v_max
        self.lower_color_range = np.array([
            self.h_min / 2.0, self.s_min, self.v_min, 0])
        self.upper_color_range = np.array([
            self.h_max / 2.0, self.s_max, self.v_max, 0])

    def filter(self, bgr_img):
        hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)
        if self.lower_color_range[0] < self.upper_color_range[0]:
            mask = cv2.inRange(hsv_img,
                               self.lower_color_range,
                               self.upper_color_range)
        else:
            lower_color_range_0 = np.array((0, self.s_min, self.v_min, 0),
                                           dtype=np.float64)
            upper_color_range_0 = np.array((self.h_max / 2.0,
                                            self.s_max, self.v_max, 0),
                                           dtype=np.float64)
            lower_color_range_360 = np.array((self.h_min / 2.0,
                                              self.s_min, self.v_min, 0),
                                             dtype=np.float64)
            upper_color_range_360 = np.array(
                (360 / 2.0, self.s_max, self.v_max, 0), dtype=np.float64)
            mask_0 = cv2.inRange(hsv_img,
                                 lower_color_range_0, upper_color_range_0)
            mask_360 = cv2.inRange(
                hsv_img, lower_color_range_360, upper_color_range_360)
            mask = np.array(
                np.logical_or(mask_0, mask_360) * 255, dtype=np.uint8)
        return mask


class LabColorFilter(ColorFilter):

    def __init__(self,
                 l_max=255,
                 l_min=0,
                 a_max=255,
                 a_min=0,
                 b_max=255,
                 b_min=0):
        super(LabColorFilter, self).__init__()
        self.update_condition(
            l_max, l_min,
            a_max, a_min,
            b_max, b_min)

    def update_condition(self,
                         l_max=None, l_min=None,
                         a_max=None, a_min=None,
                         b_max=None, b_min=None):
        if l_min is not None:
            self.l_min = l_min
        if l_max is not None:
            self.l_max = l_max
        if a_min is not None:
            self.a_min = a_min
        if a_max is not None:
            self.a_max = a_max
        if b_min is not None:
            self.b_min = b_min
        if b_max is not None:
            self.b_max = b_max
        self.lower_color_range = np.array(
            [self.l_min, self.a_min, self.b_min])
        self.upper_color_range = np.array(
            [self.l_max, self.a_max, self.b_max])

    def filter(self, bgr_img):
        lab_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2Lab)
        print(self.lower_color_range)
        print(self.upper_color_range)
        mask = cv2.inRange(lab_img,
                           self.lower_color_range,
                           self.upper_color_range)
        return mask


def hsv_color_filter(bgr_img,
                     h_max=360, h_min=0,
                     s_max=256, s_min=0,
                     v_max=256, v_min=0):
    return HSVColorFilter(
        h_max, h_min, s_max, s_min, v_max, v_min).filter(bgr_img)


def lab_color_filter(bgr_img,
                     l_max=255, l_min=0,
                     a_max=255, a_min=0,
                     b_max=255, b_min=0):
    return LabColorFilter(
        l_max, l_min, a_max, a_min, b_max, b_min).filter(bgr_img)
