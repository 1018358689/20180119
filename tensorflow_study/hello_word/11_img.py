#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from PIL import Image
import os
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def check(img, threshold):
    x_s = 28
    y_s = 28
    num0 = 0
    num255 = 0
    pix_data = img.load()
    for x in range(x_s):
        for y in range(y_s):
            if pix_data[x, y] > threshold:
                num255 = num255 + 1
            else:
                num0 = num0 + 1
    return num255 > num0


def binarizing(img, threshold):  # 二值化
    pix_data = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pix_data[x, y] < threshold:
                pix_data[x, y] = 0
            else:
                pix_data[x, y] = 255
    return img


def img_convert(path, small=True):
    img = Image.open(path).convert('L')
    # img = binarizing(img, 255)
    if small:  # img.size[0] != 28 or img.size[1] != 28
        img = img.resize((28, 28), Image.ANTIALIAS)  # Image.ANTIALIAS
    # img = binarizing(img, 233)
    print('convert!')
    return img


# img = img_convert('./pic_test/test5.jpg',True)
# img.save('./pic_test/convert5.jpg')

ckpt = tf.train.latest_checkpoint('model3')
saver = tf.train.import_meta_graph(ckpt + '.meta')
with tf.Session() as sess:
    saver.restore(sess, ckpt)
    graph = tf.get_default_graph()
    x = graph.get_tensor_by_name('Placeholder/x:0')
    kp = graph.get_tensor_by_name('Placeholder/kp:0')
    pred = graph.get_tensor_by_name('CNN/fc2:0')
    # print(pred)
    tes_img = img_convert('./pic_test/test5.jpg', True)
    # tes_img.save('./pic_test/convert5.jpg')
    tes_img.show()
    # tes_img = np.reshape(tes_img,(28*28))
    tes_img = sess.run(tf.reshape(tes_img, [-1, 28 * 28]))
    # print(tes_img.shape)
    tes_img = np.array([1 - tes_img])
    # print(tes_img.shape)
    d2img = sess.run(tf.reshape(tes_img, [-1, 28 * 28]))

    pred_lab = sess.run(pred, feed_dict={x: d2img, kp: 1.0})
    pred_lab = sess.run(tf.reshape(pred_lab, [-1]))
    pred2index = sess.run(tf.argmax(pred_lab))
    # if not sess.run(tf.equal(label2index,pred2index)):
    #     print('[{}] [{}]'.format(label2index, pred2index))
    print(pred2index)
