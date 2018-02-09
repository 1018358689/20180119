#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import time
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

m = 1 # m=1,2 accuracy:0.9815,0.9800 duration:347.93s,807.42s
# 定义超参数
batch_size = 50  # 一批输入的数据个数
learning_rate = 0.01  # 学习速率：梯度下降的幅度
iteration = 10000  # 迭代训练次数
display_step = 500  # 打印的布次

# 定义神经元个数
# n_input = 784  # 28*28
# n_hidden = 500
# n_labels = 10

x = tf.placeholder(tf.float32, [None, 28 * 28])
y = tf.placeholder(tf.float32, [None, 10])
keep_prob = tf.placeholder(tf.float32)


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


w = {
    'conv1': weight_variable([5, 5, 1, 32*m]),  # 对应filter 第一二参数值得卷积核尺寸大小，即patch，第三个参数是图像通道数，第四个参数是卷积核的数目，代表会出现多少个卷积特征图像
    'conv2': weight_variable([5, 5, 32*m, 64*m]),
    'fc1': weight_variable([7 * 7 * 64*m, 1024]),  # 只有一行7*7*64个数据的卷积，第二个参数代表卷积个数共1024个 7=28/2/2
    'fc2': weight_variable([1024, 10]),
}


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


b = {
    'conv1': bias_variable([32*m]),
    'conv2': bias_variable([64*m]),
    'fc1': bias_variable([1024]),
    'fc2': bias_variable([10]),

}


def conv2d(x, w):
    # https://www.cnblogs.com/smartwhite/p/7819689.html
    return tf.nn.conv2d(
        input=x, # 输入的图片参数：[batch张图片, 每张图片高度为in_height, 每张图片宽度为in_width, 图像通道为in_channels]
        filter=w, # 滤波器：[滤波器高度, 滤波器宽度, 接受图像的通道数, 卷积后通道数]
        strides=[1, 1, 1, 1], # 步长：每跨多少步抽取信息，strides[1, x_movement,y_movement, 1]， strides[0]和[3]必须为1
        padding='SAME', #边距处理：“SAME”表示输出图层和输入图层大小保持不变？，设置为“VALID”时表示舍弃多余边距(丢失信息)
    )


def max_pool_2x2(x):
    # return tf.nn.max_pool(x, [1, 2, 2, 1], [1, 2, 2, 1], 'SAME')
    return tf.nn.max_pool(
        value=x,
        ksize=[1, 2, 2, 1],
        strides=[1, 2, 2, 1],
        padding='SAME',
    )


def network(x_input, reuse=False):
    # 输入图片转换成单通道
    x_image = tf.reshape(x_input,
                         [-1, 28, 28, 1])  # x_image又把xs reshape成了28*28*1的形状，因为是灰色图片，所以通道是1.作为训练时的input，-1代表图片数量不定
    # 在这我们把输入shape转换成了4D tensor，第二与第三维度对应的是照片的宽度与高度，最后一个维度是颜色通道数，本例子中是1。
    # 第一层卷积+池化
    h_conv1 = tf.nn.relu(conv2d(x_image, w['conv1']) + b['conv1'])
    h_pool1 = max_pool_2x2(h_conv1)

    # 第二层卷积+池化
    h_conv2 = tf.nn.relu(conv2d(h_pool1, w['conv2']) + b['conv2'])
    h_pool2 = max_pool_2x2(h_conv2)
    # 第一层全连接
    h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64*m])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, w['fc1']) + b['fc1'])
    # 第二层全连接
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob) # 按照keep_prob的概率扔掉一些，为了减少过拟合 ：0.8表示保留80%
    h_fc2 = tf.matmul(h_fc1_drop, w['fc2']) + b['fc2']
    return h_fc2


def train(mnist):
    pred = network(x)
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=pred, labels=y))
    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)

    correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)

        val_data = {x: mnist.validation.images[:1000, :], y: mnist.validation.labels[:1000, :], keep_prob: 1.0}
        tes_data = {x: mnist.test.images[:2000, :], y: mnist.test.labels[:2000, :], keep_prob: 1.0}

        for i in range(iteration):
            xs, ys = mnist.train.next_batch(batch_size)  # batch_size个训练集丢进去训练
            _, loss = sess.run([optimizer, cross_entropy], feed_dict={x: xs, y: ys, keep_prob: 0.8})
            if i % display_step == 0:
                val_accuracy = sess.run(accuracy, feed_dict=val_data)  # 5000个验证集丢进去
                print('[{}] [{:.2f}] [{:.4f}]'.format(i, loss, val_accuracy))
        print('*' * 10)
        final_accuracy = sess.run(accuracy, feed_dict=tes_data)  # 10000个测试集丢进去
        print('the test accuracy is:{:.4f}'.format(final_accuracy))


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
