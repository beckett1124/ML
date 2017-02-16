#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'qibin'

import numpy as np

X=np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
Y=np.array([[0,1,10]]).T

syn0=2*np.random.random((3,4))-1
syn1=2*np.random.random((4,1))-1

for j in xrange(60000):
    l1=1/(1+np.exp(-(np.dot(X,syn0))))
    l2=1/(1+np.exp(-(np.dot(l1,syn1))))

