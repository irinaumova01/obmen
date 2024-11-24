import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_c_label(event):
    code=combobox.get()
    name=cur[code]
    c_label.config(text=name)


def exchange():
    code=combobox.get()

    if code:
        try:
            response=requests.get("https://v6.exchangerate-api.com/v6/571aba74e1bd586f26a2f38b/latest/USD")
            response.raise_for_status()
            data=response.json()
            if code in data["conversion_rates"]:
                exchange_rate=data["conversion_rates"][code]
                c_name=cur[code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {c_name} за 1 доллар")
            else:
                mb.showerror("Ошибка!", f"Валюта {code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}")
    else:
        mb.showwarning("Внимание!", "Введите код валюты!")



'''import pprint

result=requests.get("https://v6.exchangerate-api.com/v6/571aba74e1bd586f26a2f38b/latest/USD")
data=json.loads(result.text)
p=pprint.PrettyPrinter(indent=4)

p.pprint(data)'''

cur={
    "RUB": "Российский рубль",
    "EUR": "Евро",
    "GBR": "Британский фунт стерлингов",
    "JPY": "Японская йена",
    "CNY": "Китайский юань",
    "KZT": "Казахский тенге",
    "UZS": "Узбекский сун",
    "CHF": "Швейцарский франк",
    "AED": "Дирхам ОАЭ",
    "CAD": "Канадский доллар"
}

window=Tk()
window.title("Курсы обмена валют")
window.geometry("360x180")

Label(text="Выберите код валюты").pack(padx=10, pady=10)
#cur=["RUB", "EUR", "GBR", "JPY", "CNY", "KZT", "UZS", "CHF", "AED", "CAD"]
combobox=ttk.Combobox(values=list(cur.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind("<<ComboboxSelected>>", update_c_label)

'''entry=Entry()
entry.pack(padx=10, pady=10)'''

c_label=ttk.Label()
c_label.pack(padx=10, pady=10)


Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()

