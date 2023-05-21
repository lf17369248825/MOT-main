# -*- coding: utf-8 -*-
# @Author : CatfishW🚀
# @Time : 2023/5/1
import cv2


class Camera:
    def __init__(self, cam_preset_num=5):#cam_preset_num 相机预设数量
        self.cam_preset_num = cam_preset_num

    def get_cam_num(self):
        cnt = 0
        devices = []# device 为 0 代表内置摄像头  为 1 代表外接摄像头
        for device in range(0, self.cam_preset_num):
            stream = cv2.VideoCapture(device, cv2.CAP_DSHOW)# 获取摄像头给stream 
            grabbed = stream.grab()
            stream.release()#关闭摄像头
            if not grabbed:
                continue
            else:
                cnt = cnt + 1
                devices.append(device)
        return cnt, devices
    # def HIK_CamDriver(self):


if __name__ == '__main__':
    cam = Camera()
    cam_num, devices = cam.get_cam_num()
    print(cam_num, devices)
