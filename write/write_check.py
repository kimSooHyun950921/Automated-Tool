
import shutil
import os
import csv
import xlrd
import xlwt

from collections import defaultdict
from xlutils.copy import copy
from write.num_to_eng import change_value as nte
INVOICE = 'template/check_template.xls'
INVOICE_INFO = 'template/check_info.csv'


def copy_from_template(templatepath, output):
    #temp_path = os.getcwd()
    print("PATH", os.path.join(templatepath, INVOICE))
    shutil.copy(os.path.join(templatepath, INVOICE), output.replace('output','copy'))


def is_image(idx):
    if (idx >= 0 and idx <= 6) or (idx > 60 and idx <= 65):
        return True
    return False


def change_file(output, csv_info, invoice_val):
    workbook = xlrd.open_workbook( output.replace('output','copy'), formatting_info=True)
    wb = copy(workbook)
    boldstyle = xlwt.easyxf('font: bold on, name Courier New')
    underlinestyle = xlwt.easyxf('font: bold on, name Courier New; border: bottom thin')
    centertalinment = xlwt.easyxf('font: bold on, name Courier New; align: horizontal center; border: bottom thin')
    rightalinment = xlwt.easyxf('font: bold on, name Courier New; align: horizontal right; border: bottom thin')
    leftunderlinestyle = xlwt.easyxf('font: bold on, name Courier New; align: horizontal right; border: left 2')

    
    s = wb.get_sheet(0) 
    hypen = ' ------------------------'
    for key, value in csv_info.items():
        for row, col in value:
            if key == 'B' or key=='I' or key=='G':
                s.write(col-1, row, invoice_val[key],boldstyle)
            elif key == 'J':
                s.write(col-1, row, invoice_val[key], rightalinment)
            elif key == 'D':
                s.write(col-1, row, invoice_val[key], centertalinment)
            elif key =='C':
                value = nte(invoice_val[key].replace('-','')).upper()
                s.write(col-1, row, value+hypen,underlinestyle)
            else:
                s.write(col-1, row, invoice_val[key],underlinestyle)
    s.write(3,15, '', leftunderlinestyle)  
    wb.save(output)

def format_cell(cells):
    if len(cells) == 1 and ord(cells) >= 65 and ord(cells) <= 90:
        return int(ord(cells) - 65)
    return int(cells)

def read_copy_info(templatepath):
    csv_info = defaultdict(list)
    path = os.path.join(templatepath, INVOICE_INFO)
    with open(path, 'r') as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            for cell in row[1:]:
                if cell == '': continue
                csv_info[row[0]].append(tuple(map(format_cell, cell.split('-'))))
    return csv_info


def main(invoice_value, output_path,
         template_path=os.path.join(os.environ["HOMEPATH"], "Desktop", 'automatedTool')):
    #pc = ParsingCredit(filepath)
    #bl = ParsingBl(blfile)
    # 템플릿으로부터 엑셀 파일 읽어오기
    #template_path = os.path.join(os.environ["HOMEPATH"], "Desktop", 'automatedTool')#'C:/Users/김수현/Desktop/project/file/proejct/automatedTool'
    copy_from_template(template_path, output_path)
    # 그 파일을 읽어들여 subtitute하기
    csv_info = read_copy_info(template_path)
    change_file(output_path, csv_info, invoice_value)


if __name__ == "__main__":
    import argparse
    '''parser = argparse.ArgumentParser(description='file parser')
    parser.add_argument('--templatepath', '-t',
                        type=str,
                        required=True,
                        help='input template path')
    parser.add_argument('--output', '-o',
                    type=str,
                    required=True,
                    help='input output file path with name')
    parser.add_argument('--filename', '-f',
                        type=str,
                        required=True,
                        help='input_credit_file')
    parser.add_argument('--blfilename', '-b',
                        type=str,
                        required=True,
                        help='input_bl_file')
    args = parser.parse_args()'''

    main({'A': 'IN THE AMOUNT OF USD 300.00', 'D': '12-12', 'B': 'AT 180  DAYS AFTER SIGHT OF THIS BILL OF EXCHANGE', 'C': '1234----------------------------------------------------------', 'J': '00/100 U.S. DOLLAR', 'E1': 'HYOLIM TIMBER CO.,LTD.', 'E2': '25-333,23,BANGCHUK-RO,83 BEON-', 'E3': 'GIL,DONG-GU,INCHEON, SOUTH KOREA', 'E4': '', 'F': 'INDUSTRIAL BANK OF KOREA', 'G': 'L/C NO. M04FB2011NU00395', 'I': '10-NOV-20', 'H1': 'STANDARD CHARTERED BANK NEW YORK', 'H2': '1095 AVENUE OF THE AMERICAS', 'H3': 'NEW YORK UNITED STATES OF AMERICA', 'H4': ''},'output.xls')