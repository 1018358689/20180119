#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

matrix1 = tf.constant([[3.,3.]])
matrix2 = tf.constant([[2.],[2.]])
product = tf.matmul(matrix1,matrix2)

inpu1 = tf.placeholder(tf.float32)
inpu2 = tf.placeholder(tf.float32)
output = tf.multiply(inpu1,inpu2)
# print(product)

sess = tf.Session()
result1 = sess.run(product)
result2 = sess.run(output, feed_dict={inpu1:[[3.,3.]], inpu2:[[2.],[2,]]})
print(result2)
sess.close()