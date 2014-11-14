#!/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import copy
import math
import time

debug = 0

def gen_data(Sigma, Mu, k, N):
    global X
    global eMu
    global eSigma
    global Expectation
    X = np.zeros((1,N))
    eMu = np.random.random(k)
    eSigma = np.random.random(k)
    Expectation = np.zeros((N,k))

    for i in range(N):
        t = np.random.random(1)
        unit = float(1./k)
        cur = unit
        comp = 0
        while cur < t:
             cur = cur + unit
             comp = comp + 1
             #print t,cur

        X[0,i] = np.random.normal() * Sigma[0,comp] + Mu[0,comp]
    
    if debug:
        print "***********"
        print u"init data"
        print X

def eStep(k, N):
    global X
    global eMu
    global eSigma
    global Expectation

    for i in range(N):
        denom = 0
        for j in range(k):
            denom = denom + math.exp((-1./(2*float(eSigma[j]**2)))*(float(X[0,i]-eMu[j])**2))

        for j in range(k):
            numer = math.exp((-1./(2*float(eSigma[j]**2)))*(float(X[0,i]-eMu[j])**2))
            Expectation[i,j] = numer / denom

def mStep(k, N):
    global X
    global eMu
    global eSigma
    global Expectation

    for i in range(k):
        denom = 0
        numer_S = 0
        numer_M = 0

        for j in range(N):
            denom = denom + Expectation[j,i]
            numer_M = numer_M + Expectation[j,i]*X[0,j]
            numer_S = numer_S + Expectation[j,i]*(float(X[0,j]-eMu[i])**2)

        eMu[i] = numer_M / denom
        eSigma[i] = numer_S / denom

def run(Sigma, Mu, k, N, times, epsilon):
    gen_data(Sigma, Mu, k, N)
    
    for i in range(times):
        old_mu = copy.deepcopy(eMu)
        eStep(k, N)
        mStep(k, N)
        
        time.sleep(1)
        print Mu
        print eMu
        print
        if sum(abs(eMu-old_mu))<epsilon:
            break


if __name__=='__main__':
    k = raw_input("input k: ")
    N = raw_input("input N: ")

    N = int(N)
    k = int(k)
    print k
    Mu = np.zeros((1,k))
    Sigma = np.zeros((1,k))
    
    for i in range(k):
        Mu[0,i] = i

    for i in range(k):
        Sigma[0,i] = (i+1)*2

    #gen_data(Sigma, Mu, k, N)
    run(Sigma, Mu, k, N, 1000, 0.1)
