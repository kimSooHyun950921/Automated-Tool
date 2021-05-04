import re
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr,  laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 1
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    text = retstr.getvalue()
    fp.close()
    device.close()
    retstr.close()
    return text


def get_VS(text):
    result = None
    pattern = re.compile('(VESSEL.*)([\s\S]*)(PORT\WOF\WDISCHARGE.*)', re.MULTILINE)
    result = pattern.search(text)
    if result:
        return result[2].strip().split('\n')
    return result


def get_POD(text):
    result = None
    pattern = re.compile('(PORT\WOF\WDISCHARGE.*)\s(.+)')
    result = pattern.search(text)
    if result:
        return result[2].strip().split('\n')
    return result


def get_POL(text):
    result = None
    pattern = re.compile('(PORT\WOF\WLOADING.*)\s(.+)')
    result = pattern.search(text)
    if result:
        return result[2].strip().split('\n')
    return result


def get_hc(text):
    #(H\.S\.CODE\W*:\W*)(\d+\.\d+)
    result = None
    pattern = re.compile('(H\.S\.CODE\W*:\W*)(\d+\.\d+)')
    result = pattern.search(text)
    if result:
        return result[2].strip().split('\n')
    return result



def main():
    result = convert_pdf_to_txt('./example.pdf')
    print(get_VS(result))
    print(get_POD(result))
    print(get_POL(result))
    print(get_hc(result))
    

    
    

if __name__ == "__main__":
    main()