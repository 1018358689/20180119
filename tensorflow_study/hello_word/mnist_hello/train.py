#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from model import CNN_model
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


class Train:
    def __init__(self, mnist):
        self.mnist = mnist
        self.model = CNN_model()
        self.batch_size = 64
        self.iteration = 10000
        self.display_step = 500
        self.sess = tf.Session()
        self.sess.run(tf.global_variables_initializer())

    def train(self):
        val_data = {self.model.x: self.mnist.validation.images[:1000, :],
                    self.model.y: self.mnist.validation.labels[:1000, :], self.model.kp: 1.0}
        tes_data = {self.model.x: self.mnist.test.images[:2000, :], self.model.y: self.mnist.test.labels[:2000, :],
                    self.model.kp: 1.0}
        for i in range(1, self.iteration + 1):
            xs, ys = self.mnist.train.next_batch(self.batch_size)
            _, loss = self.sess.run([self.model.train, self.model.loss],
                                    feed_dict={self.model.x: xs, self.model.y: ys, self.model.kp: 0.8})
            if i % self.display_step == 0:
                val_accuracy = self.sess.run(self.model.accuracy, feed_dict=val_data)
                print('[{}] [{:.2f}] [{:.4f}]'.format(i, loss, val_accuracy))
        print('*' * 10)
        final_accuracy = self.sess.run(self.model.accuracy, feed_dict=tes_data)  # 10000个测试集丢进去
        print('the test accuracy is:{:.4f}'.format(final_accuracy))
        self.sess.close()


def main(argv=None):
    import time

    mnist = input_data.read_data_sets('../mnist_data', one_hot=True)
    app = Train(mnist)
    start_time = time.time()
    app.train()
    end_time = time.time()
    print('duration:{:.2f}s '.format(end_time - start_time))


if __name__ == '__main__':
    tf.app.run()