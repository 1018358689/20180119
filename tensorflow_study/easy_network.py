#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

'''
1.定义神经网络的结构，即计算图

2.定义损失函数

3.在会话中，将数据输入进构建的神经网络中，反复优化损失函数，直至得到最优解

4.将测试集丢入训练好的神经网络进行验证

'''

## part one：定义神经网络的结构，即计算图（假设我们创建一个只有两个隐藏层的神经网络）

# step1：定义超参数
learning_rate = 0.01  # 学习速率；梯度下降的幅度
bath_size = 16  # 一批输入数据的个数
epoch_step = 10 ** 4  # 迭代次数，1个epoch等于使用训练集中的全部样本训练一次；
display_step = 10 ** 2  # 打印中间结果的步数

# step2：定义输入层、隐藏层、输出层神经元
# x：输入层 [None, 784]表示x的维度，其中None代表该数暂时不确定，其实这个None与batch_size的数据相对应，x可理解为一次性输入batch_size个数据，而每个数据有784个特征向量组成，即输入层有784个神经元。
# y：输出层 因为有None个数据输入，所以输出也为None。10代表进行10分类
# layer1、layer2代表隐藏层神经元个数
x = tf.placeholder('float', [None, 784])
y = tf.placeholder('float', [None, 10])
layer1 = 16
layer2 = 32

# step3：定义神经网络参数w、b
# w中，h1代表的是输入层到第一层隐藏层的权重，因为输入层有784个神经元，隐藏层神经元个数为layer1，所以维度为[784, layer1]。h2同理。out表示第二层隐藏层到输出层的权重。
w = {
    'h1': tf.Variable(tf.random_normal([784, layer1])),
    'h2': tf.Variable(tf.random_normal([layer1, layer2])),
    'out': tf.Variable(tf.random_normal([layer2, 10])),
}

b = {
    'h1': tf.Variable(tf.random_normal([layer1])),
    'h2': tf.Variable(tf.random_normal([layer2])),
    'out': tf.Variable(tf.random_normal([10]))
}

# step4：定义神经网络network
# 其中，tf.nn.relu是非线性激励函数，常用的还有tf.sigmoid、tf.tanh
def network(x_input, weights, biases):
    net1 = tf.nn.relu(tf.matmul(x_input, weights['h1']) + biases['h1'])
    net2 = tf.nn.relu(tf.matmul(net1, weights['h2']) + biases['h2'])
    output = tf.matmul(net2, weights['out']) + biases['out']
    return output


## part two：定义损失函数

# 其中pred为预测的数据，即神经网络的输出
# cost即损失函数，tf.reduce_mean是求平均损失，因为一次性输入的是多个（batch_size个）数据。
# softmax层的作用是将输出层的数据全部压缩至0~1之间，并且所有和等于1。这就可以理解成将输出层的数据变成概率分布的形式。然后就可以用交叉熵函数定义损失函数了。
# tf.nn.softmax_cross_entropy_with_logits损失函数：即先经过softmax层然后使用交叉熵就算损失。
# tf.train.AdamOptimizer是选择的优化器，其作用是最小化cost
pred = network(x_input=x, weights=w, biases=b)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=pred, labels=y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# tf.argmax函数返回的是张量在某一维最大值的索引值，由于标签向量是由0,1组成，因此最大值1所在的索引位置就是类别标签。如果pred的最大值所在的索引值等于类别标签的索引值，表示这个结果分类正确
# tf.equal是TensorFlow中判断两个张量是否相等，返回的是一个布尔型张量，如[True,False,False]。
# 因为corret_pred是一个布尔型张量，因此需要用tf.cast()函数转化成float型来计算准确率，如[True,False,False，False]会变成[1,0,0,0]，经过reduce_mean取平均值0.25来表示准确率。
correct_pred = tf.equal(tf.argmax(y, 1), tf.argmax(pred, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, 'float'))

init = tf.global_variables_initializer()

## part three：创建会话，执行神经网络，将数据输入进构建的神经网络中，反复优化损失函数，直至得到最优解

# 遍历epoch_step次所有数据，avg_cost用来记录一个epoch里所损失平均，注意cost是一个batch_size里的平均损失，两次平均不一样。total_batch表示batch_size的个数。
# 执行optimizer与cost，因为之前定义的x与y是用的占位符tf.placeholder，这里就要用feed_dict进行数据喂养。
with tf.Session() as sess:
    sess.run(init)
    for epoch in range(epoch_step):
        avg_cost = 0
        total_batch = int(alldata / bath_size)  # alldata：所有数据的大小
        for i in range(total_batch):
            x_batch, y_batch = '一个batch_size的输入', '以及相对应的输入的标签'
            output = sess.run([optimizer, cost], feed_dict={x: x_batch, y: y_batch})
            avg_cost += output / total_batch
        if epoch % display_step == 0:
            print('cost: {}'.format(avg_cost))
    print('finish!')
    acc = sess.run(accuracy, feed_dict={x: test_x, y: test_y})  # test_x、test_y就是测试集
    print('accuracy: ')
## part four：将测试集丢入训练好的神经网络进行验证
