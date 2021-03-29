import parsing_credit as pc
import parsing_bl as bl

def main():
    credit = pc.parsing_credit_file()
    bl = bl.parsing_bl_pdf()
    write_invoice_packing_list(credit, bl)
    write_check(crdedit, bl)
    write_HSBC_cover(credit, bl)

if __name__ == "__main__":
    main()