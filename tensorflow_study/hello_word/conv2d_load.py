#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import os
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x = tf.placeholder(tf.float32, [None, 28 * 28])
# ckpt = tf.train.latest_checkpoint('model2')

# reader = tf.train.NewCheckpointReader(ckpt)
# variables = reader.get_variable_to_shape_map()
# for ele in variables:
#     print(ele)

# mnist = input_data.read_data_sets('mnist_data', one_hot=True)
# saver = tf.train.import_meta_graph(ckpt + '.meta')
# with tf.Session() as sess:
#     saver.restore(sess, ckpt)
#     graph = tf.get_default_graph()
#     pred = graph.get_tensor_by_name('pred:0')
#     print(pred)
#     tes_img = mnist.test.images[:5, :]
#     print(tes_img[0].shape)
#     print(tes_img[0].ndim)
#     tes_lab = mnist.test.labels[:5, :]
#     for i in tes_lab:
#         print(i)
#     for i in tes_img:
#         x_image = sess.run(tf.reshape(i,[-1,784]))
#         tes_pred = sess.run(pred, feed_dict={x: x_image})
#         print(tes_pred)
