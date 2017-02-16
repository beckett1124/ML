#/usr/bin/python
# -*- coding:utf-8 -*-

from numpy import *
import matplotlib.pyplot as plt

def loadDataSet(filename):
    dataMat = []
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split('\t')[3:]
        fltLine = map(float, curLine)
        dataMat.append(fltLine)
    return dataMat

def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))

def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k, n)))
    for j in range(n):
        minJ = min(array(dataSet)[:, j])
        rangeJ = float(max(array(dataSet)[:,j]) - minJ)
        centroids[:, j] = mat(minJ + rangeJ * random.rand(k, 1))
    return centroids

def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = shape(dataSet)[0]
    n = shape(dataSet)[1]
    clusterAssment = mat(zeros((m, 2)))
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf
            minIndex = -1
            for j in range(k):
                distJ = distMeas(array(centroids)[j,:],array(dataSet)[i,:])
                if distJ < minDist:
                    minDist = distJ
                    minIndex = j
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist ** 2
        print centroids
        for cent in range(k):
            #print clusterAssment[:,0]
            ptsInClust = dataSet[nonzero(array(clusterAssment)[:,0]==cent)[0][0]]
            centroids[cent, :] = mean(ptsInClust, axis=0)
            id = nonzero(array(clusterAssment)[:,0] == cent)[0]
    return centroids, clusterAssment, id

def plotBestFit(dataSet, id , centroids):
    dataArr = array(dataSet)
    cent = array(centroids)
    n = shape(dataArr)[0]
    n1 = shape(cent)[0]

    xcord1=[];ycord1=[]
    xcord2=[];ycord2=[]
    xcord3=[];ycord3=[]
    j=0
    for i in range(n):
        if j in id:
            xcord1.append(dataArr[i,0]);ycord1.append(dataArr[i,1])
        else:
            xcord2.append(dataArr[i,0]);ycord2.append(dataArr[i,1])
        j=j+1
    for k in range(n1):
        xcord3.append(cent[k,0]);ycord3.append(cent[k, 1])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')
    ax.scatter(xcord2,ycord2,s=30,c='green')
    ax.scatter(xcord3,ycord3,s=30,c='blue')

    plt.xlabel('X1');plt.ylabel('Y1')
    plt.show()

if __name__ == '__main__':
    dataMat = loadDataSet('0811_top200k_cluster')
    #print dataMat

    a=[]
    b=[]
    a, b, id = kMeans(dataMat,2)
    plotBestFit(dataMat, id , a)
