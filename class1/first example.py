# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 17:08:32 2020

@author: avi
"""
import math
def sse(m,b,x,y):
    sum = 0
    for i in range (0,len(x)):
        YP=(m*x[i])+b
        #print("X is " + str(x[i]) + " y is " + str(y[i]) + " YP is " + str(YP))
        sse_temp =  0.5*math.pow(y[i]-YP,2)
        sum+=sse_temp
    return sum

# def mse(a,b,x,y):
#     sum = 0
#     for i in range (0,len(x)):
#         YP=a+(b*x[i])
#         #print("X is " + str(x[i]) + " y is " + str(y[i]) + " YP is " + str(YP))
#         sse_temp =  0.5*math.pow(y[i]-YP,2)
#         sum+=sse_temp
#     return sum/len(x)

def dm(m,b,x,y):
    sum = 0
    for i in range (0,len(x)):
        YP=(m*x[i])+b
        #print("X is " + str(x[i]) + " y is " + str(y[i]) + " YP is " + str(YP))
        temp =  -1*(y[i]-YP)*x[i]
        sum+=temp
    return sum

def db(m,b,x,y):
    sum = 0
    for i in range (0,len(x)):
        YP=(m*x[i])+b
        #print("X is " + str(x[i]) + " y is " + str(y[i]) + " YP is " + str(YP))
        temp =  -1*(y[i]-YP)
        sum+=temp
    return sum


lr=0.01
b=0.45
m=0.75
x =[0, 0.22, 0.24, 0.33, 0.37, 0.44, 0.44, 0.57, 0.93,1]
y= [0, 0.22, 0.58, 0.2, 0.55, 0.39, 0.54, 0.53, 1, 0.61]
epsilon=0.0001
iteration=1
sse_change=sse(m,b,x,y)
while(sse_change>epsilon):
    sse_prev=sse(m,b,x,y)
    print("Iteration is " + str(iteration))
    #print(sse(a,b,x,y))
    print("SSE is " + str(sse(m,b,x,y)))
    print("dm " + str(dm(m,b,x,y)))
    print("db " + str(db(m,b,x,y)))
    m=m-lr*dm(m,b,x,y)
    b=b-lr*db(m,b,x,y)
    print("m is " + str(m))    
    print("b is " + str(b))  
    sse_change=abs(sse_prev-sse(m,b,x,y))
    print("sse change " + str(sse_change))
    iteration+=1
    if (iteration==100):
        sse_change=0
    
