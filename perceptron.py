# -*- coding: utf-8 -*-
# ---------------------------------------------------------
# Author: Félix Thibaud
# Created on: 2025-05-24
# Description: Word to make thing's move
# MIT License
# ---------------------------------------------------------

import matplotlib.pyplot as plt
import random

def predicting(vals,perceptron):
    if len(vals) != len(perceptron)-1:
        print('Error : data lenght not equal to perceptron length')
        return 'Error'
    produits = []
    for value,weight in zip(vals,perceptron[:-1]):
        produits.append(value*weight)
    somme = sum(produits)+perceptron[-1]
    if somme > 0:
         prediction = 'A'
    else:
         prediction = 'B'
    return prediction

def train(vals,percep,learningrate,label,prediction):
    if prediction != label:
        if label == 'A':
            error = 1
        if label == 'B':
            error = -1
    else:
        error = 0

    new_perceptron = []
    for val,poid in zip(vals,percep[:-1]):
        new_perceptron.append(poid+(learningrate*error*val))
    new_perceptron.append(percep[-1]+(learningrate*error))


    return [new_perceptron,error]

def train_on_data(perceptron,data,learningrate):
    hits = []
    flag = 0
    for dot in data:
        vals = dot[:-1]
        label = dot[-1]
        pred = predicting(vals,perceptron)
        result = train(vals,perceptron,learningrate,label,pred)
        perceptron = result[0]
        hits.append(result[1])
        #print(perceptron)
    if (1 or -1) not in hits:
        flag = 1
    return [perceptron,flag]



alldots = [[2,3,'A'] , [6,7,'A'] , [3,2,'A'] , [14,2,'A'], [30,5,'A'] , [3,10,'B'] , [5,60,'B'] , [9,20,'B'] ,[14,80,'B'] , [30,61,'B']]


learningrate = 0.0000001
maxepochs = 1000000

data_len = len(alldots[0])
perceptron = []

for x in range(data_len):
    perceptron.append(random.uniform(-1, 1))

log = []

for epoch in range(maxepochs):
        #print(f'epoch : {epoch}')
        #print(f'Perceptron : {perceptron}')
        log.append([epoch,perceptron])
        results = train_on_data(perceptron,alldots,learningrate)
        perceptron = results[0]
        if results[1] == 1:
            break


print("Évolution du Perceptron".center(50,'*'))
for x in log[-10:]:
    epoc = x[0]
    per = x[1]
    print(f"Epoch {epoc} :\nPercepron = {per} ")
print('\n')

print("RESULTAT".center(50,'*'))
print(f'Valeur du perceptron final: {perceptron}')
print(f"Nombre d'epoch : {epoch}")

# ******************* Représentation graphique de donné ***************

l_x = []
l_y = []
l_c = []
green = (0,1,0)
red = (1,0,0)


for dot in alldots:
    l_x.append(dot[0])
    l_y.append(dot[1])
    label = dot[2]
    if label == 'A':
        color = green
    else:
        color = red
    l_c.append(color)


plt.scatter(l_x,l_y,c=l_c)


#*********** Représentation graphique du perceptron ******

c = perceptron[2]
a = perceptron[0]
b = perceptron[1]

#x_max = max(l_x)
x_max = max(l_x) + 1
#x_min = min(l_x)
x_min = 0

# 0 = ax + by + c
# - by = ax + c
# y = - (ax + c) / b
a2 = -(a/b)
c2 = -(c/b)
 
y_max = - (a*x_max + c) / b
y_min = - (a*x_min + c) / b

x_val = [x_min,x_max]
y_val = [y_min,y_max]





fonction = f'y = {a2:.2f}x + {c2:.2f}'
print(fonction)
plt.text(3, 3, fonction, fontsize = 10)


plt.plot(x_val, y_val)

plt.show()