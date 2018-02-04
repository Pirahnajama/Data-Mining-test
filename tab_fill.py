import random
import time





def random_line_5 (tab_line):
    for i in range(0,5):
        tab_line.append(random.random()*10)
    return tab_line

def random_line_10 (tab_line):
        for i in range(0,5):
            tab_line.append(random.random()*10+10)
        return tab_line

def random_mat (tab_mat):
    tab_line=[]
    for i in range(0,5):
        tab_mat.append(random_line_5(tab_line))
        tab_line=[]
    for i in range(0,5):
        tab_mat.append(random_line_10(tab_line))
        tab_line=[]
