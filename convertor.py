from customtkinter import *
from currency_converter import CurrencyConverter

class Convertor:

    def __init__(self, root):
        self.frameMenu = CTkFrame(root, width=170, height=370, fg_color='#4b5666')
        self.frameMenu.place(x=10, y=15)

        self.labelMenu = CTkLabel(self.frameMenu, text='Menu', fg_color='transparent', text_color='white',
                                  font=('Arial', 30, 'bold'))
        self.labelMenu.place(x=45, y=40)

        self.btnConvertor = CTkButton(self.frameMenu, text='Сurrency converter', fg_color='transparent',
                                      border_width=3, border_color='#343a45', font=('Arial', 14, 'bold'))
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
        self.comboCurrency1 = CTkComboBox(self.frameMain, values=self.currency)
        self.comboCurrency1.set(self.currency[0])
        self.comboCurrency1.place(x=40, y=120)

        self.btnSwapCurrency = (CTkButton(self.frameMain, text='🔁', width=5, height=15, font=(None, 20),
                                         fg_color='#4b5666', hover_color='#4b5666', command=self.swap))
        self.btnSwapCurrency.place(x=187, y=120)

        self.comboCurrency2 = CTkComboBox(self.frameMain, values=self.currency)
        self.comboCurrency2.set(self.currency[1])
        self.comboCurrency2.place(x=230, y=120)

        self.entry1 = (CTkEntry(self.frameMain, text_color='white', height=90,  border_color='#55557a',
                                border_width=4))
        self.entry1.place(x=40, y=170)

        self.entry2 = CTkEntry(self.frameMain, text_color='white', height=90, border_color='#55557a',
                               border_width=4)
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


root = CTk()

CTk.configure(root, fg_color='#56647a')
root.geometry('650x400')
root.title('Сurrency Сonverter')
convertor = Convertor(root)

root.mainloop()