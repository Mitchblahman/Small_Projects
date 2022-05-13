#Dragon Curve Generator
#Author: Mitchell Aiken

import matplotlib.pyplot as plt

print("How many times would you like to fold the paper?")
f = int(input())


x = [0, 1]          #zero fold coordinates
y = [0, 0]

for t in range (f): #t starts at 0, this runs as many times as there are folds
#it must start with the current final coord and work back through for each doubling
#might be better to build each new segment and append the whole thing, might not make a difference?
    size = (2**t)     #size of current list
  
    for xt in range (2**t):
        x.append(x[-1] + (y[size - (xt + 1)] - y[size - xt])) #x always needs to be looking at the end of the list
    
    for yt in range (2**t):
        y.append(y[-1] + (x[size - yt] - x[size - (yt + 1)]))


fig, dragon = plt.subplots() #the graphs will need to be formatted square based on the size of the curve
dragon.plot(x,y);