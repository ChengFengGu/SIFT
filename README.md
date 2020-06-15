From : [简书：OpenCV-Python 图像SIFT特征提取](https://www.jianshu.com/p/65a56a2f63e3)

---

这个代码只能在windows下运行

代码依赖:python 3.6

pip list:

```

asn1crypto             1.3.0
astroid                2.3.3
certifi                2019.11.28
cffi                   1.14.0
chardet                3.0.4
colorama               0.4.3
conda                  4.8.2
conda-package-handling 1.6.0
cryptography           2.8
idna                   2.8
isort                  4.3.21
lazy-object-proxy      1.4.3
mccabe                 0.6.1
menuinst               1.4.16
pip                    20.0.2
pycosat                0.6.3
pycparser              2.19
pylint                 2.4.4
pyOpenSSL              19.1.0
PySocks                1.7.1
pywin32                227
requests               2.22.0
ruamel-yaml            0.15.87
setuptools             45.2.0.post20200210
six                    1.14.0
tqdm                   4.42.1
typed-ast              1.4.1
urllib3                1.25.8
wheel                  0.34.2
win-inet-pton          1.1.0
wincertstore           0.2
wrapt                  1.11.2
psd-tools              1.9.13

```



其中sift.detectAndCompute()函数返回kp，des。



kp存储的特征点信息:
---

- angle：角度，表示关键点的方向，通过Lowe大神的论文可以知道，为了保证方向不变形，SIFT算法通过对关键点周围邻域进行梯度运算，求得该点方向。-1为初值。
- class_id：当要对图片进行分类时，我们可以用class_id对每个特征点进行区分，未设定时为-1，需要靠自己设定。
- octave：代表是从金字塔哪一层提取的得到的数据。
- pt：关键点点的坐标。
- response：响应程度，代表该点强壮大小，更确切的说，是该点角点的程度。
- size：该点直径的大小

des为特征向量
---

上图dog的shape为(481, 500, 3)，提取的特征向量des的shape为(501, 128)，501个128维的特征点.


cv2.drawKeyPoints(image, keypoints, outImage, color, flags)
---
该方法可以在特征点处绘制一个小圆圈。

- image：输入图像，可以使三通道或单通道图像。
- keypoints：特征点向量，向量内每一个元素是一个KeyPoint对象，包含了特征点的各种属性信息。
- outImage：特征点绘制的画布图像，可以是原图像。
绘制的特征点的颜色信息，默认绘制的是随机彩色。
- flags：特征点的绘制模式，其实就是设置特征点的哪些信息需要绘制，哪些不需要绘制，有以下几种模式可选：

    - cv2.DRAW_MATCHES_FLAGS_DEFAULT： 只绘制特征点的坐标点,显示在图像上就是一个个小圆点,每个小圆点的圆心坐标都是特征点的坐标。
    
    - cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS：绘制特征点的时候绘制的是一个个带有方向的圆,这种方法同时显示图像的坐标，size和方向，是最能显示特征的一种绘制方式 。
    
    - cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG:函数不创建输出的图像，而是直接在输出图像变量空间绘制，要求本身输出图像变量就是一个初始化好了的，size与type都是已经初始化好的变量。
    
    - cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS: 单点的特征点不被绘制 

