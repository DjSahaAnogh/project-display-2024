# URL OF THE WEBSITE https://www.practicepython.org/

# ALL IMPORTS
from datetime import datetime

# 1. Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. Note: for this exercise, 
# the expectation is that you explicitly write out the year (and therefore be out of date the next year). 

def greeting() ->None:
  try:
    name: str = input("Please enter your name: ")
    age: int = int(input("Please enter your age: "))
  except ValueError:
    print("Invalid input! Please try again.")

  current_date_time: int = datetime.now()
  year: int = current_date_time.year

  years_left: int = 100 - age
  year_100: int = year + years_left
  
  print(f"Hello! {name}, you will turn 100 in {year_100}")


# greeting()

# 2. Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

def even_or_ood() -> None:
  try:
    num: int = int(input("Enter an integer: "))
  except ValueError:
    print("Invalid input! Please try again.")
  
  if num % 2 == 0:
    print(f"The {num} is even.")
  else:
    print(f"The {num} is ood.")
  
# even_or_ood()


# 3. Take a list, say for example this one:
a: list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

def less_than_5(lis: list) ->None:
  new_lis: list = []
  lis.sort()
  for i in lis:
    if i < 5:
      new_lis.insert(-1, i)
      new_lis.sort()
    else:
      continue
  print(new_lis)


# less_than_5(a)

# 4. Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

def divisior() -> None:
  new_lis: list = []
  num: int = int(input("Please Enter an intrger: "))
  for i in range(1, num + 1):
    if num % i == 0:
      new_lis.insert(-1, i)
      new_lis.sort()
    else:
      continue
  print(new_lis)


# divisior()

# 5. Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

def overlap(lis1: list, lis2: list) -> None:
  lis1.sort()
  lis2.sort()
  new_set1: set = set(lis1)
  new_set2: set = set(lis2)
  common: set = new_set1 & new_set2
  print(list(common))


# overlap(a, b)

# 6. Ask the user for a string and print out whether this string is a palindrome or not.

def is_palindrome() -> bool:
  text: str = input("Enter your word/s: ")
  new_text: str = text[::-1]
  if new_text == text:
    return True
  else:
    return False
  
# print(is_palindrome())

# 7. Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def even_num(lis: list) -> None:
  new_lis: list = [i for i in lis if i % 2 == 0]
  print(new_lis)

even_num(a)

# 8. 