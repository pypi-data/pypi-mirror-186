import random

import cv2


def draw_joints(img, joint, color=None, thickness=3, radius=10):
    """
    Draw 2d hand joints on image
    :param img: image to draw
    :param joint: 2d hand joints. (21*2)
    """
    # fmt: off
    joint_id_start = [0, 0, 0, 0, 0, 1, 6, 7, 2, 9, 10, 3, 12, 13, 4, 15, 16, 5, 18, 19]
    joint_id_end = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    # fmt: on
    red = [48, 48, 255]
    green = [48, 255, 48]
    blue = [192, 101, 21]
    yellow = [0, 204, 255]
    purple = [128, 64, 128]
    cyan = [180, 229, 255]
    # fmt: off
    joint_color_list = [cyan, green, blue, yellow, purple, red, green, green, green, \
            blue, blue, blue, yellow, yellow, yellow, purple, purple, purple, red, red, red ]
    bone_color_list = [ green, blue, yellow, purple, red, green, green, green, blue, \
            blue, blue, yellow, yellow, yellow, purple, purple, purple, red, red, red ]
    # fmt: on

    for i in range(len(joint_id_start)):
        i1 = joint_id_start[i]
        i2 = joint_id_end[i]
        p1 = (int(joint[i1][0]), int(joint[i1][1]))
        p2 = (int(joint[i2][0]), int(joint[i2][1]))
        color_t = bone_color_list[i] if color is None else color
        cv2.line(img, p1, p2, color=color_t, thickness=thickness, lineType=cv2.LINE_AA)
    for i, j in enumerate(joint):
        p = int(j[0] * 4), int(j[1] * 4)
        color_t = joint_color_list[i] if color is None else color
        cv2.circle(
            img,
            p,
            radius=radius,
            color=[224, 224, 224],
            thickness=thickness,
            lineType=cv2.LINE_8,
            shift=2,
        )
        cv2.circle(
            img,
            p,
            radius=radius - 4,
            color=color_t,
            thickness=thickness,
            lineType=cv2.LINE_8,
            shift=2,
        )


def draw_joints2(img, joint, color=None, thickness=3, radius=10):
    """
    Draw 2d hand joints on image
    :param img: image to draw
    :param joint: 2d hand joints. (21*2)
    """
    # fmt: off
    joint_id_start = [0, 1, 6, 7, 1, 2, 9,  10, 3,  12, 13, 4,  15, 16, 0, 5,  18, 19, 2, 3, 4]
    joint_id_end =   [1, 6, 7, 8, 2, 9, 10, 11, 12, 13, 14, 15, 16, 17, 5, 18, 19, 20, 3, 4, 5]
    # fmt: on
    red = [0, 0, 255]
    green = [0, 255, 0]
    blue = [255, 0, 0]
    yellow = [0, 255, 255]
    purple = [200, 20, 250]
    cyan = [250, 200, 50]
    # fmt: off
    joint_color = green
    bone_color_list = [blue,blue,blue,blue,red,red,red,red,cyan,cyan,cyan,yellow,yellow,yellow, \
            purple,purple,purple,purple,green,green,green]
    # fmt: on

    for i in range(len(joint_id_start)):
        i1 = joint_id_start[i]
        i2 = joint_id_end[i]
        p1 = (int(joint[i1][0]), int(joint[i1][1]))
        p2 = (int(joint[i2][0]), int(joint[i2][1]))
        color_t = bone_color_list[i] if color is None else color
        cv2.line(img, p1, p2, color=color_t, thickness=thickness, lineType=cv2.LINE_AA)
    for i, j in enumerate(joint):
        p = int(j[0]), int(j[1])
        color_t = joint_color if color is None else color
        cv2.circle(
            img,
            p,
            radius=radius,
            color=color_t,
            thickness=-1,
            lineType=cv2.LINE_AA,
        )


def draw_one_box(img, bbox, color=None, label=None, line_thickness=None):
    """
    Draw one hand box on image
    :param img: image to draw
    :param bbox: hand bounding box. list or numpy.ndarray, xyxy
    :param color: box color
    :param label: box label
    """
    tl = (
        line_thickness or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1
    )  # line/font thickness
    color = color or [random.randint(0, 255) for _ in range(3)]
    c1, c2 = (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3]))
    cv2.rectangle(img, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
    if label:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(
            img,
            label,
            (c1[0], c1[1] - 2),
            0,
            tl / 3,
            [225, 255, 255],
            thickness=tf,
            lineType=cv2.LINE_AA,
        )


def draw_corner_box(img, bbox, label=None, k=30, t=4, rt=1):
    """
    Draw hand box with corner effects
    :param img: image to draw
    :param bbox: hand bounding box. list or numpy.ndarray, xyxy
    """
    colorR = (255, 0, 255)
    colorC = (0, 255, 0)
    x, y, x1, y1 = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])

    if rt != 0:
        cv2.rectangle(img, (x, y), (x1, y1), colorR, rt)
    # Top Left  x,y
    cv2.line(img, (x, y), (x + k, y), colorC, t)
    cv2.line(img, (x, y), (x, y + k), colorC, t)
    # Top Right  x1,y
    cv2.line(img, (x1, y), (x1 - k, y), colorC, t)
    cv2.line(img, (x1, y), (x1, y + k), colorC, t)
    # Bottom Left  x,y1
    cv2.line(img, (x, y1), (x + k, y1), colorC, t)
    cv2.line(img, (x, y1), (x, y1 - k), colorC, t)
    # Bottom Right  x1,y1
    cv2.line(img, (x1, y1), (x1 - k, y1), colorC, t)
    cv2.line(img, (x1, y1), (x1, y1 - k), colorC, t)
    if label:
        cv2.putText(
            img, label, (x, y - 4), 0, 1, colorR, thickness=2, lineType=cv2.LINE_AA
        )
