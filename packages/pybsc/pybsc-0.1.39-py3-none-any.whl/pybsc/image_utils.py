from __future__ import division

import base64
from enum import Enum

import cv2
import numpy as np
import PIL
from PIL.Image import Image as PILImage
from shapely.geometry import Polygon

from pybsc.tile import squared_tile


try:
    from turbojpeg import TurboJPEG
    jpeg = TurboJPEG()
except Exception:
    jpeg = None


class ReturnType(Enum):
    BYTES = 0
    PILLOW = 1
    NDARRAY = 2


def str_to_pil_interpolation(interpolation):
    if interpolation == 'nearest':
        return PIL.Image.NEAREST
    elif interpolation == 'bilinear':
        return PIL.Image.BILINEAR
    elif interpolation == 'bicubic':
        return PIL.Image.BICUBIC
    elif interpolation == 'lanczos':
        return PIL.Image.LANCZOS
    else:
        raise ValueError(
            'Not valid Interpolation. '
            'Valid interpolation methods are '
            'nearest, bilinear, bicubic and lanczos.')


def pil_to_cv2_interpolation(interpolation):
    if isinstance(interpolation, str):
        interpolation = interpolation.lower()
        if interpolation == 'nearest':
            cv_interpolation = cv2.INTER_NEAREST
        elif interpolation == 'bilinear':
            cv_interpolation = cv2.INTER_LINEAR
        elif interpolation == 'bicubic':
            cv_interpolation = cv2.INTER_CUBIC
        elif interpolation == 'lanczos':
            cv_interpolation = cv2.INTER_LANCZOS4
        else:
            raise ValueError(
                'Not valid Interpolation. '
                'Valid interpolation methods are '
                'nearest, bilinear, bicubic and lanczos.')
    else:
        if interpolation == PIL.Image.NEAREST:
            cv_interpolation = cv2.INTER_NEAREST
        elif interpolation == PIL.Image.BILINEAR:
            cv_interpolation = cv2.INTER_LINEAR
        elif interpolation == PIL.Image.BICUBIC:
            cv_interpolation = cv2.INTER_CUBIC
        elif interpolation == PIL.Image.LANCZOS:
            cv_interpolation = cv2.INTER_LANCZOS4
        else:
            raise ValueError(
                'Not valid Interpolation. '
                'Valid interpolation methods are '
                'PIL.Image.NEAREST, PIL.Image.BILINEAR, '
                'PIL.Image.BICUBIC and PIL.Image.LANCZOS.')
    return cv_interpolation


def decode_image_cv2(b64encoded):
    bin = b64encoded.split(",")[-1]
    bin = base64.b64decode(bin)
    bin = np.frombuffer(bin, np.uint8)
    img = cv2.imdecode(bin, cv2.IMREAD_COLOR)
    return img


def decode_image_turbojpeg(b64encoded):
    bin = b64encoded.split(",")[-1]
    bin = base64.b64decode(bin)
    img = jpeg.decode(bin)
    return img


def decode_image(b64encoded):
    if jpeg is not None:
        img = decode_image_turbojpeg(b64encoded)
    else:
        img = decode_image_cv2(b64encoded)
    return img


def encode_image_turbojpeg(img):
    bin = jpeg.encode(img)
    b64encoded = base64.b64encode(bin).decode('ascii')
    return b64encoded


def encode_image_cv2(img, quality=90):
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    result, encimg = cv2.imencode('.jpg', img, encode_param)
    b64encoded = base64.b64encode(encimg).decode('ascii')
    return b64encoded


def encode_image(img):
    if jpeg is not None:
        img = encode_image_turbojpeg(img)
    else:
        img = encode_image_cv2(img)
    return img


def get_size(img):
    if isinstance(img, PILImage):
        return img.size
    elif isinstance(img, np.ndarray):
        return (img.shape[1], img.shape[0])
    else:
        raise RuntimeError('input img should be PILImage or numpy.ndarray'
                           ', get {}'.format(type(img)))


def resize_keeping_aspect_ratio(img, width=None, height=None,
                                interpolation='bilinear',
                                return_scale=False):
    if (width and height) or (width is None and height is None):
        raise ValueError('Only width or height should be specified.')
    if isinstance(img, PILImage):
        if width == img.size[0] and height == img.size[1]:
            return img
        if width:
            scale = width / img.size[0]
            height = scale * img.size[1]
        else:
            scale = height / img.size[1]
            width = scale * img.size[0]
        height = int(height)
        width = int(width)
        resized_img = img.resize(
            (width, height),
            resample=str_to_pil_interpolation(interpolation))
    elif isinstance(img, np.ndarray):
        if width == img.shape[1] and height == img.shape[0]:
            return img
        if width:
            scale = width / img.shape[1]
            height = scale * img.shape[0]
        else:
            scale = height / img.shape[0]
            width = scale * img.shape[1]
        height = int(height)
        width = int(width)
        cv_interpolation = pil_to_cv2_interpolation(interpolation)
        resized_img = cv2.resize(img, (width, height),
                                 interpolation=cv_interpolation)
    else:
        raise ValueError(
            "Input type {} is not supported.".format(type(img)))
    if return_scale:
        return resized_img, scale
    else:
        return resized_img


def resize_keeping_aspect_ratio_wrt_longside(img, length,
                                             interpolation='bilinear',
                                             return_scale=False):
    if isinstance(img, PILImage):
        W, H = img.size
        aspect = W / H
        if H > W:
            width = length * aspect
            scale = length / H
            resized_img = img.resize(
                (int(width), int(length)),
                resample=str_to_pil_interpolation(interpolation))
        else:
            height = length / aspect
            scale = length / W
            resized_img = img.resize(
                (int(length), int(height)),
                resample=str_to_pil_interpolation(interpolation))
    elif isinstance(img, np.ndarray):
        cv_interpolation = pil_to_cv2_interpolation(interpolation)
        H, W = img.shape[:2]
        aspect = W / H
        if H > W:
            width = length * aspect
            scale = length / H
            resized_img = cv2.resize(
                img, (int(width), int(length)),
                interpolation=cv_interpolation)
        else:
            height = length / aspect
            scale = length / W
            resized_img = cv2.resize(
                img, (int(length), int(height)),
                interpolation=cv_interpolation)
    else:
        raise ValueError(
            "Input type {} is not supported.".format(type(img)))
    if return_scale:
        return resized_img, scale
    else:
        return resized_img


def resize_keeping_aspect_ratio_wrt_target_size(
        img, width, height, interpolation='bilinear',
        background_color=(0, 0, 0)):
    if width == img.shape[1] and height == img.shape[0]:
        return img
    H, W, _ = img.shape
    ratio = min(float(height) / H, float(width) / W)
    M = np.array([[ratio, 0, 0],
                  [0, ratio, 0]], dtype=np.float32)
    dst = np.zeros((int(height), int(width), 3), dtype=img.dtype)
    return cv2.warpAffine(
        img, M,
        (int(width), int(height)),
        dst,
        cv2.INTER_CUBIC, cv2.BORDER_CONSTANT,
        background_color)


def squared_padding_image(img, length=None):
    H, W = img.shape[:2]
    if H > W:
        if length is not None:
            img = resize_keeping_aspect_ratio_wrt_longside(img, length)
        margin = img.shape[0] - img.shape[1]
        img = np.pad(img,
                     [(0, 0),
                      (margin // 2, margin - margin // 2),
                      (0, 0)], 'constant')
    else:
        if length is not None:
            img = resize_keeping_aspect_ratio_wrt_longside(img, length)
        margin = img.shape[1] - img.shape[0]
        img = np.pad(img,
                     [(margin // 2, margin - margin // 2),
                      (0, 0), (0, 0)], 'constant')
    return img


def concat_with_keeping_aspect(
        imgs, width, height,
        tile_shape=None):
    if len(imgs) == 0:
        raise ValueError
    if tile_shape is None:
        tile_x, tile_y = squared_tile(len(imgs))
    else:
        tile_x, tile_y = tile_shape

    w = width // tile_x
    h = height // tile_y

    ret = []
    max_height = h
    max_width = w
    for img in imgs:
        if img.shape[1] / w > img.shape[0] / h:
            tmp_img = resize_keeping_aspect_ratio(img, width=w, height=None)
        else:
            tmp_img = resize_keeping_aspect_ratio(img, width=None, height=h)
        ret.append(tmp_img)

    canvas = np.zeros((height, width, 3),
                      dtype=np.uint8)

    i = 0
    for y in range(tile_y):
        for x in range(tile_x):
            lh = (max_height - ret[i].shape[0]) // 2
            rh = (max_height - ret[i].shape[0]) - lh
            lw = (max_width - ret[i].shape[1]) // 2
            rw = (max_width - ret[i].shape[1]) - lw
            img = np.pad(ret[i],
                         [(lh, rh),
                          (lw, rw),
                          (0, 0)], 'constant')
            canvas[y * max_height:(y + 1) * max_height,
                   x * max_width:(x + 1) * max_width] = img
            i += 1
            if i >= len(imgs):
                break
        if i >= len(imgs):
            break
    return canvas


def mask_to_bbox(mask, threshold=0):
    if isinstance(mask, PILImage):
        mask = np.array(mask)
    elif isinstance(mask, np.ndarray):
        pass
    else:
        raise TypeError('Invalid input image type, {}'.format(type(mask)))
    mask = mask > threshold
    mask_indexes = np.where(mask)
    y_min = np.min(mask_indexes[0])
    y_max = np.max(mask_indexes[0])
    x_min = np.min(mask_indexes[1])
    x_max = np.max(mask_indexes[1])
    return (y_min, x_min, y_max, x_max)


def masks_to_bboxes(mask):
    R, _, _ = mask.shape
    instance_index, ys, xs = np.nonzero(mask)
    bboxes = np.zeros((R, 4), dtype=np.float32)
    for i in range(R):
        ys_i = ys[instance_index == i]
        xs_i = xs[instance_index == i]
        if len(ys_i) == 0:
            continue
        y_min = ys_i.min()
        x_min = xs_i.min()
        y_max = ys_i.max() + 1
        x_max = xs_i.max() + 1
        bboxes[i] = np.array(
            [x_min, y_min, x_max, y_max],
            dtype=np.float32)
    return bboxes


def alpha_blend(a_img, b_img, alpha=0.5):
    viz = cv2.addWeighted(a_img, alpha, b_img, 1 - alpha, 0)
    return viz


def zoom(img, ratio=1.0, interpolation='bilinear'):
    """zoom function resize and crop images.

    Parameters
    ----------
    img : np.ndarray
        input image (C, H, W)
    ration : float
        zoom ratio
        should be greater than 1.0.
    Returns
    -------
    cropped_img : np.ndarray
        zoomed image
    """
    if ratio < 1.0:
        raise ValueError('ratio should be greater than 1.0, but given {}'.
                         format(ratio))
    w, h = get_size(img)
    H = int(h * ratio)
    W = int(w * ratio)
    resized_img = resize_keeping_aspect_ratio(
        img, height=H,
        interpolation=interpolation)
    cropped_img = resized_img[(H - h) // 2:(H - h) // 2 + h,
                              (W - w) // 2:(W - w) // 2 + w,
                              :]
    return cropped_img


def tile_image(wh_size, tile_size_wh, window_size=None):
    w, h = wh_size
    if isinstance(tile_size_wh, tuple) or isinstance(tile_size_wh, list):
        tile_width, tile_height = tile_size_wh
    else:
        tile_width, tile_height = tile_size_wh, tile_size_wh

    if window_size is None:
        window_h = tile_height
        window_w = tile_width
    else:
        if isinstance(window_size, tuple) or isinstance(window_size, list):
            window_w, window_h = window_size
        else:
            window_w = window_size
            window_h = window_size

    tile_w = tile_width
    tile_h = tile_height

    x = np.arange(0, w - tile_w, window_w)
    if (w - tile_w) % tile_w != 0:
        x = np.concatenate([x, np.array([w - tile_w])])
    y = np.arange(0, h - tile_h, window_h)
    if (h - tile_h) % tile_h != 0:
        y = np.concatenate([y, np.array([h - tile_h])])

    sx, sy = np.meshgrid(x, y)
    sx = sx.reshape(-1)
    ex = sx + tile_w
    sy = sy.reshape(-1)
    ey = sy + tile_h

    return np.array(
        [((sx[i], sy[i], ex[i] - sx[i], ey[i] - sy[i]))
         for i in range(len(sx))])


def get_bboxes_from_tile(bboxes, tile):
    new_bboxes = []
    for y1, x1, y2, x2 in bboxes:
        new_bboxes.append(Polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)]))
    bboxes = new_bboxes
    x1, y1, w, h = tile
    x2, y2 = x1 + w, y1 + h
    pol = Polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)])
    sliced_bboxes = []
    indices = []
    for box_idx, box in enumerate(bboxes):
        if pol.intersects(box):
            inter = pol.intersection(box)
            # get the smallest polygon
            # (with sides parallel to the coordinate axes)
            # that contains the intersection
            new_box = inter.envelope

            # get coordinates of polygon vertices
            x, y = new_box.exterior.coords.xy
            x = x - x1
            y = y - y1

            sliced_bboxes.append([min(y), min(x), max(y), max(x)])
            indices.append(box_idx)
    return sliced_bboxes, indices


def non_maximum_suppression(bbox, thresh, score=None, limit=None):
    if len(bbox) == 0:
        return np.zeros((0,), dtype=np.int32)

    if score is not None:
        order = score.argsort()[::-1]
        bbox = bbox[order]
    bbox_area = np.prod(bbox[:, 2:] - bbox[:, :2], axis=1)

    indices = np.zeros(bbox.shape[0], dtype=bool)
    for i, b in enumerate(bbox):
        tl = np.maximum(b[:2], bbox[indices, :2])
        br = np.minimum(b[2:], bbox[indices, 2:])
        area = np.prod(br - tl, axis=1) * (tl < br).all(axis=1)

        iou = area / (bbox_area[i] + bbox_area[indices] - area)
        if (iou >= thresh).any():
            continue

        indices[i] = True
        if limit is not None and np.count_nonzero(indices) >= limit:
            break

    indices = np.where(indices)[0]
    if score is not None:
        indices = order[indices]
    return indices.astype(np.int32)
