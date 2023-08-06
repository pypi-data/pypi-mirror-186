from __future__ import division

from collections import defaultdict

import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from pybsc.data import font_path


category_trans = int(0.6 * 255)


def visualize_bboxes(img, bboxes, labels=None, copy=False,
                     font_size=None, box_color=(191, 40, 41),
                     box_alpha=255,
                     text_alpha=None,
                     background_alpha=None,
                     font_ratio=20,
                     text_colors=None):
    """Visualize bounding boxes.

    Note that if alpha is 0, the target color will be transparent.
    """
    height, width, _ = img.shape
    long_side = min(width, height)
    font_size = font_size or max(int(round((long_side / font_ratio))), 1)
    box_width = max(int(round(long_side / 180)), 1)
    font = ImageFont.truetype(font_path(), font_size)

    result_vis = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(result_vis)

    for _, (y1, x1, y2, x2) in bboxes:
        draw.rectangle((x1, y1, x2, y2), outline=box_color + (box_alpha,),
                       width=box_width)

    bbox_captions = defaultdict(list)
    if labels is not None:
        if len(labels) > 0:
            if len(labels[0]) == 3:
                for i_box, label, color in labels:
                    bbox_captions[i_box].append((label, color, 'left top'))
            elif len(labels[0]) == 4:
                for i_box, label, color, loc in labels:
                    bbox_captions[i_box].append((label, color, loc))

    alpha = background_alpha if background_alpha is not None \
        else category_trans
    text_alpha = text_alpha if text_alpha is not None else category_trans
    text_color = (255, 255, 255)
    for i_box, (score, box) in enumerate(bboxes):
        captions = []
        bg_colors = []
        locs = []

        loc = 'left top'
        for label, color, loc in bbox_captions[i_box]:
            captions.append(label)
            bg_colors.append(color)
            locs.append(loc)

        if score is not None:
            conf = " %.2f" % score
            captions.append('score ' + conf)
            bg_colors.append((176, 85, 234))
            locs.append(loc)

        if len(captions) == 0:
            continue
        y1, x1, y2, x2 = box
        overlay = Image.new("RGBA", result_vis.size, (0, 0, 0, 0))
        trans_draw = ImageDraw.Draw(overlay)
        caption_sizes = [trans_draw.textsize(caption, font=font)
                         for caption in captions]
        caption_widths, caption_heights = list(zip(*caption_sizes))
        max_height = max(caption_heights)
        rec_height = int(round(1.8 * max_height))
        space_height = int(round(0.2 * max_height))
        total_height = (rec_height + space_height) \
            * (len(captions) - 1) \
            + rec_height
        width_pad = max(font_size // 2, 1)
        start_y = max(round(y1) - total_height, space_height)

        right_i = 0
        left_i = 0
        for i, (caption, loc) in enumerate(zip(captions, locs)):
            height_pad = round((rec_height - caption_heights[i]) / 2)
            if loc == 'left top':
                r_x1 = round(x1)
                r_y1 = start_y + (rec_height + space_height) * left_i
                r_x2 = r_x1 + caption_widths[i] + width_pad * 2
                r_y2 = r_y1 + rec_height
                left_i += 1
            elif loc == 'right top':
                r_y1 = start_y + (rec_height + space_height) * right_i
                r_x1 = x2 - (caption_widths[i] + width_pad * 2)
                r_y2 = r_y1 + rec_height
                r_x2 = x2
                right_i += 1
            else:
                raise RuntimeError
            rec_pos = (r_x1, r_y1, r_x2, r_y2)
            text_pos = (r_x1 + width_pad, r_y1 + height_pad)

            trans_draw.rectangle(rec_pos, fill=bg_colors[i]
                                 + (int(alpha),))
            # TODO(iory) Fix text color.
            if np.linalg.norm(
                    np.array(bg_colors[i]) - np.array(text_color)) <= 40:
                tc = (0, 0, 0)
            else:
                tc = text_color
            trans_draw.text(text_pos, caption,
                            fill=tc + (text_alpha,), font=font,
                            align="center")
        result_vis = Image.alpha_composite(result_vis, overlay)

    pil_img = Image.fromarray(img[..., ::-1])
    pil_img = pil_img.convert("RGBA")
    pil_img = Image.alpha_composite(pil_img, result_vis)
    pil_img = pil_img.convert("RGB")
    if copy:
        return np.array(pil_img, dtype=np.uint8)[..., ::-1]
    else:
        img[:] = np.array(pil_img, dtype=np.uint8)[..., ::-1]
        return img
