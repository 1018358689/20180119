#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Time    : 2018/2/9 1:30
# @Author  : 11
# @File    : gpu_test.py
from tensorflow.python.client import device_lib as _device_lib


def is_gpu_available(cuda_only=True):
    """
    code from https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/platform/test.py
    Returns whether TensorFlow can access a GPU.
    Args:
      cuda_only: limit the search to CUDA gpus.
    Returns:
      True iff a gpu device of the requested kind is available.
    """

    if cuda_only:
        return any((x.device_type == 'GPU')
                   for x in _device_lib.list_local_devices())
    else:
        return any((x.device_type == 'GPU' or x.device_type == 'SYCL')
                   for x in _device_lib.list_local_devices())


def get_available_gpus():
    """
    查看GPU的命令：nvidia-smi
    查看被占用的情况：ps aux | grep PID
    :return: GPU个数
    """
    local_device_protos = _device_lib.list_local_devices()
    print("all: %s" % [x.name for x in local_device_protos])
    print("gpu: %s" % [x.name for x in local_device_protos if x.device_type == 'GPU'])


print(is_gpu_available())
print(get_available_gpus())
