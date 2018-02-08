#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tensorflow as tf

# our NN's output
logits = tf.constant([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0]])
# step1:do softmax
y = tf.nn.softmax(logits)
# true label
y_ = tf.constant([[1.0, 3.0, 1.0], [2.0, 3.0, 1.0], [4.0, 3.0, 1.0]])
# step2:do cross_entropy
cross_entropy = tf.reduce_mean(tf.reduce_sum(-y_ * tf.log(y), 1))
cross_entropy_value = -y_ * tf.log(y)
# do cross_entropy just one step
cross_entropy2 = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits, labels=y_))  # dont forget tf.reduce_sum()!!
cross_entropy2_value = tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits,
                                                                  labels=y_)  # dont forget tf.reduce_sum()!!

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    l1 = sess.run(logits)
    y_softmax = sess.run(y)
    label = sess.run(y_)
    print(l1)
    print(y_softmax)
    print(label)
    c1 = sess.run(cross_entropy)
    c2 = sess.run(cross_entropy2)
    c1_value = sess.run(cross_entropy_value)
    c2_value = sess.run(cross_entropy2_value)
    print(c1_value)
    print(c1)
    print(c2_value)
    print(c2)
