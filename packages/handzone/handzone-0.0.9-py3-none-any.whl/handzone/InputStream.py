import glob
import os

import cv2


class WebCamera:
    def __init__(self, index=0):
        self.cap = cv2.VideoCapture(index)

    def get_frame(self):
        ret, frame = self.cap.read()
        return ret, frame

    def get_fps_size_len(self):
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        size = (
            int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        )
        length = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        return (fps, size, length)

    def isOpened(self):
        if self.cap.isOpened:
            return True
        else:
            return False

    def stop(self):
        self.cap.release()


class LoadImgData:
    def __init__(self, path=None, img_root=None):
        self.frame_index = 0
        self.frame_num = 0
        if os.path.isdir(path):
            self.img_path_list = sorted(glob.glob(os.path.join(path, "*.jpg")))
        else:
            self.img_path_list = [
                line.split()[0] for line in open(path, "r").readlines()
            ]
            if img_root:
                self.img_path_list = [
                    os.path.join(img_root, p) for p in self.img_path_list
                ]
        self.frame_num = len(self.img_path_list)

    def isOpened(self):
        if self.frame_index <= self.frame_num - 1:
            return True
        else:
            return False

    def get_frame(self):
        img_path = self.img_path_list[self.frame_index]
        frame = cv2.imread(img_path)
        # self.frame_index = min(self.frame_index + 1, self.frame_num - 1)
        self.frame_index = self.frame_index + 1
        if self.frame_index <= self.frame_num - 1:
            success = True
        else:
            success = False
        return success, frame, img_path

    def stop(self):
        exit(1)
