"""
Anaconda_101219148_zhousheng_image.py
Digital Signal Processing
Image Programs
Winter 2021
@ Shanghai University of Engineering Science (SUES)

"""

import numpy as np
from skimage import io,img_as_float,transform
import matplotlib.pyplot as plt #使用plt绘制圆形

"""

本代码受蒋老师原代码启发，在尽量不改变原代码功能的情况下
通过将数组遍历改成切片或者使用现有函数进行改写
将图像处理的所需时间减少，原3000*4000图像处理时间从大约2分钟缩短至约10秒。
圆形处理功能还是使用遍历为好，这里使用其他方法实则是强行变换并不好。

"""

def main():
    
    photoName = "./pic1.jpg"
    
    photoConstruction(photoName)
    
    photoBlue(photoName)
    
    photoCircle(photoName)
    
    photoRotate(photoName)
    
    photoName2 = "./pic2.jpg"
    
    photoCombine(photoName, photoName2)

def photoConstruction(photoName) :#输出参数

    myPhoto = io.imread(photoName)  
    rowNum, columnNum, colorNum = myPhoto.shape
    print("rowNum = ",rowNum)
    print("columnNum = ",columnNum)
    print("colorNum = ",colorNum)

def photoBlue(photoName):  #变蓝

    myPhoto = io.imread(photoName) 
    myPhoto=img_as_float(myPhoto)#原图像为整型，无法直接处理，需要改为浮点型
    myPhoto[:,:,0] *= 0.7
    myPhoto[:,:,1] *= 0.7
    '''myPhoto[rowIdx,columnIdx,2] is not changed.'''        
    io.imsave("./pic1_1blue.jpg",myPhoto)
    
def photoCircle(photoName):  #画圆
    myPhoto = plt.imread(photoName)
    rowNum, columnNum, colorNum = myPhoto.shape
    squareNum = min(rowNum, columnNum)
    circlePhoto = np.zeros((squareNum,squareNum,3),dtype="uint8")
    circleCenter = np.int(squareNum/2)
    radius = circleCenter
    circlePhoto=myPhoto[:squareNum,:squareNum,:]
    i=0
    while(i<=2000): #从图片中心出画足够密度的中心圆
        plt.scatter(circleCenter,circleCenter,color='None',
                    edgecolors='w',s=31*(radius+i),marker='o')
        i=i+10
    plt.imshow(circlePhoto)  # 显示图片
    plt.savefig("./pic1_2Circle.jpg",dpi=750)
    #裁切plt生成区域
    circlePhoto1 = io.imread("./pic1_2Circle.jpg")
    io.imshow(circlePhoto1)
    circlePhoto1=circlePhoto1[392:2588,1207:3400,:]
    io.imsave("./pic1_2Circle.jpg",circlePhoto1)


"""

def photoCircle(photoName):  

    myPhoto = io.imread(photoName)
    rowNum, columnNum, colorNum = myPhoto.shape
    squareNum = min(rowNum, columnNum)
    circlePhoto = np.zeros((squareNum,squareNum,3),dtype="uint8")
    circleCenter = np.int(squareNum/2)
    radius = circleCenter
    circlePhoto=myPhoto[:squareNum,:squareNum,:]
    i=0
    while(i<=700):
        rr, cc=draw.circle_perimeter(circleCenter,circleCenter,radius+i)
        draw.set_color(circlePhoto,[rr,cc],[255,255,255])
        i+=1
    io.imshow(circlePhoto)
    io.imsave("./pic1_2circle.jpg",circlePhoto)    


def photoCircle(photoName):    
    myPhoto = io.imread(photoName)
    rowNum, columnNum, colorNum = myPhoto.shape
    squareNum = min(rowNum, columnNum)
    circlePhoto = np.zeros((squareNum,squareNum,3),dtype="uint8")
    circleCenter = np.int(squareNum/2)
    radius = circleCenter
    for rowIdx in np.arange(0,squareNum,1):
        for columnIdx in np.arange(0,squareNum,1):
            if ( (rowIdx    - circleCenter)**2
                +(columnIdx - circleCenter)**2
                < radius**2 ):
                    circlePhoto[rowIdx,columnIdx,:]=myPhoto[rowIdx,columnIdx,:]
            else:
                    circlePhoto[rowIdx,columnIdx,:]=255

    io.imsave("./pic1_2circle.jpg",circlePhoto)    

"""

def photoRotate(photoName):#旋转

    myPhoto = io.imread(photoName)
    #调用rotate函数，第二个参数为旋转角度
    rotatePhoto=transform.rotate(myPhoto, 45,resize=False)
    io.imsave("./pic1_3rotate.jpg",rotatePhoto)

def photoCombine(photoName, photoName2):  #合并

    myPhoto1 = io.imread(photoName)
    rowNum1, columnNum1, colorNum1 = myPhoto1.shape
    myPhoto2 = io.imread(photoName2)
    rowNum2, columnNum2, colorNum2 = myPhoto2.shape    
    combinedRowNum = min(rowNum1, rowNum2)
    combinedColumnNum = columnNum1 + columnNum2
    combinedPhoto = np.zeros((combinedRowNum,combinedColumnNum,3),
                              dtype="uint8")
    #将myPhoto1全部赋予到combinedPhoto的 0至combinedRowNum，0至columnNum1
    combinedPhoto[:combinedRowNum,:columnNum1,:]= myPhoto1
    #将myPhoto2裁切至与myPhoto1 row相同
    myPhoto2=myPhoto2[:rowNum1,:,:]
    #将裁切后的myPhoto2全部赋予到combinedPhoto的0至combinedRowNum，columnNum1至combinedColumnNum
    combinedPhoto[:combinedRowNum,columnNum1:combinedColumnNum,:]= myPhoto2   
    io.imsave("./pic1_4combined.jpg",combinedPhoto)    
    
main()