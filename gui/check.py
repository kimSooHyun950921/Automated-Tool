import tkinter as tk

class makeGUI(tk.Frame):
    ROWS = 30
    COLS = 16
    def __init__(self, master, credit):
        super().__init__(master)
        self.master = master
        self.credit = credit
        
        self.check_dict = dict()
        self.make_template(self.master)

    def make_template(self, master):
        entity_list = dict()
        frame0 = tk.Frame(master=master,  borderwidth=1, height=100)
        frame1 = tk.Frame(master=master, borderwidth=1, height=100)
        frame2 = tk.Frame(master=master, borderwidth=1, height=100)

        for i in range(30):
            frame0.grid_rowconfigure(i, weight=1)
        for i in range(16):
            frame0.grid_columnconfigure(i, weight=1)

        for i in range(4):
            frame1.grid_columnconfigure(i, weight=1)

        for i in range(6):
            frame2.grid_columnconfigure(i, weight=1)            

        title = tk.Label(master=frame2, text='BILL OF EXCHANGE')
        title.grid(row=1, column=1, sticky='WE', padx=10, pady=10)

        value = 'IN THE AMOUNT OF USD 입력'
        AMOUNT_VALUE_1 = tk.StringVar(value=value)
        AMOUNT_VALUE = tk.Entry(master=frame2, width=55, textvariable=AMOUNT_VALUE_1)
        AMOUNT_VALUE.insert(0, value)
        AMOUNT_VALUE.grid(row=2, column=0, sticky='W', padx=10, pady=20)
        entity_list['A'] = AMOUNT_VALUE

        dated = tk.Label(master=frame2, text='DATED')
        dated.grid(row=2, column=1, sticky='E', padx=10, pady=10)

        value = '입력'
        DATED_VALUE_1 = tk.StringVar(value=value)
        DATED_VALUE = tk.Entry(master=frame2, width=20, textvariable=DATED_VALUE_1)
        DATED_VALUE.insert(0, value)
        DATED_VALUE.grid(row=2, column=2, sticky='WE')
        entity_list['D'] = DATED_VALUE

        LOC = tk.Label(master=frame2, text='VANCOUVER, CANADA')
        LOC.grid(row=2, column=3, sticky='W', padx=10, pady=10)


        value = self.credit['CHECK_B']
        EXC_1 = tk.StringVar(value=value)
        EXC_VALUE = tk.Entry(master=frame0, width=55, textvariable=EXC_1)
        EXC_VALUE.insert(0, value)
        EXC_VALUE.grid(row=3, column=0, sticky='W', padx=10, pady=10)
        entity_list['B'] = EXC_VALUE

        PAYTO = tk.Label(master=frame0, text='PAY TO')
        PAYTO.grid(row=4, column=0, sticky='W', padx=10, pady=10)
        

        value = 'HSBC BANK OF CANADA'
        PAYTO_1 = tk.StringVar(value=value)
        PAYTO_VALUE = tk.Entry(master=frame0, width=95, textvariable=PAYTO_1)
        PAYTO_VALUE.insert(0, value)
        PAYTO_VALUE.grid(row=4, column=1, sticky='W', padx=10, pady=10)
        
        ADDITONAL = tk.Label(master=frame0, text='OR ORDER')
        ADDITONAL.grid(row=4, column=2, sticky='W', padx=10, pady=10)

        THESUMOF = tk.Label(master=frame0, text='THE SUM OF')
        THESUMOF.grid(row=5, column=0, sticky='W', padx=10, pady=10)

        value = f'입력----------------------------------------------------------'
        THESUMOF_1 = tk.StringVar(value=value)
        THESUMOF_VALUE = tk.Entry(master=frame0, width=95, textvariable=THESUMOF_1)
        THESUMOF_VALUE.insert(0, value)
        THESUMOF_VALUE.grid(row=5, column=1, sticky='W', padx=10, pady=10)
        entity_list['C'] = THESUMOF_VALUE

        value = '입력/100 U.S. DOLLAR'
        DOLLAR_1 = tk.StringVar(value=value)
        DOLLAR_VALUE = tk.Entry(master=frame0, width=20, textvariable=DOLLAR_1)
        DOLLAR_VALUE.insert(0, value)
        DOLLAR_VALUE.grid(row=5, column=2, sticky='W', padx=10, pady=10)
        entity_list['J'] = DOLLAR_VALUE


        text='VALUE RECEIVED AND CHARGE THE SAME TO THE ACCOUNT OF'
        VRCA = tk.Label(master=frame0, text=text)
        VRCA.grid(row=6, column=0, sticky='W', padx=10, pady=10)
        

        value = self.credit["INVOICE_A_CHECK_E"][0]
        VRCA_1 = tk.StringVar(value=value)
        VRCA_VAL1 = tk.Entry(master=frame0, width=95, textvariable=VRCA_1)
        VRCA_VAL1.insert(0, value)
        VRCA_VAL1.grid(row=6, column=1, sticky='W', padx=10, pady=10)
        entity_list['E1'] = VRCA_VAL1


        value = ''
        vrca_len = len(self.credit["INVOICE_A_CHECK_E"])
        if vrca_len >= 2:
            value = self.credit["INVOICE_A_CHECK_E"][1]
        VRCA_2 = tk.StringVar(value=value)
        VRCA_VAL2 = tk.Entry(master=frame0, width=95, textvariable=VRCA_2)
        VRCA_VAL2.insert(0, value)
        VRCA_VAL2.grid(row=7, column=1, sticky='W', padx=10, pady=10)
        entity_list['E2'] = VRCA_VAL2



        value = ''
        if vrca_len >= 3:
            value = self.credit["INVOICE_A_CHECK_E"][2]
        VRCA_3 = tk.StringVar(value=value)
        VRCA_VAL3 = tk.Entry(master=frame0, width=95, textvariable=VRCA_3)
        VRCA_VAL3.insert(0, value)
        VRCA_VAL3.grid(row=8, column=1, sticky='W', padx=10, pady=10)
        entity_list['E3'] = VRCA_VAL3


        value = ''
        if vrca_len >= 4:
            value = self.credit["INVOICE_A_CHECK_E"][3]
        VRCA_4 = tk.StringVar(value=value)
        VRCA_VAL4 = tk.Entry(master=frame0, width=95, textvariable=VRCA_4)
        VRCA_VAL4.insert(0, value)
        VRCA_VAL4.grid(row=9, column=1, sticky='W', padx=10, pady=10)
        entity_list['E4'] = VRCA_VAL4

        text='DRAWN UNDER'
        DRAWEN = tk.Label(master=frame0, text=text)
        DRAWEN.grid(row=10, column=0, sticky='W', padx=10, pady=10)
        
        

        value = self.credit['CHECK_F']
        DRAWEN_VAL1 = tk.StringVar(value=value)
        DRAWEN_VAL = tk.Entry(master=frame0, width=95, textvariable=DRAWEN_VAL1)
        DRAWEN_VAL.insert(0, value)
        DRAWEN_VAL.grid(row=10, column=1, sticky='W', padx=10, pady=10)
        entity_list['F'] = DRAWEN_VAL

        value = 'L/C NO. '+self.credit['INVOICE_M_CHECK_G']
        LCNO_1 = tk.StringVar(value=value)
        LCNO = tk.Entry(master=frame0, width=35, textvariable=LCNO_1)
        LCNO.insert(0, value)
        LCNO.grid(row=11, column=0, sticky='W', padx=10, pady=10)
        entity_list['G'] = LCNO

        dated = tk.Label(master=frame0, text='DATED')
        dated.grid(row=11, column=1, sticky='E', padx=10, pady=10)

        value = self.credit["CHECK_I"]
        DATED_VALUE_1 = tk.StringVar(value=value)
        DATED_VALUE = tk.Entry(master=frame0, width=10, textvariable=DATED_VALUE_1)
        DATED_VALUE.insert(0, value)
        DATED_VALUE.grid(row=11, column=2, sticky='W', padx=10, pady=10)
        entity_list['I'] = DATED_VALUE

        TO = tk.Label(master=frame0, text='TO')
        TO.grid(row=12, column=0, sticky='W', padx=10, pady=10)

        len_to = len(self.credit['CHECK_H'])
        value = self.credit['CHECK_H'][0]
        TO_1 = tk.StringVar(value=value)
        TO_VALUE1 = tk.Entry(master=frame0, width=55, textvariable=TO_1)
        TO_VALUE1.insert(0, value)
        TO_VALUE1.grid(row=12, column=1, sticky='W', padx=10, pady=10)
        entity_list['H1'] = TO_VALUE1

        value = ''
        if len_to >= 2:
            value = self.credit['CHECK_H'][1]
        TO_2 = tk.StringVar(value=value)
        TO_VALUE2 = tk.Entry(master=frame0, width=55, textvariable=TO_2)
        TO_VALUE2.insert(0, value)
        TO_VALUE2.grid(row=13, column=1, sticky='W', padx=10, pady=10)
        entity_list['H2'] = TO_VALUE2

        value = ''
        if len_to >= 3:
            value = self.credit['CHECK_H'][2]
        TO_3 = tk.StringVar(value=value)
        TO_VALUE3 = tk.Entry(master=frame0, width=55, textvariable=TO_3)
        TO_VALUE3.insert(0, value)
        TO_VALUE3.grid(row=14, column=1, sticky='W', padx=10, pady=10)
        entity_list['H3'] = TO_VALUE3

        value = ''
        if len_to >= 4:
            value = self.credit['CHECK_H'][3]
        TO_4 = tk.StringVar(value=value)
        TO_VALUE4 = tk.Entry(master=frame0, width=55, textvariable=TO_4)
        TO_VALUE4.insert(0, value)
        TO_VALUE4.grid(row=15, column=1, sticky='W', padx=10, pady=10)
        entity_list['H4'] = TO_VALUE4

        YLLTD = tk.Label(master=frame0, text='Y.L. FOREST TRADING LTD.')
        YLLTD.grid(row=15, column=5, sticky='W', padx=10, pady=20)

        OKBUTTON = tk.Button(master=frame1,  width = '35',
                            command=lambda: self.get_value(entity_list),
                            text='OK')
        OKBUTTON.grid(row=0, column=3, sticky='NE', 
                      pady=10, padx=10)

        CANCELBUTTON = tk.Button(master=frame1,  width = '35', 
                                 command=exit, text='Cancel')
        CANCELBUTTON.grid(row=0, column=4, sticky='NE', pady=10, padx=10)
        
        frame2.pack(fill=tk.X, side=tk.TOP)
        frame0.pack()
        frame1.pack(fill=tk.X, side=tk.BOTTOM)

    def get_value(self, entity_list):
        for key, value in entity_list.items():
            self.check_dict[key] = value.get()
            #print(value.get())
        self.master.quit()


def main(credit):
    root = tk.Tk()
    gui = makeGUI(root, credit)
    print(credit)
    print(credit['CHECK_B'])
    gui.master.title("Invoice Packing List")
    gui.master.minsize(1000, 650)
    gui.mainloop()
    return gui.check_dict


if __name__ == "__main__":
    main({'INVOICE_M_CHECK_G': 'M04FB2011NU00395', 'INVOICE_A_CHECK_E': ['HYOLIM TIMBER CO.,LTD.', '25-333,23,BANGCHUK-RO,83 BEON-', 'GIL,DONG-GU,INCHEON, SOUTH KOREA'], 'INVOICE_G': 'COUNTRY OF ORIGIN : CANADA', 'INVOICE_H': 'CANADIAN ROUND LOGS', 'INVOICE_J': 'PRICE TERMS : CFR SOUTH KOREAN PORT(S)', 'CHECK_B': 'AT 180  DAYS AFTER SIGHT OF THIS BILL OF EXCHANGE', 'CHECK_H': ['STANDARD CHARTERED BANK NEW YORK', '1095 AVENUE OF THE AMERICAS', 'NEW YORK UNITED STATES OF AMERICA'], 'CHECK_F': 'INDUSTRIAL BANK OF KOREA, SEOUL, LETTER OF CREDIT NO. M04FB2011NU00395 DATED 2020-11-10 ', 'CHECK_I': '10-NOV-20'},
   )