# import datetime
# name = input('what is your name?? ')
# print('helooo '+name)
# print(round(10.6))
# print(abs(-10.6))
# test1 = 'this is a string'
# print(f'this is a goof thing {test1}')
# # python function
# print(len(test1))
# print(test1[:5])
# print('this is a {} good boy{}'.format(test1, test1))
# # string methods
# print(test1.capitalize())
# print(test1.upper())
# test2 = 'this is a good thing'
# print(test2.find('this'))
# print(test2.replace('this', 'that'))
# currentDateTime = datetime.datetime.now()
# date = currentDateTime.date()
# year = date.strftime("%Y")
# born = input('what year you born of? ')
# print('your age is : ' + str((int(year) - int(born))))
# user_name = input('please enter your username: ')
# passward = input('please enter your passward: ')
# hidden_passward = '*' * len(passward)
# print(
#     f'the passward  for  {user_name} is {hidden_passward} and the length {len(passward)} long')
# basket = ['ball', 'bat', 'gloves']
# print(basket)
# basket.append('pad')
# print(basket)
# basket.insert(0, 'baby')
# print(basket)
# basket.pop()
# print(basket)
# basket.pop(0)
# print(basket)
# basket.remove('bat')
# print(basket)
# basket.clear()
# print(basket)
# basket = [1, 2, 3, 'wamik']
# print('wamik' in basket)
# print(basket.index(1))
# print(basket.count('wamik'))
# print(range(1, 100))
# print(list(range(1, 100, 2)))
# newlist = ' testing '.join(['wamik', 'hossain', 'raju'])
# print(newlist)
# a, *b, c = [1, 2, 5, 5, 3]
# print(a)
# print(b)
# print(c)
# dictionary = {
#     'q': 'wamik',
#     'b': 'aaaa'
# }
# print(dictionary['b'])
# print(dictionary.get('q'))
# print(dictionary.get('raj', '100'))


# test1 = False
# test2 = False
# if test1:
#     print('true')
# elif test2:
#     print('true1')
# else:
#     print('else')
# print('yes')

# is_magitian=False
# is_expart=False

# if is_magitian and is_expart:
#     print('you are eligable')
# elif is_magitian and not(is_expart):
#     print('atleast you are getting there')
# elif not(is_magitian):
#     print('you need magic')
# else:
#     print('you are not eligable')

# my_list=[1,2,3,4,5,6,7,8,9]
# sum=0
# for item in my_list:
#     sum +=item
# print(sum)

# for i,number in enumerate(list(range(100))):
#     if number==50:
#         print('index of 50 is ' + str(i))
    
    
# picture=[
#     [0,0,0,1],
#     [1,0,0,1],
#     [1,1,1,1]
# ]
# for item in picture:
    
#         for item1 in item:
            
#             if item1 == 0:
#                 print('*',end='')    
#             else:
#                 print(' ')
#         print('')

# some_list=['q','q','a','b','b']
# dublicate_list=[]
# for item in some_list:
#     if some_list.count(item)>1:
#         if item not in dublicate_list:
#             dublicate_list.append(item)

# print(dublicate_list)

# deff say_heloo():
#     print('say h')
age=input('whats your age?? ')
def checkDriverAge(age):
    if int(age) < 18:
	    print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
	    print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
	    print("Congratulations on your first year of driving. Enjoy the ride!")
    return age
if int(age) is True:
    checkDriverAge(int(age))
else:
    checkDriverAge(0)






