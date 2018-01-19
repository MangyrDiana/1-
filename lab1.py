# импорт модуля
import requests
import re

r = requests.get('http://www.tsu.ru/education/faculties/')
code=r.text

'''\w - любая буква,цифра и _
  + - 1 или более вхождений символа в строку
  . - любой символ, кроме новой строки \n'''
reg = "[\w.]+@\w+\.\w+" # регулярное выражение, которое находит в тексте адреса
emails = re.findall(reg, code) # возвращает список найденных фрагментов
emails = set(emails) # множество эл. адресов без повторений
print(emails) # вывод
print(len(emails))