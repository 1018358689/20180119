#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tensorflow as tf


class CNN_model:
    def __init__(self):
        self.learning_rate = 0.01
        self.x = tf.placeholder(dtype=tf.float32, shape=[None, 28 * 28])
        self.y = tf.placeholder(dtype=tf.float32, shape=[None, 10])
        self.kp = tf.placeholder(tf.float32)
        self.w = {
            'conv1': tf.Variable(tf.truncated_normal(shape=[5, 5, 1, 32], stddev=0.1), name='w_c1'),
            'conv2': tf.Variable(tf.truncated_normal(shape=[5, 5, 32, 64], stddev=0.1), name='w_c2'),
            'fc1': tf.Variable(tf.truncated_normal(shape=[7 * 7 * 64, 1024], stddev=0.1), name='w_f1'),
            'fc2': tf.Variable(tf.truncated_normal(shape=[1024, 10], stddev=0.1), name='w_f2'),
        }
        self.b = {
            'conv1': tf.Variable(tf.constant(0.1, shape=[32]), name='b_c1'),
            'conv2': tf.Variable(tf.constant(0.1, shape=[64]), name='b_c2'),
            'fc1': tf.Variable(tf.constant(0.1, shape=[1024]), name='b_f1'),
            'fc2': tf.Variable(tf.constant(0.1, shape=[10]), name='b_f2'),
        }

        self.pred = self.network()
        self.loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=self.pred, labels=self.y))
        self.train = tf.train.GradientDescentOptimizer(self.learning_rate).minimize(self.loss)
        self.correct_pred = tf.equal(tf.argmax(self.pred, 1), tf.argmax(self.y, 1))
        self.accuracy = tf.reduce_mean(tf.cast(self.correct_pred, tf.float32))

    def __conv2d(self, x, w):
        return tf.nn.conv2d(
            input=x,  # 输入的图片参数：[batch张图片, 每张图片高度为in_height, 每张图片宽度为in_width, 图像通道为in_channels]
            filter=w,  # 滤波器：[滤波器高度, 滤波器宽度, 接受图像的通道数, 卷积后通道数]
            strides=[1, 1, 1, 1],  # 步长：每跨多少步抽取信息，strides[1, x_movement,y_movement, 1]， strides[0]和[3]必须为1
            padding='SAME',  # 边距处理：“SAME”表示输出图层和输入图层大小保持不变？，设置为“VALID”时表示舍弃多余边距(丢失信息)
        )

    def __max_pool_2x2(self, x):
        return tf.nn.max_pool(
            value=x,
            ksize=[1, 2, 2, 1],
            strides=[1, 2, 2, 1],
            padding='SAME',
        )

    def network(self):
        x_image = tf.reshape(self.x, [-1, 28, 28, 1])
        h_conv1 = tf.nn.relu(self.__conv2d(x_image, self.w['conv1']) + self.b['conv1'])
        h_pool1 = self.__max_pool_2x2(h_conv1)

        h_conv2 = tf.nn.relu(self.__conv2d(h_pool1, self.w['conv2']) + self.b['conv2'])
        h_pool2 = self.__max_pool_2x2(h_conv2)

        h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
        h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, self.w['fc1']) + self.b['fc1'])
        h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob=self.kp)

        h_fc2 = tf.matmul(h_fc1_drop, self.w['fc2']) + self.b['fc2']
        return h_fc2

