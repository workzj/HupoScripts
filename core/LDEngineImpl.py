# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     HupoEngine
   Description :   任务基类，提供：
                        1、DB 操作接口
                        2、代理服务器

   Author :        zj
   date：          2023/3/10
-------------------------------------------------
"""
__author__ = 'ZJ'

import os
import sys
from datetime import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class LDEngineImpl(object):
    """
    LDEngineImpl LD虚拟机实行类

    抽象方法定义：
        init(): 初始化函数;

        touchAtPoint
        touchAt
        inputText
        mouseDrag
        matchImage
        matchImageRoi
        matchImageMulti
        matchAndTouch
        SaveImage
        RunCommand
        FindColorBlock
        FindColorBlockMulti


        所有方法需要相应类去具体实现：
            ld: HupoLDPlayerEngine.py
    """

    def __init__(self):
        pass

    def __del__(self):
        pass

    def touchAtPoint(self, point, offset=(0, 0)):
        """
        触屏单击
        :param point: 坐标（X,Y）
        :param offset: 偏移（X,Y）
        """
        return self.impl.touchAtPoint(point, offset)

    def touchAt(self, x, y, offset=(0, 0)):
        """
        文字输入
        :param offset: 偏移
        :param y:
        :param x:
        """
        return self.impl.touchAtPoint(x, y, offset)

    def inputText(self, text):
        """
        文字输入
        :param text:
        """
        return self.impl.inputText(text)

    def mouseDrag(self, x, y, step):
        """
        鼠标拖拽
        :param x: 起始坐标
        :param y:
        :param step: 上下步长
        """
        return self.impl.mouseDrag(x, y, step)

    def matchImage(self, match_img, roi=None, threshold=80):
        """
        图像匹配
        :param threshold: 临界度
        :param roi:  搜索区域
        :param match_img: 匹配图片
        """
        return self.impl.matchImage(match_img, roi, threshold)

    def matchImageMulti(self, match_img, roi=None, threshold=80):
        """
        图像匹配多个结果
        :param threshold: 临界度
        :param roi:  搜索区域
        :param match_img: 匹配图片
        """
        return self.impl.matchImageMulti(match_img, roi, threshold)

    def matchAndTouch(self, match_img, roi=None, threshold=80, offset=(0,0)):
        """
        找图 并 点击
        :param offset:
        :param threshold: 临界度
        :param roi:  搜索区域
        :param match_img: 匹配图片
        """
        return self.impl.matchAndTouch(match_img, roi, threshold, offset)

    def SaveImage(self, img='./log/{}.jpg'.format(time.strftime('%Y-%m-%d-%H-%M-%S'))):
        """
        保存图片
        :param img:
        """
        return self.impl.SaveImage(img)

    def RunCommand(self, cmd):
        """
        运行命令行
        :param cmd:
        """
        return self.impl.RunCommand(cmd)
