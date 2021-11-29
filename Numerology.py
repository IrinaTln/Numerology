from module1 import *

dictionary=main("info.txt")

while True:
  
    name=input("Введите имя для анализа на русском языке: ").lower()
    numerology_magic=get_name_number(dictionary, name)
