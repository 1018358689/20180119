#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Part1: 通过tf.train.Saver类实现保存和载入神经网络模型
# c1 = tf.Variable(tf.constant(1.0, tf.float32, [1, 2]), name='c1')
# c2 = tf.Variable(tf.constant(2.0, tf.float32, [2, 2]), name='c2')
# c3 = tf.matmul(c1, c2, name='c3')
# saver = tf.train.Saver()
# init = tf.global_variables_initializer()
# with tf.Session() as sess:
#     sess.run(init)
#     saver.save(sess, './Model_test/model.ckpt')

# Part2: 加载TensorFlow模型的方法
# c1 = tf.Variable(tf.constant(1.0, tf.float32, [1, 2]), name='c1')
# c2 = tf.Variable(tf.constant(2.0, tf.float32, [2, 2]), name='c2')
# c3 = tf.matmul(c1, c2, name='c3')
# saver = tf.train.Saver()
# with tf.Session() as sess:
#     saver.restore(sess, "./Model_test/model.ckpt")  # 注意此处路径前添加"./"
#     print(sess.run(c3))  # [[4. 4.]]

# Part3: 若不希望重复定义计算图上的运算，可直接加载已经持久化的图
saver = tf.train.import_meta_graph('./Model_test/model.ckpt.meta')
with tf.Session() as sess:
    # saver.restore(sess,'./Model_test/model.ckpt')
    saver.restore(sess,tf.train.latest_checkpoint('./Model_test'))
    print(sess.run(tf.get_default_graph().get_tensor_by_name('c3:0')))

# Part4： tf.train.Saver类也支持在保存和加载时给变量重命名
# u1 = tf.Variable(tf.constant(1.0, tf.float32, [1, 2]),name='u1')
# u2 = tf.Variable(tf.constant(2.0, tf.float32, [2, 2]),name='u2')
# c3 = tf.matmul(u1, u2, name='c3')
# # 若直接生命Saver类对象，会报错变量找不到
# # 使用一个字典dict重命名变量即可，{"已保存的变量的名称name": 重命名变量名}
# # 原来名称name为c3的变量现在加载到变量u1（名称name为c3）中
# saver = tf.train.Saver({'c1': u1, 'c2': u2,})
# with tf.Session() as sess:
#     saver.restore(sess, './Model_test/model.ckpt')
#     print(sess.run(c3))

# 读取变量
# reader = tf.train.NewCheckpointReader("./Model_test/model.ckpt")
# variables = reader.get_variable_to_shape_map()
# for ele in variables:
#     print(ele)
