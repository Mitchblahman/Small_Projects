#Dragon Curve Generator
#Author: Mitchell Aiken

import matplotlib.pyplot as plt

print("How many times would you like to fold the paper?")
f = int(input())
   
x = [0, 1]            #zero fold coordinates
y = [0, 0]

for t in range (f):   #runs as many times as there are folds
    size = (2**t)     #size of current list
  
    for xt in range (2**t):
        x.append(x[-1] + (y[size - (xt + 1)] - y[size - xt] )) #x bases its new positions on y's going back to the origin
    
    for yt in range (2**t):
        y.append(y[-1] - (x[size - (yt + 1)] - x[size - yt] )) #y bases its new positions on x's going back to the origin

    print(str(t + 1) + '/' + str(f))     #how far along the program is

fig, ax = plt.subplots() #the graphs will need to be formatted square based on the size of the curve
ax.set_aspect('equal')    #sets square aspect ratio
ax.axis('off')
ax.plot(x, y, linewidth = .05);   #line width needs to be adjusted based on folds
#plt.savefig(str(f) + ' folds', dpi = 2400)     #saves a png with the number of folds in its name