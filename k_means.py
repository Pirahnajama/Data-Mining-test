import tab_fill
import distance_perso
import random
import time
import math
import copy

print("######################################")
print("#    Debut apprentissage K-means     #")
print("######################################")
print("                            ")

def node_selec(tab_mat):
    global tab_node1
    global tab_node2
    temp1=random.randint(0,5)-1
    tab_node1=copy.deepcopy(tab_mat[temp1])
    temp2=random.randint(5,10)-1
    tab_node2=copy.deepcopy(tab_mat[temp2])

def cluster(tab_mat,tab_node1,tab_node2):
        for i in tab_mat:
            temp1=distance_perso.distanceEuclid(i,tab_node1)
            temp2=distance_perso.distanceEuclid(i,tab_node2)
            if temp1<temp2:
                i.append("node1")
            else:
                i.append("node2")







tab_mat=[]
tab_node1=[]
tab_node2=[]

random.seed(time.time())

tab_fill.random_mat(tab_mat)

for i in tab_mat:
    print(i)

node_selec(tab_mat)
print(tab_node1)
print(tab_node2)
cluster(tab_mat,tab_node1,tab_node2)

for i in tab_mat:
    print(i)



print("                            ")
print("#########################################")
print("#       Fin Execution programme         #")
print("#########################################")
