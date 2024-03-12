from customtkinter import *
from currency_converter import CurrencyConverter
from tkinter import messagebox


class Convertor:
    def __init__(self, root):
        self.frameMenu = CTkFrame(root, width=170, height=370, fg_color='#4b5666')
        self.frameMenu.place(x=10, y=15)

        self.labelMenu = CTkLabel(self.frameMenu, text='Menu', fg_color='transparent', text_color='white',
                                  font=('Arial', 30, 'bold'))
        self.labelMenu.place(x=45, y=40)

        self.btnConvertor = CTkButton(self.frameMenu, text='Сurrency converter', fg_color='transparent',
                                      border_width=3, border_color='#343a45', font=('Arial', 14, 'bold'), command=self.currencyConverter)
        self.btnConvertor.place(x=10, y=100)

        self.btnBuySell = CTkButton(self.frameMenu, text='Buy/Sell currency', fg_color='transparent',
                                      border_width=3, border_color='#343a45', font=('Arial', 14, 'bold'), command=self.buySell)
        self.btnBuySell.place(x=15, y=150)

        self.btnExit = CTkButton(self.frameMenu, text='Exit'
                                    ,font=('Arial', 14, 'bold'), command=root.destroy)
        self.btnExit.place(x=15, y=330)

        self.frameMain = CTkFrame(root, width=420, height=370, fg_color='#4b5666')
        self.frameMain.place(x=200, y=15)

        self.mainLabel = CTkLabel(self.frameMain, text='Converter', fg_color='transparent', text_color='white',
                                  font=('Arial', 30, 'bold'))
        self.mainLabel.place(x=130, y=50)

        self.currency = ['USD', 'EUR', 'PLN', 'GBP', 'TRY', 'CZK']
        self.comboCurrency1 = CTkComboBox(self.frameMain, values=self.currency, state='readonly')
        self.comboCurrency1.set(self.currency[0])
        self.comboCurrency1.place(x=40, y=120)

        self.btnSwapCurrency = (CTkButton(self.frameMain, text='🔁', width=5, height=15, font=(None, 20),
                                         fg_color='#4b5666', hover_color='#4b5666', command=self.swap))
        self.btnSwapCurrency.place(x=187, y=120)

        self.comboCurrency2 = CTkComboBox(self.frameMain, values=self.currency, state='readonly')
        self.comboCurrency2.set(self.currency[1])
        self.comboCurrency2.place(x=230, y=120)

        self.entry1 = (CTkEntry(self.frameMain, text_color='white', height=90))
        self.entry1.place(x=40, y=170)

        self.entry2 = CTkEntry(self.frameMain, text_color='white', height=90)
        self.entry2.place(x=230, y=170)
        self.entry2.configure(state='disabled')


        self.btnResult = CTkButton(self.frameMain, text='Convert', text_color='white', fg_color='#1f2329',
                                   command=self.convert)
        self.btnResult.place(x=130, y=300)

    def convert(self):
        self.entry2.configure(state='normal')
        self.entry2.delete('0', 'end')
        countCurrent = float(self.entry1.get())
        converter = CurrencyConverter()
        current1 = self.comboCurrency1.get()
        current2 = self.comboCurrency2.get()
        res = converter.convert(countCurrent, current1, current2)
        self.entry2.insert('end', res)
        self.entry2.configure(state='disabled')

    def swap(self):

        current1 = self.comboCurrency1.get()
        current2 = self.comboCurrency2.get()

        indexCurrency1 = self.currency.index(current1)
        indexCurrency2 = self.currency.index(current2)

        self.comboCurrency1.set(self.currency[indexCurrency2])
        self.comboCurrency2.set(self.currency[indexCurrency1])

    def buySell(self):
        self.entry1.place_forget()
        self.entry2.place_forget()
        self.comboCurrency1.place_forget()
        self.btnResult.place_forget()
        self.comboCurrency2.place_forget()
        self.mainLabel.place_forget()
        self.btnSwapCurrency.place_forget()
        self.labelBuySell = CTkLabel(self.frameMain, text='Buy/Sell', fg_color='transparent', text_color='white',
                                     font=(None, 30, 'bold'))
        self.labelBuySell.place(x=140, y=20)

        self.framePrice = CTkFrame(self.frameMain, width=250, height=180,
                                   fg_color='transparent', border_width=3, border_color='black')
        self.framePrice.place(x=75, y=70)

        self.labelInfo1 = CTkLabel(self.framePrice, text='Валюта', fg_color='transparent', font=(None, 18, 'bold'))
        self.labelInfo1.place(x=8, y=10)
        self.frameRozdil = CTkFrame(self.framePrice, border_width=2, width=5, height=180, border_color='black')
        self.frameRozdil.place(x=80, y=0)

        self.labelInfo2 = CTkLabel(self.framePrice, text='Купівля', fg_color='transparent', font=(None, 18, 'bold'))
        self.labelInfo2.place(x=90, y=10)
        self.frameRozdil2 = CTkFrame(self.framePrice, border_width=2, width=5, height=180, border_color='black')
        self.frameRozdil2.place(x=160, y=0)

        self.labelInfo3 = CTkLabel(self.framePrice, text='Продаж', fg_color='transparent', font=(None, 18, 'bold'))
        self.labelInfo3.place(x=170, y=10)

        self.labelCurrent = CTkLabel(self.framePrice, text='USD\nEUR\nPLN\nTRY\nGBP', font=(None, 18, 'bold'))
        self.labelCurrent.place(x=20, y=50)

        self.priceCurrent = [

            38.1148,
            41.5862,
            9.4837,
            2.8637,
            49.2140

        ]
        self.priceCurrent2 = [

            37.1148,
            40.5862,
            8.4837,
            1.8637,
            48.2140

        ]
        self.labelBuyCurrent = CTkLabel(self.framePrice, text=f'{self.priceCurrent[0]}'
                                                                f'\n{self.priceCurrent[1]}'
                                                                f'\n{self.priceCurrent[2]}'
                                                                f'\n{self.priceCurrent[3]}'
                                                                f'\n{self.priceCurrent[4]}', font=(None, 18, 'bold'))
        self.labelBuyCurrent.place(x=90, y=50)

        self.labelSellCurrent = CTkLabel(self.framePrice, text=f'{self.priceCurrent2[0]}'
                                                              f'\n{self.priceCurrent2[1]}'
                                                              f'\n{self.priceCurrent2[2]}'
                                                              f'\n{self.priceCurrent2[3]}'
                                                              f'\n{self.priceCurrent2[4]}', font=(None, 18, 'bold'))
        self.labelSellCurrent.place(x=170, y=50)

        self.labelInfoCurrentUser = CTkLabel(self.frameMain, text='Виберіть валюту: ')
        self.labelInfoCurrentUser.place(x=80, y=260)
        val = ['USD', 'EUR', 'PLN', 'TRY', 'GBP']
        self.comboCurrent = CTkComboBox(self.frameMain, values=val, state='readonly')
        self.comboCurrent.set(val[0])
        self.comboCurrent.place(x=190, y=260)

        self.infoCountCurrentUser = CTkLabel(self.frameMain, text='Введіть кількість: ')
        self.infoCountCurrentUser.place(x=80, y=300)
        self.entryCountCurrentUser = CTkEntry(self.frameMain)
        self.entryCountCurrentUser.place(x=190, y=300)

        self.btnBuy = CTkButton(self.frameMain, text='Buy', command=self.buy)
        self.btnBuy.place(x=60, y=340)
        self.btnSell = CTkButton(self.frameMain, text='Sell', command=self.sell)
        self.btnSell.place(x=210, y=340)

    def buy(self):
        try:
            Usd, Eur, Pln, Try, Gbp = 37.1148, 40.5862, 8.4837, 1.8637, 48.2140
            count = float(self.entryCountCurrentUser.get())
            current = self.comboCurrent.get()
            res = 0
            if current == 'USD':
                res = count * Usd
                mess = messagebox.askokcancel('Придбати валюту', f'Ви бажаєте придбати USD на суму: {res}')
            elif current == 'EUR':
                res = count * Eur
                mess = messagebox.askokcancel('Придбати валюту', f'Ви бажаєте придбати EUR на суму: {res}')
            elif current == 'PLN':
                res = count * Pln
                mess = messagebox.askokcancel('Придбати валюту', f'Ви бажаєте придбати PLN на суму: {res}')
            elif current == 'TRY':
                res = count * Try
                mess = messagebox.askokcancel('Придбати валюту', f'Ви бажаєте придбати TRY на суму: {res}')
            elif current == 'GBP':
                res = count * Gbp
                mess = messagebox.askokcancel('Придбати валюту', f'Ви бажаєте придбати GBP на суму: {res}')
            if mess == True:
                messagebox.showinfo('Придбано', 'Успішно')
            else:
                messagebox.showinfo('Не придбано', 'Операція скасованна')
        except ValueError:
            pass

    def sell(self):
        try:
            Usd, Eur, Pln, Try, Gbp = 37.1148, 40.5862, 8.4837, 1.8637, 48.2140
            count = float(self.entryCountCurrentUser.get())
            current = self.comboCurrent.get()
            res = 0
            if current == 'USD':
                res = count * Usd
                mess = messagebox.askokcancel('Продати валюту', f'Ви бажаєте продати USD на суму: {res}')
            elif current == 'EUR':
                res = count * Eur
                mess = messagebox.askokcancel('Продати валюту', f'Ви бажаєте продати EUR на суму: {res}')
            elif current == 'PLN':
                res = count * Pln
                mess = messagebox.askokcancel('Продати валюту', f'Ви бажаєте продати PLN на суму: {res}')
            elif current == 'TRY':
                res = count * Try
                mess = messagebox.askokcancel('Продати валюту', f'Ви бажаєте продати TRY на суму: {res}')
            elif current == 'GBP':
                res = count * Gbp
                mess = messagebox.askokcancel('Продати валюту', f'Ви бажаєте продати GPB на суму: {res}')
            if mess == True:
                messagebox.showinfo('Продано', 'Успішно')
            else:
                messagebox.showinfo('Не продано', 'Операція скасованна')
        except ValueError:
            pass

    def currencyConverter(self):
        try:
            self.labelBuySell.place_forget()
            self.framePrice.place_forget()
            self.labelInfo1.place_forget()
            self.frameRozdil.place_forget()
            self.labelInfo2.place_forget()
            self.frameRozdil2.place_forget()
            self.labelInfo3.place_forget()
            self.labelCurrent.place_forget()
            self.labelBuyCurrent.place_forget()
            self.labelSellCurrent.place_forget()
            self.labelInfoCurrentUser.place_forget()
            self.comboCurrent.place_forget()
            self.infoCountCurrentUser.place_forget()
            self.entryCountCurrentUser.place_forget()
            self.btnBuy.place_forget()
            self.btnSell.place_forget()
            self.mainLabel.place(x=130, y=50)

            self.comboCurrency1.place(x=40, y=120)
            self.btnSwapCurrency.place(x=187, y=120)
            self.comboCurrency2.place(x=230, y=120)
            self.entry1.place(x=40, y=170)
            self.entry2.place(x=230, y=170)
            self.entry2.configure(state='disabled')
            self.btnResult.place(x=130, y=300)
        except AttributeError:
            pass


root = CTk()

CTk.configure(root, fg_color='#56647a')
root.geometry('650x400')
root.resizable(width=False, height=False)
root.title('Сurrency Сonverter')
convertor = Convertor(root)

root.mainloop()
