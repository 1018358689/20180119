#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

ckpt = tf.train.latest_checkpoint('model3')
# reader = tf.train.NewCheckpointReader(ckpt)
# variables = reader.get_variable_to_shape_map()
# for ele in variables:
#     print(ele)
'''
Train/global_step
CNN/w_c2
CNN/w_f1
CNN/b_c1
CNN/b_f2
CNN/w_c1
CNN/w_f2
CNN/b_c2
CNN/b_f1
'''
# saver = tf.train.import_meta_graph(ckpt+'.meta')
# with tf.Session() as sess:
#     saver.restore(sess,ckpt)
#     graph = tf.get_default_graph()
#     for op in graph.get_operations():
#         print(op.name) # op.name, op.values()


mnist = input_data.read_data_sets('mnist_data', one_hot=True)
saver = tf.train.import_meta_graph(ckpt+'.meta')
with tf.Session() as sess:
    saver.restore(sess,ckpt)
    graph = tf.get_default_graph()
    x = graph.get_tensor_by_name('Placeholder/x:0')
    kp = graph.get_tensor_by_name('Placeholder/kp:0')
    pred = graph.get_tensor_by_name('CNN/fc2:0')
    # print(pred)
    tes_img = mnist.test.images[:1, :]
    tes_lab = mnist.test.labels[:1, :]
    for i in range(len(tes_img)):
        label2index = sess.run(tf.argmax(tes_lab[i]))
        d2img = sess.run(tf.reshape(tes_img[i], [-1, 28 * 28]))
        pred_lab = sess.run(pred, feed_dict={x: d2img, kp: 1.0})
        pred_lab = sess.run(tf.reshape(pred_lab, [-1]))
        pred2index = sess.run(tf.argmax(pred_lab))
        # if not sess.run(tf.equal(label2index,pred2index)):
        #     print('[{}] [{}]'.format(label2index, pred2index))
        print('[{}] [{}]'.format(label2index, pred2index))