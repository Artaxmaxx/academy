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


def update_currency_label(event):
    code = target_combobox.get()

    name = crypto[code]
    target_label.config(text=name)


crypto = {
    'BTC': 'Bitcoin',
    'ETH': 'Ethereum',
    'USDT': 'Tether',
    'BNB': 'BNB',
    'XRP': 'XRP',
    'USDC': 'USDC',
    'SOL': 'Solana',
    'TRX': 'TRON',
    'ZEC': 'Zcash',
    'HYPE': 'Hyperliquid',
    'XMR': 'Monero'

}

root = Tk()
root.title('Курс обмена криптовалют')
root.geometry('360x180')

Label(root, text='Базовая криптовалюта').pack()
base_combobox = ttk.Combobox(root, values=list(crypto.keys()))
base_combobox.pack(pady=3, padx=10)
base_combobox.bind('<<ComboboxSelected>>', update_base_label)
base_label = ttk.Label()
base_label.pack()

Label(root, text='Целевая криптовалюта' ).pack(padx=10)

target_combobox = ttk.Combobox(root, values=list(crypto.keys()))
target_combobox.pack(pady=3, padx=10)
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)

target_label = ttk.Label()
target_label.pack()


Button(text='Получить курс обмена',
       command=exchange).pack(pady=10, padx=10)


root.mainloop()