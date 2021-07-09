# name=input('what is your name?? ')
# print('helooo '+name)
# print(round(10.6))
# print(abs(-10.6))
# test1='this is a string'
# print(f'this is a goof thing {test1}')
# #python function
# print(len(test1))
# print(test1[:5])
# print('this is a {} good boy{}'.format(test1,test1))
# #string methods
# print(test1.capitalize())
# print(test1.upper())
# test2='this is a good thing'
# print(test2.find('this'))
# print(test2.replace('this','that'))
import datetime
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
born=input('what year you born of? ' )
print('your age is : ' + str((int(year) - int(born))) )







