import tab_fill
import random
import time
import math

print("######################################")
print("#    Debut apprentissage K-means     #")
print("######################################")
print("                            ")

def addSquare(x,y):
    return (x-y)*(x-y)

def distanceEuclid(tab_line1,tab_line2):
    temp=0
    for i in range(len(tab_line1)):
            temp=temp+addSquare(tab_line1[i],tab_line2[i])
    return math.sqrt(temp)

tab_mat=[]

random.seed(time.time())

tab_fill.random_mat(tab_mat)

for i in tab_mat:
    print(i)

print(distanceEuclid(tab_mat[0],tab_mat[1]))

print("                            ")
print("#########################################")
print("#       Fin Execution programme         #")
print("#########################################")
