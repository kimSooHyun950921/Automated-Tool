import re
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
class ParsingBl():
    def __init__(self, path):
        self.text = self.convert_pdf_to_txt(path)
        #print(self.text)

            
    def convert_pdf_to_txt(self, path):
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


    def get_VS(self):
        result = None
        pattern = re.compile('(VESSEL.*)([\s\S]*)(PORT\WOF\WDISCHARGE.*)', re.MULTILINE)
        result = pattern.search(self.text)
        if result:
            return result[2].strip().split('\n')[0]
        return result


    def get_POD(self):
        result = None
        pattern = re.compile('(PORT\WOF\WDISCHARGE.*)\s(.+)')
        result = pattern.search(self.text)
        if result:
            return result[2].strip().split('\n')[0]
        return result


    def get_POL(self):
        result = None
        pattern = re.compile('(PORT\WOF\WLOADING.*)\s(.+)')
        result = pattern.search(self.text)
        if result:
            return result[2].strip().split('\n')[0]
        return result


    def get_hc(self):
        #(H\.S\.CODE\W*:\W*)(\d+\.\d+)
        result = None
        pattern = re.compile('(H\.S\.CODE\W*:\W*)(\d+\.\d+)')
        result = pattern.search(self.text)
        if result:
            return result[2].strip().split('\n')
        return result



def main(filename):
    bl = ParsingBl(filename)
    print("vessel", bl.get_VS())
    print("port of discharge", bl.get_POD())
    print("port of loading", bl.get_POL())
    print("hscode", bl.get_hc())
    

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='pdf parser')
    parser.add_argument('--filename', '-f',
                        type=str,
                        required=True,
                        help='input credit file')
    args = parser.parse_args()
    main(args.filename)