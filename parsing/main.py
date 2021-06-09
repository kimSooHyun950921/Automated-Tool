import parsing.parsing_credit as pc
import parsing.parsing_bl as bl

def main(credit_path, bl_path):
    pc_dict, bl_dict = dict(), dict()
    credit = pc.ParsingCredit(credit_path)
    pc_dict["INVOICE_M_CHECK_G"] = credit.get_20DC()
    pc_dict["INVOICE_A_CHECK_E"] = credit.get_50APPLICANT()
    pc_dict["INVOICE_G"] =  credit.get_COUNTRYORIGIN()
    pc_dict["INVOICE_H"] = credit.get_LOGS()
    pc_dict["INVOICE_J"] = credit.get_TERMSPRICE()
    pc_dict["CHECK_B"] = credit.get_42C()
    pc_dict["CHECK_H"] = credit.get_42A()
    pc_dict["CHECK_F"] = credit.get_drawn()
    pc_dict["CHECK_I"] = credit.get_31()


    bls = bl.ParsingBl(bl_path)
    bl_dict["INVOICE_D"] = bls.get_VS()
    bl_dict["INVOICE_POL"] = bls.get_POL()
    bl_dict["INVOICE_POD"] = bls.get_POD()
    bl_dict["INVOICE_HSCODE"] = bls.get_hc()
    #write_invoice_packing_list(credit, bl)
    #write_check(crdedit, bl)
    #write_HSBC_cover(credit, bl)
    return pc_dict, bl_dict

if __name__ == "__main__":
    main()