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
# age=input('whats your age?? ')
# def checkDriverAge(age):
#     if int(age) < 18:
# 	    print("Sorry, you are too young to drive this car. Powering off")
#     elif int(age) > 18:
# 	    print("Powering On. Enjoy the ride!");
#     elif int(age) == 18:
# 	    print("Congratulations on your first year of driving. Enjoy the ride!")
#     return age
# if int(age) is True:
#     checkDriverAge(int(age))
# else:
#     checkDriverAge(0)

# def highest_even(lis):
#     list1=[]
#     for item in lis:
#         if item % 2 == 0:
#             list1.append(item)
#     return max(list1)
# print(highest_even([1,2,3,4,5,6]))

# print 'this';

# class Test:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# player1=Test('raj',24)
# player1.hobby='football'
# print(player1.age)
# print(player1.hobby)

#Given the below class:
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
        


    
    


# # 1 Instantiate the Cat object with 3 cats
# cat1=Cat('wamik',20)
# cat2=Cat('karishma',25)
# cat3=Cat('raju',25)


# # 2 Create a function that finds the oldest cat
# def oldest_cat(*args):
#     if max(args):
#         return args.
# print(f'the  oldest cat is {oldest_cat(cat1.age,cat2.age,cat3.age)}')
    


# # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# #1 Add nother Cat
# class Suzy(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# #2 Create a list of all of the pets (create 3 cat instances from the above)
# my_cats = [Simon('Simon', 4), Sally('Sally', 21), Suzy('Suzy', 1)]

# #3 Instantiate the Pet class with all your cats
# my_pets = Pets(my_cats)

# #4 Output all of the cats singing using the my_pets instance
# my_pets.walk()

from functools import reduce

# #1 Capitalize all of the pet names and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']

# def capitalize_pet(pet):
#     return pet.capitalize()
    
# print(list(map(capitalize_pet,my_pets)))

# print(list(map(lambda pet: pet.capitalize(),my_pets)))

    




# #2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5,4,3,2,1]

# print(list(zip(my_strings,sorted(my_numbers))))






# # 3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]
# def score_above_50(score):
#     return score>50
# print(sorted(list(filter(score_above_50,scores))))
# print(sorted(list(filter(lambda score: score>50,scores))))



# # #4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
# my_numbers = [5,4,3,2,1]
# scores = [73, 20, 65, 19, 76, 100, 88]
# def accumu(acc,item):
#     return acc+item
# print(reduce(accumu,(my_numbers+scores)))
# print(reduce(lambda acc,item: acc+item,(my_numbers+scores)))

# scores = [2, 20, 65, 19, 76, 100, 88]
# print(list(map(lambda item: pow(item,2),scores)))

# a=[(1,2),(2,3)]
# print(sorted(list(map(lambda item:item[1],a))))

# mylist=[char for char in 'hello']
# mylist1=[pow(num,1) for num in range(1,100) if num%2==0]
# print(mylist1)


# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  # code here
  def wrapper(*arg,**kawrs):
      if kawrs.keys:
          return fn(*arg,**kawrs)
      else:
          break
    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)












            





    






