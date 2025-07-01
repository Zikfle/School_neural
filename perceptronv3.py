# -*- coding: utf-8 -*-
# ---------------------------------------------------------
# Author: Félix Thibaud
# Created on: 2025-05-24
# Description: PerceptronFelix v3
# MIT License
# ---------------------------------------------------------
import matplotlib

import matplotlib.pyplot as plt
import random
import pandas as pd


alldots = [[40,15,'A'] , [65,30,'A'] , [67,26,'A'] , [14,2,'A'], [30,5,'A'] , [60,10,'A'] ,
           [80,24,'A'] , [54,28,'A'] , [82,31,'A'] , [30,5,'A'] ,  
           [25,45,'B'] , [5,60,'B'] , [70,75,'B'] ,[14,80,'B'] , [30,61,'B'], 
           [30,61,'B'], [100,75,'B'], [30,61,'B'], [41,55,'B'], [30,61,'B']]

class Perceptron:
    def __init__(self,input_size,learning_rate,max_epoch):
        self.weights = [random.uniform(-1, 1) for _ in range(input_size)]
        self.bias = 100
        self.lr = learning_rate
        self.max_epoch = max_epoch
        self.save_epoch = {'epoch' : [] , 'save' : [], 'loss' : []}
        self.save_step = {'step' : [] , 'save' : [], 'error' : [] }

    def predict(self,dot):
        sum = self.bias
        for val, wei in zip(dot,self.weights):
            sum += val * wei
        return 'A' if sum >= 0 else 'B'
    
    def train_one(self,input):
        dot = input[:-1]
        label = input[-1]
        target = 1 if label == 'A' else -1
        prediction = 1 if self.predict(dot) == 'A' else -1
        error = target - prediction
        new_weight = []
        for wei,val in zip(self.weights,dot):
            new_weight.append(wei+(self.lr*error*val))
        self.weights = new_weight
        self.bias = self.bias + (self.lr*error)
        return 1 if error != 0 else 0 # 1 = mistake, 0 = correct

    def training(self, data):
        step = 0
        flag = 0
        for epoch in range(1,self.max_epoch+1):
            save = list(self.weights)
            save.append(float(self.bias))
            self.save_epoch['epoch'].append(epoch)
            self.save_epoch['save'].append(save)
            loss = 0
            for input in data:
                step += 1
                save = list(self.weights)
                save.append(float(self.bias))
                self.save_step['step'].append(step)
                self.save_step['save'].append(save)
                error = self.train_one(input)
                loss += error
                self.save_step['error'].append(error)
            self.save_epoch['loss'].append(loss)
            if loss == 0:
                save = list(self.weights)
                save.append(float(self.bias))
                self.save_epoch['epoch'].append('succesful')
                self.save_epoch['save'].append(save)
                self.save_epoch['loss'].append(loss)
                flag = 1
                break
        if flag == 0:
            save = list(self.weights)
            save.append(float(self.bias))
            self.save_epoch['epoch'].append('failed')
            self.save_epoch['save'].append(save)
            self.save_epoch['loss'].append(loss)
    def get_value(self):
        save = list(self.weights)
        save.append(float(self.bias))
        return save
            
            
PerA = Perceptron(input_size=2, learning_rate=0.00001, max_epoch=10000)
PerA.training(alldots)

#df = pd.DataFrame.from_dict(PerA.save_epoch)
#print(df)
saves = PerA.save_epoch['save']
saveb = PerA.save_epoch['loss']
'''
for save,loss in zip(saves,saveb):
    print(save,loss)
'''
percept = PerA.get_value()

#calcul de la fonction
a = percept[0]
b = percept[1]
c = percept[2]

a2 = -(a/b)
c2 = -(c/b)

fonction = f'y = {a2:.2f}x + {c2:.2f}'

print(f'Perceptron : {percept}')
print(f'Fonction f(x) : {fonction}')
print(f'Satus of the training : {PerA.save_epoch['epoch'][-1]}')
print(f'Nb of epoch : {PerA.save_epoch['epoch'][-2]}')
print(f'Nb of steps : {PerA.save_step['step'][-2]}')

def graph_it(percept,data,epoch):
    # ******************* Représentation graphique de donné ***************
    #calcul de la fonction
    #print(percept)
    a = percept[0]
    b = percept[1]
    c = percept[2]

    a2 = -(a/b)
    c2 = -(c/b)

    fonction = f'y = {a2:.2f}x + {c2:.2f}'

    l_x = []
    l_y = []
    l_c = []
    green = (0,1,0)
    red = (1,0,0)

    for dot in data:
        l_x.append(dot[0])
        l_y.append(dot[1])
        label = dot[2]
        if label == 'A':
            color = green
        else:
            color = red
        l_c.append(color)
    plt.clf()  # clear figure
    plt.scatter(l_x,l_y,c=l_c)

    #*********** Représentation graphique du perceptron ******

    #x_max = max(l_x)
    x_max = max(l_x) + 1
    #x_min = min(l_x)
    x_min = 0

    y_max = - (a*x_max + c) / b
    y_min = - (a*x_min + c) / b

    x_val = [x_min,x_max]
    y_val = [y_min,y_max]

    plt.text(3, 3, f'epoch : {epoch}\n{fonction}', fontsize = 10)
    plt.plot(x_val, y_val)
    plt.pause(0.01)

for i in range(0,len(PerA.save_epoch['save']),4):
    save = PerA.save_epoch['save'][i]
    graph_it(save,alldots,i)
plt.show()