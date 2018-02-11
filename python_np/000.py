#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np

#创建数组
list = [1,2,3,4]
array = np.array(list)
array1 = np.array([[1.],[2.],[3.]])
# print(array1)

#数组元素个数
array1_size = array1.size
# print(array1_size)

#数组形状
array1_shape = array1.shape
# print(type(array1_shape))
# print(array1_shape)

#数组维度
array1_ndim = array1.ndim
# print(array1_ndim)

#数组元素类型
array1_dtype = array1.dtype
# print(array1_dtype)

#创建10*10的浮点1矩阵
array_10_10_1 = np.ones((10,10))
# print(array2)

#创建10*10的浮点0矩阵
array_10_10_0 = np.zeros((10,10))
# print(array_10_10_0)
# print(array_10_10_0.dtype)

#创建10*10的随即数组（0-1）
array3 = np.random.rand(10,10)
# print(array3)

#创建5*的一维数组（0-100）
array4 = np.random.uniform(0, 100, size=5)
print(array4)
print(array4.shape)
#创建6*的一维数组（0-50）
array5 = np.random.randint(0, 50, size=6)
# print(array5)

#创建均值=1.5，标准差=0.1的2*3的矩阵
array_normal = np.random.normal(1.5, 0.1, (3,4))
# print(array_normal)

#矩阵切割根据索引1、2行2列（索引从0开始）
array_normal2 = array_normal[1:3,2:3]
# print(array_normal2)

#改变矩阵形状（要求个数相同）
array_reshape = array_normal.reshape((2,6))
# print(array_reshape)

#改变矩阵形状（不要求个数相同）原矩阵改变  reshape函数返回一个新数组，但原数组本身不变；resize在返回一个新数组的同时也改变原数组本身。
array_normal.resize((2,3), refcheck=False)
# print(array_normal)

array_test = np.random.rand(2,3)*100
# print(array_test)

#条件运算
array_than = array_test >50
# print(array_than)

#三木运算
array_three = np.where(array_test<50, 0, 1)
# print(array_three)

#求每一行（列）最值 axis=0表示列 axis=1表示行  max--min  amax--amin 不加axis即求所有的均值
array_0_max = array_test.max()
array_0_max2 = np.amax(array_test, axis=0)
# print(array_0_max)
# print(array_0_max2)

#求每一行（列）平均值 不加axis即求所有的均值
array_0_mean = np.mean(array_test)
array_0_mean2 = array_test.mean(axis=0)
# print(array_0_mean)
# print(array_0_mean2)

#求每一行（列）方差 不加axis即求所有的均值
array_0_std = np.std(array_test)
array_0_std2 = array_test.std(axis=0)
# print(array_0_std)
# print(array_0_std2)

#矩阵运算(m_n)*(n_b)=(m_b) n相同
array_grades = np.array([[80,90],[70,66],[90,98],[66,67]])
array_percent = np.array([[0.4],[0.6]])
matrixmul = np.dot(array_grades,array_percent)
# print(matrixmul)

#矩阵拼接 vstack垂直拼接 hstack水平拼接
array_vstack = np.vstack((array_10_10_0,array_10_10_1))
array_hstack = np.hstack((array_10_10_0,array_10_10_1))
# print(array_vstack)
# print(array_hstack)
# a = [[1.],
#      [2.],
#      [3.]]
# b = np.array(a)
# print(a,b)
# print(type(a),type(b))

# result = np.genfromtxt('./test1.csv', delimiter=',')
# print(result)