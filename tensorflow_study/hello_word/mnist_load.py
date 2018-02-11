#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# reader = tf.train.NewCheckpointReader("./model1/model.ckpt-20000")
# variables = reader.get_variable_to_shape_map()
# a = reader.get_tensor()
# for ele in variables:
#     print(ele)

'''
hidden/biases
hidden/weights
out/weights
out/biases
'''
# saver = tf.train.import_meta_graph('./model1/model.ckpt-20000.meta')
# with tf.Session() as sess:
#     saver.restore(sess,'./model1/model.ckpt-20000')
#     graph = tf.get_default_graph()
#     # print(sess.run(graph.get_tensor_by_name('hidden/biases:0')))
#     network = graph.get_tensor_by_name('network:0')
#     print(network)
ckpt = tf.train.get_checkpoint_state('model4')
# a = ckpt.model_checkpoint_path
print(ckpt)
# print(a)