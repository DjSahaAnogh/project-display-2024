# URL OF THE WEBSITE https://www.practicepython.org/

# ALL IMPORTS
from datetime import datetime
import random
import string
import requests
from bs4 import BeautifulSoup


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

# even_num(a)

# 8. Make a two-player Rock-Paper-Scissors game. 
def rock_paper_scissors() -> None:
  while True:
    option: list = ["rock", "paper", "scissors"]
    user_responce: str = input("Choose a symbol(rock, paper, scissors): ").lower()
    computer_responce: str = random.choice(option)

    # checking
    if user_responce in option:
      pass
    else:
      print('Invaild input, please try again!')
      rock_paper_scissors()
    
    # game
    if user_responce == computer_responce:
      print("It is a tie")
      break
    elif (user_responce == "rock" and computer_responce == "scissors") or (user_responce == "scissors" and computer_responce == "paper") or (user_responce == "paper" and computer_responce == "rock"):
      print("You won!")
      break
    else:
      print("Computer won!")
      break
  if input("Do you want to play again? If yes enter 'y' \nor enter any key: "). lower() == "y":
    rock_paper_scissors()

# rock_paper_scissors()

# 9. Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

def guess_game() -> None:
  num: int = random.randint(1, 9)
  while True:
    try:
      user_responce: int = int(input("Guess the number: "))
    except ValueError:
      print("Invaild input, please try again!")
      guess_game()
    

    if user_responce > num:
      print("too high")
    elif user_responce < num:
      print("too low")
    else:
      print("Congratulations! You won!")
      break
  
  if input("Do you want to play again? If yes enter 'y' \nor enter any key: "). lower() == "y":
    guess_game()


# guess_game()

# 10. Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).

def overlap2(lis1: list, lis2: list) -> list:
  lis1.sort()
  set1: set = set(lis1)
  lis2.sort()
  set2: set = set(lis2)
  new_lis1: list = list(set1)
  new_lis2: list = list(set2)
  overlap: list = [x for x in new_lis1 for y in new_lis2 if x == y]
  return overlap

# print(overlap2(a, b))

# 11. Ask the user for a number and determine whether the number is prime or not.

def is_prime(num:list) -> bool:
  divisior_lis: list = [x for x in range(1, num+1) if num % x == 0]
  if len(divisior_lis) == 2:
    return True
  else:
    return False

# print(is_prime(4))

# 12. Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.

p = [5, 10, 15, 20, 25]
def list_end(lis: list) -> None:
  new_lis = [lis[i] for i in (0, -1)]
  print(new_lis)

# list_end(p)

# 13. Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.

def fibonnaci_v01(num: int) -> None:
  num1: int = 0
  num2: int = 1
  i: int = 0
  while num != i:
    num1, num2 = num2, num1+num2
    print(num1)
    i += 1

# fibonnaci_v01(5)

# or

def fibonnaci_v02() -> None:
  while True:
    try:
      num_of_term: int = int(input("Please enter the number of terms of Fibonnaci sequence: "))
    except ValueError:
      print("Invalid input, please try again.")
    
    num1: int = 0
    num2: int = 1

    while num_of_term:
      num1, num2 = num2, num1+num2
      print(num1)
      num_of_term -= 1
    
    if num_of_term == 0:
      break
    else:
      continue

# fibonnaci_v02()

# 14. Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.

def backward_order() -> None:
  text: str = input("Plear provide a text: ")
  lis: list = text.split(" ")
  new_lis: list = lis[::-1]
  new_str: str = " ".join(new_lis)
  print(new_str)


# backward_order()

# 15. Password Generator

def password_generator() -> str:
  lis_symbol: list = ["#", "@", "!", "%", "&", "$", "/", "\\"]
  uppercase_letter: str = random.choice(string.ascii_uppercase)
  lowercase_letter: str = random.choice(string.ascii_lowercase)
  num: str = str(random.randint(1, 10))
  symbol: str = random.choice(lis_symbol)
  password_lis: list = [uppercase_letter, lowercase_letter, num, symbol]
  random.shuffle(password_lis)
  password: str = "".join(password_lis)
  return password

# print(password_generator())

# 16. Decode a web page

# url: str = "https://aniwatchtv.to/blue-exorcist-1198?ref=search"
# responce = requests.get(url)

# html = responce.text

# soup = BeautifulSoup(html, "html.parser")
# print(soup.title.string)

# headings = soup.find_all("h2")
# for i, heading in enumerate(headings):
#   print(f"{i+1}: {heading.text.strip()}")

# 17. Cows And Bulls

def get_secret_num() -> str:
  secret_num: list = random.sample(range(10), 4)
  return str(secret_num)

def get_user_guess() -> str:
  while True:
    guess = input("Enter your guess (4 unique digits): ")
    if len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4:
      return guess
    print("Invalid input. Please enter 4 unique digits.")

def calculate_cows_and_bulls(secret, guess) -> set:
    cows = sum(1 for s, g in zip(secret, guess) if s == g)
    cow_hint = [x for i, x in enumerate(secret) if i < len(guess) and x == guess[i]]
    bulls = sum(1 for g in guess if g in secret)
    bull_hint = [x for x in guess if x in secret]
    return cows, bulls, cow_hint, bull_hint

def game_play() -> None:
  attempts: int = 0
  max_attempts: int = 10
  secret: str = get_secret_num()
  
  print("Welcome to the cows and bulls game.\n Please guess the 4 digits. You have 10 attempts.")
  
  while attempts < max_attempts:
    attempts += 1
    cows, bulls, cow_hints, bull_hints = calculate_cows_and_bulls(secret, get_user_guess())
    print(f"Cows: {cows}, Bulls: {bulls}, No. of attempts {attempts}. Hint for cow {cow_hints}, for bull {bull_hints}")

    if cows == 4:
      print(f"Congratulation you won the game in {attempts} attempts")
      break
  else:
    print(f"Sorry! You've used all attempts. The secret number was {secret}.")

# if __name__ == "__main__":
#   game_play()