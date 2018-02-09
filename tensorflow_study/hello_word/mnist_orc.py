#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import time
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 获取mnist数据
# mnist = input_data.read_data_sets('mnist_data', one_hot=True)
# print('training data size: {}'.format(mnist.train.num_examples))  # 训练集 55000
# print('validate data size: {}'.format(mnist.validation.num_examples))  # 验证集 5000
# print('test data size: {}'.format(mnist.test.num_examples))  # 测试集 10000
# print('test data label: {}'.format(mnist.test.labels[0]))

# 定义超参数
batch_size = 50  # 一批输入的数据个数
learning_rate = 0.01  # 学习速率：梯度下降的幅度
iteration_step = 10000  # 迭代训练次数
display_step = 500

# 定义神经元个数
n_input = 784  # 28*28
n_hidden = 500
n_labels = 10


# 定义神经网络（仅一个隐藏层）
def network(x_input, reuse=False):
    with tf.variable_scope('hidden', reuse):
        weights = tf.get_variable('weights', [n_input, n_hidden],
                                  initializer=tf.truncated_normal_initializer(
                                      stddev=0.1))  # 用一个较小的正数来初始化偏置项，以避免神经元节点输出恒为0的问题
        biases = tf.get_variable('biases', [n_hidden], initializer=tf.constant_initializer(0.1))
        hidden = tf.nn.relu(tf.matmul(x_input, weights) + biases)
    with tf.variable_scope('out', reuse):
        weights = tf.get_variable('weights', [n_hidden, n_labels],
                                  initializer=tf.truncated_normal_initializer(stddev=0.1))
        biases = tf.get_variable('biases', [n_labels], initializer=tf.constant_initializer(0.1))
        output = tf.matmul(hidden, weights) + biases  # 不必softmax 因为tf.nn.softmax_cross_entropy_with_logits_v2
    return output


# 定义训练过程
def train(mnist):
    x = tf.placeholder(tf.float32, [None, n_input])
    y = tf.placeholder(tf.float32, [None, n_labels])
    pred = network(x)
    # 计算损失函数-交叉熵
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=pred, labels=y))
    # 定义优化器
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cross_entropy)
    # 定义准确率计算
    correct_pred = tf.equal(tf.argmax(pred, axis=1),
                            tf.argmax(y, axis=1))  # argmax取pred和y每一行最大值的索引 equal判断是否相等 返回bool的张量
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))  # case将bool张量转【0，1，0，0】这样子

    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init)
        # 定义验证集和测试集
        validate_data = {x: mnist.validation.images, y: mnist.validation.labels}
        test_data = {x: mnist.test.images, y: mnist.test.labels}

        for i in range(iteration_step):
            # xs,ys该循环的每个步骤中，我们都会随机抓取训练数据中的batch_size个批处理数据点（每次不重复点，除非用完了所有点），然后我们用这些数据点作为参数替换之前的占位符来运行optimizer
            xs, ys = mnist.train.next_batch(batch_size)
            _, loss = sess.run([optimizer, cross_entropy], feed_dict={x: xs, y: ys})

            if i % display_step == 0:
                validate_accuracy = sess.run(accuracy, feed_dict=validate_data)
                print('step:{} loss:{:.2f} validation accuracy:{:.4f}'.format(i, loss, validate_accuracy))
        print('the training is finish!')
        # 最终的测试准确率
        test_accuracy = sess.run(accuracy, feed_dict=test_data)
        print('the test accuracy is:{:.4f}'.format(test_accuracy))


def main(argv=None):
    mnist = input_data.read_data_sets('mnist_data', one_hot=True)
    # print('training data size:{}'.format(mnist.train.num_examples))  # 训练集 55000
    # print('validate data size:{}'.format(mnist.validation.num_examples))  # 验证集 5000
    # print('test data size:{}'.format(mnist.test.num_examples))  # 测试集 10000
    # print('test data label:{}'.format(mnist.test.labels[0])) # 取出一个label看看
    start_time = time.time()
    train(mnist)
    end_time = time.time()
    print('duration:{:.2f}s '.format(end_time - start_time))


if __name__ == '__main__':
    tf.app.run()
