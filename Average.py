userInput = input('Input values for x & y (seperate by space): ')
x,y = (userInput.split(' '))
print('x: ', x, '\ny: ',y)
print('x + y = ', float(x)+float(y))
average = (float(x)+float(y))/2
print('average of x & y = ', average)