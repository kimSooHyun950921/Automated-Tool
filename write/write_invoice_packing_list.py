
import shutil
import os
import csv
import xlrd
import xlwt

from collections import defaultdict
from xlutils.copy import copy
INVOICE = 'template/invoice_template.xls'
INVOICE_INFO = 'template/invoice_info.csv'


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
    boldstyle = xlwt.easyxf('font: bold on, name Courier New;')
    normalstyle = xlwt.easyxf('font: name Courier New')
    rightalinment = xlwt.easyxf('font: name Courier New; align: horizontal right;')


    s = wb.get_sheet(0)
    s.insert_bitmap('reference/imagetoadd.bmp', 0, 0, 6,5)
    s.insert_bitmap('reference/imagetoadd.bmp', 59, 0, 6,5)
    
    for key, value in csv_info.items():
        
        for row, col in value:
            if key == 'M' or key == 'G':
                s.write(col-1, row, invoice_val[key],boldstyle)
            elif key == 'I' and (col==103 or col == 44):
                s.write(col-1, row, invoice_val[key],rightalinment)
            elif key == 'K' and (col==103 or col == 44):
                s.write(col-1, row, invoice_val[key],rightalinment)
            elif key == 'N':
                s.write(col-1, row, invoice_val[key],rightalinment)
            else:
                s.write(col-1, row, invoice_val[key],normalstyle)

    wb.save(output)


    '''tf = TemporaryFile()
    w = StreamWriter(tf)
    f = w.get_stream(output)
    tf.seek()
    sheet = workbook.sheet_by_name('Sheet1')
    for row in range(sheet.nrows):
        for col in range(0, sheet.ncols):
            newsheet.write(row, col, sheet.cell_value(row, col))
    
            #print("value", cell.value)
    newworkbook.save('./ex.xls')'''

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

    main({'A1': 'HYOLIM TIMBER CO.,LTD.', 'A2': '25-333,23,BANGCHUK-RO,83 BEON-', 'A3': 'GIL,DONG-GU,INCHEON, SOUTH KOREA', 'A4': '', 'A5': '', 'M': 'M04FB2011NU00395', 'G': 'COUNTRY OF ORIGIN : CANADA', 'B': '1234', 'C': '1234', 'D': 'M.V. SANDY BAY', 'E': 'NANAIMO, BC, CANADA', 'F': 'INCHON SOUTH KOREA PORT', 
'H': 'CANADIAN ROUND LOGS', 'I': '1234', 'K': '1234', 'N': '1234', 'J': 'PRICE TERMS : CFR SOUTH KOREAN PORT(S)', 'O': '1234', 'L': '1234'},'Result/output.xls')