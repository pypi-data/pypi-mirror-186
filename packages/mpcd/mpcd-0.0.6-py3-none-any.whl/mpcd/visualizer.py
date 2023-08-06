import cv2
import numpy as np
from PIL import Image
from math import *
import os

class PointCloudVisualizer:
    def __init__(
        self,
        height=2400,
        width=1200,
        scale=10,
        world_trans=[0, 0, 0],
    ):
        self._set_canvas(
            height=height, width=width, scale=scale, world_trans=world_trans
        )

        self.FONT = cv2.FONT_HERSHEY_PLAIN
        self.color_dic = {
            "GT": [255, 255, 255],
            "FP": {
                "HIGH": [0, 0, 255],
                "MID": [144, 32, 208],
                "LOW": [203, 192, 255],
            },
            "FN": [0, 255, 255],
            "TP": [0, 255, 0],
            "FTP": [0, 255, 0],  # force tp
            "STP": [238, 229, 0],  # soft tp
            "DET": {
                "LOW": [205, 205, 150],
                # 'MID': [0,255,0],
                "HIGH": [0, 255, 0],
                "MID": [124, 205, 124],
            },
            "red": [255, 0, 0],
            "green": [0, 255, 0],
            "blue": [0, 0, 255],
            "yellow": [255, 255, 0],
            "purple": [255, 0, 255],
            "cyan": [0, 255, 255],
            "white": [255, 255, 255],
            "black": [0, 0, 0],
            "gray": [128, 128, 128],
        }

    def _maybe_tensor2numpy(self, data):
        if isinstance(data, torch.Tensor):
            data = data.detach().cpu().numpy()
        return data

    def _set_canvas(self, height=2000, width=1000, scale=10, world_trans=[0, 0, 0]):
        self.IM_H = height
        self.IM_W = width
        self.SCALE = scale
        self.WORLD_TRANS = world_trans
        self.IMAGE_TRANS = [self.IM_W / 2, self.IM_H / 2]

    def _init_image(self):
        image = np.zeros((self.IM_H, self.IM_W, 3), np.uint8)
        return image

    def transfer_coor(self, pt):
        pt_trans = (np.array(pt) + np.array(self.WORLD_TRANS)) * self.SCALE
        pt_trans[0] = np.clip(-pt_trans[0] + self.IMAGE_TRANS[1], 0, self.IM_H)
        pt_trans[1] = np.clip(-pt_trans[1] + self.IMAGE_TRANS[0], 0, self.IM_W)
        return pt_trans.astype(np.int32)

    def transfer_coors(self, pts):
        pts_trans = np.array([self.transfer_coor(x) for x in pts])
        return pts_trans.astype(np.int32)

    def draw_pcloud(self, pcloud, color="gray", r=0, draw_distance_marker=True, draw_orin=False):
        """
        draw point cloud on image
        Args:
        image: [H, W, 3]
        pcloud: [N, 4] ndarray
        """
        image = self._init_image()

        for pt in pcloud:
            pt_draw = self.transfer_coor([pt[0], pt[1], 0])
            if (
                pt_draw[0] >= 0
                and pt_draw[0] < self.IM_H
                and pt_draw[1] >= 0
                and pt_draw[1] < self.IM_W
            ):
                image[
                    pt_draw[0] - r : pt_draw[0] + r + 1,
                    pt_draw[1] - r : pt_draw[1] + r + 1,
                ] = self.color_dic[color]
        if draw_distance_marker:
            self.draw_distance_marker(image)
        if draw_orin:
            pass
            #self.draw_orin(image)
        return image



    def draw_pcloud_fast(self, pcloud, color="gray", r=0, draw_distance_marker=True, draw_orin=False):
        """
        draw point cloud on image
        Args:
        image: [H, W, 3]
        pcloud: [N, 4] ndarray
        """
        image = self._init_image()

        xy = pcloud[:, :2]

        for pt in pcloud:
            pt_draw = self.transfer_coor([pt[0], pt[1], 0])
            if (
                pt_draw[0] >= 0
                and pt_draw[0] < self.IM_H
                and pt_draw[1] >= 0
                and pt_draw[1] < self.IM_W
            ):
                image[
                    pt_draw[0] - r : pt_draw[0] + r + 1,
                    pt_draw[1] - r : pt_draw[1] + r + 1,
                ] = self.color_dic[color]
        if draw_distance_marker:
            self.draw_distance_marker(image)
        if draw_orin:
            pass
            #self.draw_orin(image)
        return image



    def draw_pc_overlay(self, pc_tuple, draw_distance_marker=True):
        """
        draw multiple point cloud class on image
        Args:
        image: [H, W, 3]
        pcloud: [N, 4] ndarray

        """
        image = self._init_image()
        for pcloud_color in pc_tuple:
            pcloud, color, r = pcloud_color
            for pt in pcloud.pc_data:
                pt_draw = self.transfer_coor([pt["x"], pt["y"], 0])
                if (
                    pt_draw[0] >= 0
                    and pt_draw[0] < self.IM_H
                    and pt_draw[1] >= 0
                    and pt_draw[1] < self.IM_W
                ):
                    image[
                        pt_draw[0] - r : pt_draw[0] + r + 1,
                        pt_draw[1] - r : pt_draw[1] + r + 1,
                    ] = self.color_dic[color]
        if draw_distance_marker:
            self.draw_distance_marker(image)
        return image

    def draw_orin(self):
        pass

    def draw_distance_marker(self, image, ranges_value=None):
        if not ranges_value:
            ranges_value = [40, 80, 120, 160, 200]
        color = (255, 255, 255)
        thickness = 1
        center_coordinates = tuple([int(self.IMAGE_TRANS[0]), int(self.IMAGE_TRANS[1])])

        for range_value in ranges_value:
            radius = int(range_value * self.SCALE)
            cv2.circle(image, center_coordinates, radius, color, thickness)

    def img_save(self, image, save_path, auto_rot=True):
        if auto_rot and image.shape[0] > image.shape[1]:
            img = np.rot90(image, -1)
        else:
            img = image
        path = os.path.join(save_path)
        img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cv2.imwrite(path, img_bgr)

    def draw_bbox(self, image, obj_corners, color=(255, 255, 255), line=1):
        b = obj_corners[:8].reshape([-1, 2])
        scor = obj_corners[-2] if obj_corners.shape[0] > 8 else 1.0
        clas = obj_corners[-1] if obj_corners.shape[0] > 8 else -1
        for k in range(0, 4):
            i, j = k, (k + 1) % 4
            pt0 = self.transfer_coor([b[i, 0], b[i, 1], 0])
            pt1 = self.transfer_coor([b[j, 0], b[j, 1], 0])
            cv2.line(image, (pt0[1], pt0[0]), (pt1[1], pt1[0]), color, line)

    def draw_cicle(self, image, obj, color=(0, 0, 255), r=4):
        center = obj[:3]
        pt = self.transfer_coor([center[0], center[1], 0])
        cv2.circle(image, (pt[1], pt[0]), r, color, -1)

    def draw_orientation(self, image, obj, color=(0, 255, 255)):
        center = obj[:3]
        theta = obj[6]
        vec = np.array([cos(theta), sin(theta), 0]) * obj[3]
        orientation = center + vec
        pt0 = self.transfer_coor([center[0], center[1], 0])
        pt1 = self.transfer_coor([orientation[0], orientation[1], 0])
        cv2.line(image, (pt0[1], pt0[0]), (pt1[1], pt1[0]), color, 1)

    def img_show(self, image, auto_rot=True):
        if auto_rot and image.shape[0] > image.shape[1]:
            img = np.rot90(image, -1)
        else:
            img = image
        img = Image.fromarray(img)
        img.show()

    def draw_str(self, image, center, class_name, color=(255, 255, 255)):
        pt0 = self.transfer_coor([center[0], center[1], 0])
        cv2.putText(
            image,
            class_name,
            (pt0[1] + 10 + 10, pt0[0] + 10),
            self.FONT,
            0.8,
            color,
            1,
            cv2.LINE_AA,
        )

    def draw_arrow(self, image, pixes1, pixes2, color=(0, 155, 155)):
        pixes1 = self._maybe_tensor2numpy(pixes1)
        pixes2 = self._maybe_tensor2numpy(pixes2)
        for pt1, pt2 in zip(pixes1, pixes2):
            pt1 = self.transfer_coor([pt1[0], pt1[1], 0])
            pt2 = self.transfer_coor([pt2[0], pt2[1], 0])
            cv2.arrowedLine(
                image,
                (int(pt1[1]), int(pt1[0])),
                (int(pt2[1]), int(pt2[0])),
                color,
                thickness=1,
                line_type=cv2.LINE_4,
                shift=0,
                tipLength=0.1,
            )
        return image
