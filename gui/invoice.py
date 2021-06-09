import tkinter as tk
import tk_tools

class makeGUI(tk.Frame):
    ROWS = 54
    COLS = 12
    def __init__(self, master, credit, bl):
        super().__init__(master)
        self.master = master
        self.credit = credit
        self.bl = bl
        
        self.invoice_dict = dict()
        self.make_template(self.master)

    def make_template(self, master):
        entity_list = dict()
        frame0 = tk.Frame(master=master,  borderwidth=1, height=100)
        frame1 = tk.Frame(master=master,  borderwidth=1,width=500)
        frame2 = tk.Frame(master=master, borderwidth=1 ,width=500)
        frame3 = tk.Frame(master=master, borderwidth=1,height=200, width=100)
        frame4 = tk.Frame(master=master, borderwidth=1, height=200)
        frame5 = tk.Frame(master=master, borderwidth=1, height=200)
        frame6 = tk.Frame(master=master, borderwidth=1, height=200)
        frame7 = tk.Frame(master=master, borderwidth=1, height=100)

        for i in range(10):
            frame0.grid_columnconfigure(i, weight=1)

        for i in range(2):
            frame5.grid_rowconfigure(i, weight=1)
        for i in range(10):
            frame5.grid_columnconfigure(i, weight=1)

        for i in range(1):
            frame4.grid_rowconfigure(i, weight=1)
        for i in range(10):
            frame4.grid_columnconfigure(i, weight=1)

        for i in range(10):
            frame7.grid_columnconfigure(i, weight=1)
        
        title = tk.Label(master=frame0, text='Original\nPackinglist')
        title.grid(row=8, column=5, sticky='NW')

        SOLDTO = tk.Label(master=frame1, width=12, text='SOLD TO:')
        SOLDTO.grid(row=13, column=0, sticky='W', pady=10, padx=10)
        print(self.credit["INVOICE_A_CHECK_E"][0])
        SOLDTO_VALUE_1 = tk.StringVar(value="1234")#'self.credit["INVOICE_A_CHECK_E"][0]')
        SOLDTO_VALUE_ENT1 = tk.Entry(master=frame1, width=20, textvariable=SOLDTO_VALUE_1)
        SOLDTO_VALUE_ENT1.insert(0, self.credit["INVOICE_A_CHECK_E"][0])
        SOLDTO_VALUE_ENT1.grid(row=13, column=1, sticky='WE', pady=5, padx=10)
        entity_list['A1'] = SOLDTO_VALUE_ENT1
        

        value = ''
        if len(self.credit["INVOICE_A_CHECK_E"]) >= 2:
            value = self.credit["INVOICE_A_CHECK_E"][1] 
        SOLDTO_VALUE_2 = tk.StringVar(value=value)
        SOLDTO_VALUE_ENT2 = tk.Entry(master=frame1, width=20, textvariable=SOLDTO_VALUE_2)
        SOLDTO_VALUE_ENT2.insert(0, value)
        SOLDTO_VALUE_ENT2.grid(row=14, column=1, sticky='WE', pady=5, padx=10)
        entity_list['A2'] = SOLDTO_VALUE_ENT2

        value = ''
        if len(self.credit["INVOICE_A_CHECK_E"]) >= 3:
            value = self.credit["INVOICE_A_CHECK_E"][2] 
        SOLDTO_VALUE_3 = tk.StringVar(value=value)
        SOLDTO_VALUE_ENT3 = tk.Entry(master=frame1, width=20, textvariable=SOLDTO_VALUE_3)
        SOLDTO_VALUE_ENT3.insert(0, value)
        SOLDTO_VALUE_ENT3.grid(row=15, column=1, sticky='WE', pady=5, padx=10)
        entity_list['A3'] = SOLDTO_VALUE_ENT3
        
        
        value = ''
        if len(self.credit["INVOICE_A_CHECK_E"]) >= 4:
            value = self.credit["INVOICE_A_CHECK_E"][3] 
        SOLDTO_VALUE_4 = tk.StringVar(value=value)
        SOLDTO_VALUE_ENT4 = tk.Entry(master=frame1, width=20, textvariable=SOLDTO_VALUE_4)
        SOLDTO_VALUE_ENT4.insert(0, value)
        SOLDTO_VALUE_ENT4.grid(row=16, column=1, sticky='WE', pady=5, padx=10)
        entity_list['A4'] = SOLDTO_VALUE_ENT4

        value = ''
        if len(self.credit["INVOICE_A_CHECK_E"]) >= 5:
            value = self.credit["INVOICE_A_CHECK_E"][4] 
        SOLDTO_VALUE_5 = tk.StringVar()
        SOLDTO_VALUE_ENT5 = tk.Entry(master=frame1, width=20, textvariable=SOLDTO_VALUE_5)
        SOLDTO_VALUE_ENT5.insert(0, value)
        SOLDTO_VALUE_ENT5.grid(row=17, column=1, sticky='WE', pady=5, padx=10)
        entity_list['A5'] = SOLDTO_VALUE_ENT5

        LCNO = tk.Label(master=frame1, text='L/C NO.')
        LCNO.grid(row=18, column=0, sticky='WE',padx=10)


        LCNO_VAL_1 = tk.StringVar(value=self.credit["INVOICE_M_CHECK_G"])
        LCONO_VAL = tk.Entry(master=frame1, width=20, textvariable=LCNO_VAL_1)
        LCONO_VAL.insert(0, self.credit["INVOICE_M_CHECK_G"])
        LCONO_VAL.grid(row=19, column=1, sticky='WE', pady=5, padx=10)
        entity_list['M'] = LCONO_VAL

        COO_VAL1 = tk.StringVar(value=self.credit["INVOICE_G"])
        COO_VAL = tk.Entry(master=frame1, width=30, textvariable=COO_VAL1)
        COO_VAL.insert(0, self.credit["INVOICE_G"])
        COO_VAL.grid(row=20, column=1, sticky='WE', pady=5, padx=10)
        entity_list['G'] = COO_VAL

        DATE = tk.Label(master=frame2, text='DATE:')
        DATE.grid(row=12, column=3, sticky='W', padx=10)

        #DATE_VAL = tk.Text(master=frame, width=20, height=2)
        #DATE_VAL.grid(row=12, column=5, sticky='WE', pady=1, padx=1)

        DATE_VAL1 = tk.StringVar(value="직접 입력해주세요")
        DATE_VAL = tk.Entry(master=frame2, width=30, textvariable=DATE_VAL1)
        DATE_VAL.insert(0, "직접 입력해주세요")
        DATE_VAL.grid(row=12, column=5, sticky='WE', pady=5, padx=10)
        entity_list['B'] = DATE_VAL

        INVOICENO = tk.Label(master=frame2, text='INVOICE NO.:')
        INVOICENO.grid(row=13, column=3, sticky='W', pady=10, padx=10)

        INVOICENO_VAL1 = tk.StringVar(value="직접 입력해주세요")
        INVOICENO_VAL = tk.Entry(master=frame2, width=30, textvariable=INVOICENO_VAL1)
        INVOICENO_VAL.insert(0, "직접 입력해주세요")
        INVOICENO_VAL.grid(row=13, column=5, sticky='WE', pady=5, padx=10)
        entity_list['C'] = INVOICENO_VAL

        VESSELNAME = tk.Label(master=frame2, text='VESSEL NAME')
        VESSELNAME.grid(row=14, column=3, sticky='W', pady=10, padx=10)

        value = '파싱 에러 직접 입력해주세요'
        if self.bl["INVOICE_D"]:
            value = self.bl["INVOICE_D"]
        VESSELNAME_VAL1 = tk.StringVar(value = value)
        VESSELNAME_VAL = tk.Entry(master=frame2, width=30, textvariable=VESSELNAME_VAL1)
        VESSELNAME_VAL.insert(0, value)
        VESSELNAME_VAL.grid(row=14, column=5, sticky='WE', pady=5, padx=10)
        entity_list['D'] = VESSELNAME_VAL

        PORTOFLOADING = tk.Label(master=frame2, text='PORT OF LOADING')
        PORTOFLOADING.grid(row=16, column=3, sticky='W', pady=10, padx=10)

        value = '파싱 에러 직접 입력해주세요'
        if self.bl["INVOICE_POL"]:
            value = self.bl["INVOICE_POL"]
        PORTOFLOADING_VAL1 = tk.StringVar(value=value)
        PORTOFLOADING_VAL = tk.Entry(master=frame2, width=30, textvariable=PORTOFLOADING_VAL1)
        PORTOFLOADING_VAL.insert(0, value)
        PORTOFLOADING_VAL.grid(row=16, column=5, sticky='WE', pady=5, padx=10)
        entity_list['E'] = PORTOFLOADING_VAL

        PORTOFDISCHARGE = tk.Label(master=frame2, text='PORT OF DISCHARGE')
        PORTOFDISCHARGE.grid(row=18, column=3, sticky='W', pady=10, padx=10)

        value = '파싱 에러 직접 입력해주세요'
        if self.bl["INVOICE_POD"]:
            value = self.bl["INVOICE_POD"]
        PORTOFDISCHARGE_VAL1 = tk.StringVar(value=value)
        PORTOFDISCHARGE_VAL = tk.Entry(master=frame2, width=30, textvariable=PORTOFDISCHARGE_VAL1)
        PORTOFDISCHARGE_VAL.insert(0, value)
        PORTOFDISCHARGE_VAL.grid(row=18, column=5, sticky='WE', pady=5, padx=10)
        entity_list['F'] = PORTOFDISCHARGE_VAL

        FINALDESTINATION = tk.Label(master=frame2, text='FINAL DESTINATION')
        FINALDESTINATION.grid(row=20, column=3, sticky='W', pady=10, padx=10)

  
        FINALDESTINATION_VAL1 = tk.StringVar(value=value)
        FINALDESTINATION_VAL = tk.Entry(master=frame2, width=30, textvariable=FINALDESTINATION_VAL1)
        FINALDESTINATION_VAL.insert(0, value)
        FINALDESTINATION_VAL.grid(row=20, column=5, sticky='WE', pady=5, padx=10)
        

        value = '파싱에러 직접입력해주세요'
        if self.credit["INVOICE_H"]:
            value = self.credit["INVOICE_H"]
        COMMDITY_VAL1 = tk.StringVar(value=value)
        COMMDITY_VAL = tk.Entry(master=frame6, width=30, textvariable=COMMDITY_VAL1)
        COMMDITY_VAL.insert(0, value)
        COMMDITY_VAL.grid(row=24, column=1, sticky='WE', pady=5, padx=10)
        entity_list['H'] = COMMDITY_VAL

        PIECES = tk.Label(master=frame5, text='PIECES')
        PIECES.grid(row=26, column=0, sticky='WE', pady=10, padx=10)
        

        value = '직접 입력해주세요'
        PIECES_VAL1 = tk.StringVar(value = value)
        PIECES_VAL = tk.Entry(master=frame5, width=10, textvariable=PIECES_VAL1)
        PIECES_VAL.insert(0, value)
        PIECES_VAL.grid(row=27, column=0, sticky='WE', pady=10, padx=10)
        entity_list['I'] = PIECES_VAL

        COMMODITYDESC = tk.Label(master=frame5, text='COMMODITY DESC.')
        COMMODITYDESC.grid(row=26, column=3, sticky='WE', pady=10, padx=10)

        value = '파싱에러 직접입력해주세요'
        if self.credit["INVOICE_H"]:
            value = self.credit["INVOICE_H"]
        COMMODITYDESC_VAL1 = tk.StringVar(value=value)
        COMMODITYDESC_VAL = tk.Entry(master=frame5, width=10, textvariable=COMMODITYDESC_VAL1)
        COMMODITYDESC_VAL.insert(0, value)
        COMMODITYDESC_VAL.grid(row=27, column=3, sticky='WE', pady=5, padx=10)
        
        

        MBF = tk.Label(master=frame5, text='MBF')
        MBF.grid(row=26, column=5, sticky='WE', pady=10, padx=10)

        value='직접 입력해주세요'
        MBF_VAL1 = tk.StringVar(value=value)
        MBF_VAL = tk.Entry(master=frame5, width=10, textvariable=MBF_VAL1)
        MBF_VAL.insert(0, value)
        MBF_VAL.grid(row=27, column=5, sticky='WE', pady=10, padx=10)
        entity_list['K'] = MBF_VAL

        AMOUNT = tk.Label(master=frame5, text='AMOUNT (US$)')
        AMOUNT.grid(row=26, column=7, sticky='WE', pady=10, padx=10)
        

        value='직접입력해주세요'
        AMOUNT_VAL1 = tk.StringVar(value=value)
        AMOUNT_VAL = tk.Entry(master=frame5, width=10, textvariable=AMOUNT_VAL1)
        AMOUNT_VAL.insert(0, value)
        AMOUNT_VAL.grid(row=27, column=7, sticky='WE', pady=10, padx=10)
        entity_list['N'] = AMOUNT_VAL

        value = '파싱에러 직접입력해주세요'
        if self.credit["INVOICE_J"]:
            value = self.credit["INVOICE_J"]
        GOODS_VAL1 = tk.StringVar(value=value)
        GOODS_VAL = tk.Entry(master=frame5, width=10, textvariable=GOODS_VAL1)
        GOODS_VAL.insert(0, value)
        GOODS_VAL.grid(row=29, column=3, sticky='WE', pady=10, padx=10)
        entity_list['J'] = GOODS_VAL

        
        value = '파싱에러 직접입력해주세요'
        if self.bl["INVOICE_HSCODE"]:
            value = self.credit["INVOICE_HSCODE"]
        HSCODE_VAL1 = tk.StringVar(value=value)
        HSCODE_VAL = tk.Entry(master=frame5, width=10, textvariable=HSCODE_VAL1)
        HSCODE_VAL.insert(0, value)
        HSCODE_VAL.grid(row=31, column=3, sticky='WE', pady=10, padx=10)
        entity_list['O'] = HSCODE_VAL

        
        BL_NUM_VAL1 = tk.StringVar()
        BL_NUM_VAL = tk.Entry(master=frame5, width=10, textvariable=BL_NUM_VAL1)
        BL_NUM_VAL.insert(0, value)
        BL_NUM_VAL.grid(row=33, column=3, sticky='WE', pady=10, padx=10)
        entity_list['L'] = BL_NUM_VAL

        TOTAL = tk.Label(master=frame4, text='TOTAL')
        TOTAL.grid(row=44, column=0, sticky='WE', pady=10, padx=10)


        TOTAL_VAL1 = tk.StringVar(value='PIECIES와 동일')
        TOTAL_VAL = tk.Entry(master=frame4, width=10, textvariable=TOTAL_VAL1)
        TOTAL_VAL.insert(0, 'PIECIES와 동일')
        TOTAL_VAL.grid(row=44, column=1, sticky='WE', pady=10, padx=10)

        MBF_VAL2 = tk.StringVar(value='MBF와 동일')
        MBF_VAL_R = tk.Entry(master=frame4, width=10, textvariable=MBF_VAL2)
        MBF_VAL_R.insert(0, 'MBF와 동일')
        MBF_VAL_R.grid(row=44, column=5, sticky='WE', pady=10, padx=10)

        AMOUNT_VAL2 = tk.StringVar(value='AMOUNT와 동일 (US$)')
        AMOUNT = tk.Entry(master=frame4, width=10, textvariable=AMOUNT_VAL2)
        AMOUNT.insert(0, 'AMOUNT와 동일 (US$)')
        AMOUNT.grid(row=44, column=7, sticky='WE', pady=10, padx=10)

        

        LTD = tk.Label(master=frame3, text='Y.L. FOREST TRADING LTD.')
        LTD.grid(row=54, column=8, sticky='WE', pady=10, padx=10)

        OKBUTTON = tk.Button(master=frame7,  width = '30', 
                            command=lambda: self.get_value(entity_list), text='OK')
        OKBUTTON.grid(row=55, column=9, sticky='NE', 
                      pady=10, padx=10)

        CANCELBUTTON = tk.Button(master=frame7,  width = '30', 
                                 command=exit, text='Cancel')
        CANCELBUTTON.grid(row=55, column=10, sticky='NE', pady=10, padx=10)

        frame0.pack(fill=tk.X, side=tk.TOP)
        frame7.pack(fill=tk.X, side=tk.BOTTOM)
        frame3.pack(fill=tk.X, side=tk.BOTTOM)
        frame4.pack(fill=tk.X, side=tk.BOTTOM)
        frame5.pack(fill=tk.X, side=tk.BOTTOM)
        frame6.pack(fill=tk.X, side=tk.BOTTOM)
        frame1.pack(fill=tk.Y, side=tk.LEFT)
        frame2.pack(fill=tk.Y, side=tk.LEFT)
        

    def get_value(self, entity_list):
        for key, value in entity_list.items():
            self.invoice_dict[key] = value.get()
            #print(value.get())
        self.master.quit()


def main(credit, bl):
    root = tk.Tk()
    gui = makeGUI(root, credit, bl)
    gui.master.title("Invoice Packing List")
    gui.master.minsize(700, 650)
    gui.mainloop()
    return gui.invoice_dict


#if __name__ == "__main__":
#    main({'INVOICE_M_CHECK_G': 'M04FB2011NU00395', 'INVOICE_A_CHECK_E': ['HYOLIM TIMBER CO.,LTD.', '25-333,23,BANGCHUK-RO,83 BEON-', 'GIL,DONG-GU,INCHEON, SOUTH KOREA'], 'INVOICE_G': 'COUNTRY OF ORIGIN : CANADA', 'INVOICE_H': 'CANADIAN ROUND LOGS', 'INVOICE_J': 'PRICE TERMS : CFR SOUTH KOREAN PORT(S)', 'CHECK_B': 'AT 180  DAYS AFTER SIGHT OF THIS BILL OF EXCHANGE', 'CHCECK_H': ['STANDARD CHARTERED BANK NEW YORK', '1095 AVENUE OF THE AMERICAS', 'NEW YORK UNITED STATES OF AMERICA'], 'CHECK_F_1': 'INDUSTRIAL BANK OF KOREA', 'CHECK_F_2': 'INDUSTRIAL BANK OF KOREA, SEOUL, LETTER OF CREDIT NO. M04FB2011NU00395 DATED 2020-11-10 ', 'CHECK_C': '10-NOV-20'},
#    {'INVOICE_D': 'M.V. SANDY BAY', 'INVOICE_POL': 'NANAIMO, BC, CANADA', 'INVOICE_POD': 
#'INCHON SOUTH KOREA PORT', 'INVOICE_HSCODE': None})