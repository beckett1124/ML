#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'qibin'

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns;sns.set()

from sklearn.datasets.samples_generator import make_blobs
x,y=make_blobs(n_samples=300,centers=4,random_state=0,cluster_std=0.6)
plt.scatter(x[:,0],x[:,1],s=50)
