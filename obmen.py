import requests
import json
from tkinter import *
from tkinter import messagebox as mb


def



'''import pprint

result=requests.get("https://v6.exchangerate-api.com/v6/571aba74e1bd586f26a2f38b/latest/USD")
data=json.loads(result.text)
p=pprint.PrettyPrinter(indent=4)

p.pprint(data)'''

window=Tk()
window.title("Курсы обмена валют")
window.geometry("360x180")

Label(text="Введите курс валюты").pack(padx=10, pady=10)

entry=Entry()
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()

