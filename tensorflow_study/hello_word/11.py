#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import time
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 定义超参数
batch_size = 50  # 一批输入的数据个数
learning_rate = 0.01  # 学习速率：梯度下降的幅度
iteration = 30000  # 迭代训练次数
display_step = 500  # 打印的布次

# global_step = tf.Variable(0, trainable=False, name='global_step')

with tf.variable_scope('Placeholder'):
    x = tf.placeholder(tf.float32, [None, 28 * 28], 'x')
    y = tf.placeholder(tf.float32, [None, 10], 'y')
    kp = tf.placeholder(tf.float32, [], name='kp')


def conv2d(x, w):
    return tf.nn.conv2d(x, w, [1, 1, 1, 1], 'SAME')


def max_pool_2x2(x):
    return tf.nn.max_pool(x, [1, 2, 2, 1], [1, 2, 2, 1], 'SAME')


with tf.variable_scope('CNN'):
    w_c1 = tf.get_variable('w_c1', [5, 5, 1, 32], initializer=tf.truncated_normal_initializer(stddev=0.1))
    w_c2 = tf.get_variable('w_c2', [5, 5, 32, 64], initializer=tf.truncated_normal_initializer(stddev=0.1))
    w_f1 = tf.get_variable('w_f1', [7 * 7 * 64, 1024], initializer=tf.truncated_normal_initializer(stddev=0.1))
    w_f2 = tf.get_variable('w_f2', [1024, 10], initializer=tf.truncated_normal_initializer(stddev=0.1))
    b_c1 = tf.get_variable('b_c1', [32], initializer=tf.constant_initializer(0.1))
    b_c2 = tf.get_variable('b_c2', [64], initializer=tf.constant_initializer(0.1))
    b_f1 = tf.get_variable('b_f1', [1024], initializer=tf.constant_initializer(0.1))
    b_f2 = tf.get_variable('b_f2', [10], initializer=tf.constant_initializer(0.1))

    x2img = tf.reshape(x, [-1, 28, 28, 1], 'x2img')
    conv1 = tf.nn.relu(conv2d(x2img, w_c1) + b_c1, 'conv1')  # (28*28,32)
    pool1 = max_pool_2x2(conv1)  # (14*14,32)
    conv2 = tf.nn.relu(conv2d(pool1, w_c2) + b_c2, 'conv2')  # (14*14,64)
    pool2 = max_pool_2x2(conv2)  # (7*7,64)

    p2flat = tf.reshape(pool2, [-1, 7 * 7 * 64], 'p2flat')
    fc1 = tf.nn.relu(tf.matmul(p2flat, w_f1) + b_f1, 'fc1')

    f2drop = tf.nn.dropout(fc1, kp)
    # fc2 = tf.nn.relu(tf.matmul(f2drop, w_f2) + b_f2, 'fc2')
    fc2 = tf.add(tf.matmul(f2drop, w_f2), b_f2, 'fc2')

with tf.variable_scope('Loss'):
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=fc2, labels=y), name='c_e')

with tf.variable_scope('Train'):
    global_step = tf.get_variable('global_step', [], dtype=tf.int32, trainable=False,
                                  initializer=tf.constant_initializer(0))
    train_op = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss=cross_entropy, global_step=global_step)

with tf.variable_scope('Accuracy'):
    correct_pred = tf.equal(tf.argmax(fc2, 1), tf.argmax(y, 1))  # return [bool,bool,...]
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32), name='accuracy')


def train(mnist):
    saver = tf.train.Saver(max_to_keep=3)
    init = tf.global_variables_initializer()
    ckpt = tf.train.get_checkpoint_state('model3')
    with tf.Session() as sess:
        sess.run(init)
        validation_data = {x: mnist.validation.images[:1000, :], y: mnist.validation.labels[:1000, :], kp: 1.0}
        test_data = {x: mnist.test.images[:2000, :], y: mnist.test.labels[:2000, :], kp: 1.0}
        step = 0  # 记录步数（初始化）
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            step = sess.run(global_step)
            print('Update:{}'.format(step))
        while step < iteration:
            xs, ys = mnist.train.next_batch(batch_size)
            _, loss = sess.run([train_op, cross_entropy], feed_dict={x: xs, y: ys, kp: 0.8})
            step = sess.run(global_step)
            if step % display_step == 0:
                validation_accuracy = sess.run(accuracy, feed_dict=validation_data)
                print('[{}] [{:.2f}] [{:.4f}]'.format(step, loss, validation_accuracy))
                saver.save(sess, './model3/model.ckpt', global_step=step)
        print('*' * 10)
        test_accuracy = sess.run(accuracy, feed_dict=test_data)  # 10000个测试集丢进去
        print('the test accuracy is:{:.4f}'.format(test_accuracy))


def pred(mnist):
    saver = tf.train.Saver(max_to_keep=3)
    ckpt = tf.train.get_checkpoint_state('model3')
    with tf.Session() as sess:
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            tes_img = mnist.test.images[:2000, :]
            tes_lab = mnist.test.labels[:2000, :]
            for i in range(len(tes_img)):
                label2index = sess.run(tf.argmax(tes_lab[i]))
                d2img = sess.run(tf.reshape(tes_img[i], [-1, 28 * 28]))
                pred_lab = sess.run(fc2, feed_dict={x: d2img, kp: 1.0})
                pred_lab = sess.run(tf.reshape(pred_lab, [-1]))
                pred2index = sess.run(tf.argmax(pred_lab))
                # if not sess.run(tf.equal(label2index,pred2index)):
                #     print('[{}] [{}]'.format(label2index, pred2index))
                print('[{}] [{}]'.format(label2index, pred2index))
        else:
            print('NO Model!')


def main(argv=None):
    mnist = input_data.read_data_sets('mnist_data', one_hot=True)
    # print('training data size:{}'.format(mnist.train.num_examples))  # 训练集 55000
    # print('validate data size:{}'.format(mnist.validation.num_examples))  # 验证集 5000
    # print('test data size:{}'.format(mnist.test.num_examples))  # 测试集 10000
    # print('test data label:{}'.format(mnist.test.labels[0])) # 取出一个label看看
    start_time = time.time()
    # pred(mnist)
    train(mnist)
    end_time = time.time()
    print('duration:{:.2f}s '.format(end_time - start_time))


if __name__ == '__main__':
    tf.app.run()
