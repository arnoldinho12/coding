print('Hello Chucky Cheese!')
selection = input('Please type in your selection [1 - 12]:')
selection = int(selection)

#Defining and Developing Functions for Selection Process below
x = 'Aye no mames!!'
def option1_function():
    print('-------------------')
    print('Welcome to Addition')
    print('-------------------')
    num1 = input("Please enter a number: ")
    num1 = float(num1)
    num2 = input("Please enter a number: ")
    num2 = float(num2)
    total = num1 + num2
    print('The sum of {0} and {1} is {2}'.format(num1,num2,total))

def option2_function():
    print('-----------------------')
    print('Welcome to Square Root')
    print('-----------------------')
    num = input("Please enter a number: ")
    num = float(num)
    num_sqrt = num ** 0.5
    print('The square root of %0.2f is %0.2f'%(num ,num_sqrt))

if selection == 1:
    option1_function()
elif selection ==2:
    option2_function()
else:
    print('Sorry! Have a nice day!')
    print(x)


option1_function()
option2_function()
