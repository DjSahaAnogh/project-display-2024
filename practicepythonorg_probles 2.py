# Note: The practicepythonorg_probles.py file became too large, causing the code to execute slowly. 
# Therefore, I created a second part of it. 😇

# URL OF THE WEBSITE https://www.practicepython.org/

# ALL IMPORTS
import requests
from bs4 import BeautifulSoup

# 18. Decode A Web Page Two

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
responce = requests.get(url)

soup = BeautifulSoup(responce.text, "html.parser")
title = soup.title.string

article = soup.find_all("p")
x: int = 0
# for i in article:
#   x += 1
#   print(f"{x}:\n {i.get_text()}\n")

# 19.  Write a function that takes an ordered list of numbers and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

def check_list(num_list: list, num: int) -> bool:
  if num in num_list:
    return True
  else:
    return False
  
# print(check_list([1, 2, 3, 4, 5], 3))

# or

def binary_search(arr: list, target: int) -> bool:
    low: int = 0
    high: int = len(arr) - 1
    
    while low <= high:
        mid: int = (low + high) // 2 
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if low > high:
        return False
    
# print(binary_search([1, 2, 3, 4, 5], 3))

# 20. Write To A File
with open("emaple.txt", "w") as text:
    text.write("hello")