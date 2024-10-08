# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'watermark.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import (QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QLineEdit,
                               QPushButton,
                               QVBoxLayout)

from videotrans.configure import config


class Ui_watermark(object):
    def setupUi(self, watermark):
        if not watermark.objectName():
            watermark.setObjectName(u"watermark")
        watermark.resize(643, 350)
        watermark.setWindowModality(QtCore.Qt.NonModal)

        self.videourls = []

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(watermark.sizePolicy().hasHeightForWidth())
        watermark.setSizePolicy(sizePolicy)
        watermark.setMaximumSize(QtCore.QSize(643, 350))

        self.horizontalLayout_3 = QHBoxLayout(watermark)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.videourl = QLineEdit(watermark)
        self.videourl.setObjectName(u"videourl")
        self.videourl.setMinimumSize(QSize(0, 35))

        self.videourl.setReadOnly(True)

        self.horizontalLayout.addWidget(self.videourl)

        self.videobtn = QPushButton(watermark)
        self.videobtn.setObjectName(u"videobtn")
        self.videobtn.setMinimumSize(QSize(180, 35))
        self.videobtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.videobtn.setMouseTracking(False)

        self.horizontalLayout.addWidget(self.videobtn)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pngurl = QLineEdit(watermark)
        self.pngurl.setObjectName(u"pngurl")
        self.pngurl.setMinimumSize(QSize(0, 35))
        self.pngurl.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.pngurl)

        self.pngbtn = QPushButton(watermark)
        self.pngbtn.setObjectName(u"pngbtn")
        self.pngbtn.setMinimumSize(QSize(180, 35))
        self.pngbtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.pngbtn)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        pos = QtWidgets.QHBoxLayout()
        self.labelpos = QtWidgets.QLabel()
        self.compos = QtWidgets.QComboBox()
        self.compos.addItems([
                                 "左上角",
                                 "右上角",
                                 "右下角",
                                 "左下角",
                                 "居 中"
                             ] if config.defaulelang == 'zh' else [
            "Upper left",
            "Upper right",
            "Bottom right",
            "Bottom left",
            "Center"
        ])
        pos.addWidget(self.labelpos)
        pos.addWidget(self.compos)
        self.verticalLayout.addLayout(pos)

        tmpx = QtWidgets.QHBoxLayout()
        self.labelx = QtWidgets.QLabel()
        self.linex = QtWidgets.QLineEdit()
        tmpx.addWidget(self.labelx)
        tmpx.addWidget(self.linex)

        tmpy = QtWidgets.QHBoxLayout()
        self.labely = QtWidgets.QLabel()
        self.liney = QtWidgets.QLineEdit()
        tmpy.addWidget(self.labely)
        tmpy.addWidget(self.liney)

        tmpw = QtWidgets.QHBoxLayout()
        self.labelw = QtWidgets.QLabel()
        self.linew = QtWidgets.QLineEdit()
        tmpw.addWidget(self.labelw)
        tmpw.addWidget(self.linew)

        self.startbtn = QPushButton(watermark)
        self.startbtn.setObjectName(u"startbtn")
        self.startbtn.setMinimumSize(QSize(0, 35))
        self.startbtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addLayout(tmpx)
        self.verticalLayout.addLayout(tmpy)
        self.verticalLayout.addLayout(tmpw)
        self.verticalLayout.addWidget(self.startbtn)

        self.resultlabel = QLabel(watermark)
        self.resultlabel.setObjectName(u"resultlabel")

        self.verticalLayout.addWidget(self.resultlabel)

        self.resultbtn = QPushButton(watermark)
        self.resultbtn.setObjectName(u"resultbtn")
        self.resultbtn.setStyleSheet("background-color:transparent")
        self.resultbtn.setMinimumSize(QSize(0, 30))
        self.resultbtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.resultbtn)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(watermark)

        QMetaObject.connectSlotsByName(watermark)

    def retranslateUi(self, watermark):
        watermark.setWindowTitle("批量视频添加图片水印" if config.defaulelang == 'zh' else 'Adding image watermark to videos')
        self.videourl.setPlaceholderText(
            "选择视频1或多个" if config.defaulelang == 'zh' else 'Select  Videos')

        self.pngurl.setPlaceholderText("选择水印图片" if config.defaulelang == 'zh' else 'Select a watermark image')
        self.videobtn.setText("选择视频" if config.defaulelang == 'zh' else 'Select a Video')
        self.pngbtn.setText("选择水印图" if config.defaulelang == 'zh' else 'Select an Image')
        self.startbtn.setText("开始执行" if config.defaulelang == 'zh' else 'Start operating')
        self.resultlabel.setText("")
        self.resultbtn.setText("打开保存结果目录" if config.defaulelang == 'zh' else 'Open the save results directory')

        self.labelx.setText(
            '水印距离左侧/右侧距离' if config.defaulelang == 'zh' else 'Distance of watermark from left or right side')
        self.labely.setText(
            '水印距离顶部/底部的距离' if config.defaulelang == 'zh' else 'Distance of watermark from top or bottom')

        self.labelw.setText('水印图宽度x高度' if config.defaulelang == 'zh' else 'Watermark width x height')
        self.linew.setText('50x50')
        self.labelpos.setText('水印位置' if config.defaulelang == 'zh' else 'Watermark Location')

        self.linex.setText('10')
        self.liney.setText('10')
