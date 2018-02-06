#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np

a = np.array([[1, 5, 5, 2],
              [9, 6, 2, 8],
              [3, 7, 9, 1]])
print(np.argmax(a, axis=0))
