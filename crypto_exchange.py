from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests
import json
import pprint


def update_base_label(event):
    code = base_combobox.get()
    name = crypto[code]
    base_label.config(text=name)


def exchange():
    base_code = base_combobox.get().strip()
    if base_code:
        try:
            response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={base_code}&vs_currencies=usd')
            response.raise_for_status()
            data = response.json()
            if data:
                base = crypto[base_code]
                mb.showinfo('Курс обмена',
                            f'Курс: {data[base_code]["usd"]} долларов США за 1 {base}')
            else:
                mb.showerror('Ошибка',
                            f'Криптовалюта {base_code} не найдена')
        except Exception as er:
            mb.showerror('Ошибка', er)

    else:
        mb.showwarning('Внимание', 'Введите код криптовалюты')


crypto = {
    'bitcoin': 'Bitcoin',
    'ethereum': 'Ethereum',
    'tether': 'Tether',
    'binancecoin': 'BNB',
    'ripple': 'XRP',
    'usd-coin': 'USDC',
    'solana': 'Solana',
    'tron': 'TRON',
    'zcash': 'Zcash',
    'hyperliquid': 'Hyperliquid',
    'monero': 'Monero'
}

root = Tk()
root.title('Курс обмена криптовалют')
root.geometry('360x120')

Label(root, text='Выберите криптовалюту').pack()

base_combobox = ttk.Combobox(root, values=list(crypto.keys()))
base_combobox.pack(pady=3, padx=10)
base_combobox.bind('<<ComboboxSelected>>', update_base_label)

base_label = ttk.Label()
base_label.pack()

Button(text='Получить курс обмена',
       command=exchange).pack(pady=10, padx=10)


root.mainloop()