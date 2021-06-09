import os
import gui.main as gm
import gui.check as gc
import gui.invoice as gi

import parsing.main as pmain

import write.write_invoice_packing_list as wipl
import write.write_check as wc


def start_program():
    credit_path, bl_path, excel_path, filename, program_path = gm.gui_main()
    

    if credit_path != '' and bl_path != '' and excel_path != '':
        pc_dict, bl_dict = pmain.main(credit_path, bl_path)
        invoice_value = gi.main(pc_dict, bl_dict)
        print(invoice_value)
        wipl.main(invoice_value, os.path.join(excel_path,f'invoice_{filename}.xls'), program_path)
        check_value = gc.main(pc_dict)
        print(check_value)
        wc.main(check_value, os.path.join(excel_path,f'BE_{filename}.xls'),program_path)


start_program()