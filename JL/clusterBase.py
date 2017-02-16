#/usr/bin/python
# -*- coding:utf-8 -*-

from math import sqrt

def importData(FIFE = '0811_top200k_cluster'):
    dataMat = []
    fr = open(FIFE)
    for line in fr.readlines():
        curLine = line.strip().split('\t')[3:]
        fltLine = map(float, curLine)
        dataMat.append(fltLine)
    return dataMat

def pearson_distance(vector1, vector2):
    """
    Calculate distance between two vectors using pearson method
    See more : http://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient
    """
    sum1 = sum(vector1)
    sum2 = sum(vector2)

    sum1Sq = sum([pow(v, 2) for v in vector1])
    sum2Sq = sum([pow(v, 2) for v in vector2])

    pSum = sum([vector1[i] * vector2[i] for i in range(len(vector1))])

    num = pSum - (sum1*sum2/len(vector1))
    den = sqrt((sum1Sq - pow(sum1, 2)/len(vector1)) * (sum2Sq - pow(sum2, 2)/len(vector1)))

    if den == 0 : return 0.0
    return 1.0 - num/den
