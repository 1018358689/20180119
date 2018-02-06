#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import time
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 获取mnist数据
# mnist = input_data.read_data_sets('mnist_data', one_hot=True)
# print('training data size: {}'.format(mnist.train.num_examples))  # 训练集
# print('validate data size: {}'.format(mnist.validation.num_examples))  # 验证集
# print('test data size: {}'.format(mnist.test.num_examples))  # 测试集
# print('test data label: {}'.format(mnist.test.labels[0]))

# 定义超参数
batch_size = 100  # 一批输入的数据个数
learning_rate = 0.1  # 学习速率：梯度下降的幅度
training_step = 30000  # 训练次数
display_step = 1000

# 定义神经元个数
n_input = 784
n_hidden = 500
n_labels = 10


# 定义神经网络（仅一个隐藏层）
def network(x_input, reuse=False):
    with tf.variable_scope('hidden', reuse):
        weights = tf.get_variable('weights', [n_input, n_hidden], initializer=tf.random_normal_initializer())
        biases = tf.get_variable('biases', [n_hidden], initializer=tf.constant_initializer(0.0))
        hidden = tf.nn.relu(tf.matmul(x_input, weights) + biases)
    with tf.variable_scope('out', reuse):
        weights = tf.get_variable('weights', [n_hidden, n_labels], initializer=tf.random_normal_initializer())
        biases = tf.get_variable('biases', [n_labels], initializer=tf.constant_initializer(0.0))
        output = tf.matmul(hidden, weights) + biases
    return output


# 定义训练过程
def train(mnist):
    x = tf.placeholder('float', [None, n_input])
    y = tf.placeholder('float', [None, n_labels])
    pred = network(x)
    # 计算损失函数-交叉熵
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=pred, labels=y))
    # 定义优化器
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cross_entropy)
    # 定义准确率计算
    correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init)
        # 定义验证集和测试集
        validate_data = {x: mnist.validation.images, y: mnist.validation.labels}
        test_data = {x: mnist.test.images, y: mnist.test.labels}

        for i in range(training_step):
            # xs,ys为每个batch_size的训练数据对应的标签
            xs, ys = mnist.train.next_batch(batch_size)
            _, loss = sess.run([optimizer, cross_entropy], feed_dict={x: xs, y: ys})

            if i % display_step == 0:
                validate_accuracy = sess.run(accuracy, feed_dict=validate_data)
                print('step:{} loss:{} validation accuracy:{}'.format(i, loss, validate_accuracy))
        print('the training is finish!')
        # 最终的测试准确率
        test_accuracy = sess.run(accuracy, feed_dict=test_data)
        print('the test accuracy is:{}'.format(test_accuracy))


def main(argv=None):
    mnist = input_data.read_data_sets('mnist_data', one_hot=True)
    # print('training data size:{}'.format(mnist.train.num_examples))  # 训练集 55000
    # print('validate data size:{}'.format(mnist.validation.num_examples))  # 验证集 5000
    # print('test data size:{}'.format(mnist.test.num_examples))  # 测试集 10000
    # print('test data label:{}'.format(mnist.test.labels[0])) # 取出一个label看看
    start_time = time.time()
    train(mnist)
    end_time = time.time()
    print('duration:{}s '.format(end_time - start_time))


if __name__ == '__main__':
    tf.app.run()
