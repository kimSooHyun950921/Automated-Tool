import re
import sys

class ParsingCredit():
    def __init__(self, path):
        self.text = self.read_text(path)

    
    def read_text(self, path):
        data = ''
        reader = open(path, 'r')
        data = reader.read()
        reader.close()
        return data


    def get_31(self):
        date = ''
        pattern = re.compile('(31C\W+DATE\WOF\WISSUE:\W+)(.+)')
        hypen_pattern = re.compile('([0-9]+)([A-Z]+)([0-9]+)')
        if pattern:
            date = pattern.search(self.text)
            return '-'.join(hypen_pattern.findall(date[2])[0])
                

        return date[2]


    def find_info(self, lines):
        result = None
        lines = ' '.join(lines)
        sub_pattern = re.compile('((\W)(\d\.\W)|-\W|\+)')
        target_pattern = re.compile('(ALL\WDRAFTS\WMUST\WBE\WMARKED\W\'DRAWN\WUNDER\W)(.+)')
        lines = sub_pattern.sub('\n', lines).split('\n')
        for line in lines:
            search = target_pattern.search(line)
            if search:
                result = search.group(2)
                break
        return result

    def get_drawn(self):
        result_1 = self.get_47A()
        result_2 = self.get_46A()
        if result_1 and result_2:
            return result_1
        elif result_1:
            return result_1
        else:
            return result_2


    def get_47A(self):
        result = None
        start_pattern = re.compile("^(47A\W+ADDITIONAL\W+CONDITIONS:\W+)(.+)", re.MULTILINE)
        end_pattern = re.compile("^(71D\W+DETAILS\W+OF\W+CHARGES:\W+)(.+)", re.MULTILINE)
        start_search = start_pattern.search(self.text)
        end_search = end_pattern.search(self.text)
        if start_search and end_search:
            start_index = start_search.span(2)[0]
            end_index = end_search.start()
            lines = self.text[start_index:end_index]
            lines = list(map(self.stripping, lines.strip().split("\n")))
            result = self.find_info(lines)
        return result
    

    def find_bank_name(self, lines):
        result = None
        line = ' '.join(lines)
        start_pattern = re.compile("(TO\W+THE\W+ORDER\W+OF)(.+)")
        end_pattern = re.compile("(MARKED\W+FREIGHT\W+PREPAID)(.+)")
        start_search = start_pattern.search(line)
        end_search = end_pattern.search(line)
        if start_search and end_search:
            start_index = start_search.span(2)[0]
            end_index = end_search.start()
            result = line[start_index:end_index]
            result = list(map(self.stripping, result.strip().split("\n")))[0]
        return result


    def get_46A(self):
        result = None
        start_pattern = re.compile("^(46A\W+DOCUMENTS\W+REQUIRED:\W+)(.+)", re.MULTILINE)
        stop_pattern = re.compile("^(47A\W+ADDITIONAL\W+CONDITIONS:\W+)(.+)", re.MULTILINE)
        start_search = start_pattern.search(self.text)
        end_search = stop_pattern.search(self.text)
        if start_pattern and end_search:
            start_index = start_search.span(2)[0]
            end_index = end_search.start()
            result = self.text[start_index:end_index]
            result = list(map(self.stripping, result.strip().split("\n")))
            result = self.find_bank_name(result)
        return result


    def get_45GOODS(self):
        start_pattern = re.compile("^(45A\W+GOODS:\W+)(.+)", re.MULTILINE)
        stop_pattern = re.compile("^(46A\W+DOCUMENTS\W+REQUIRED:\W+)(.+)", re.MULTILINE)
        start_search = start_pattern.search(self.text)
        end_search = stop_pattern.search(self.text)
        if start_search and end_search:
            start_index = start_search.span(2)[0]
            end_index = end_search.start()
            result = self.text[start_index:end_index]
            result = list(map(self.stripping, result.strip().split("\n")))
            result = [text.replace('+','') for text in result]
            return result
        return None


    def get_LOGS(self):
        pattern = re.compile('[:]*([a-zA-Z\s]+LOGS)')
        goods = self.get_45GOODS()
        if goods:
            for partial in goods:
                search = pattern.search(partial)
                if search: 
                    return search.group(1)


    def get_TERMSPRICE(self):
        pattern = re.compile('([a-zA-Z\s]*[:]*[a-zA-Z\s]+PORT[(S)]*)')
        goods = self.get_45GOODS()
        if goods:
            for partial in goods:
                search = pattern.search(partial)
                if search: 
                    return search.group(1).rstrip().lstrip()


    def get_COUNTRYORIGIN(self):
        pattern = re.compile('(.*ORIGIN.*)')
        goods = self.get_45GOODS()
        if goods:
            for partial in goods:
                search = pattern.search(partial)
                if search: 
                    return search.group(1).rstrip().lstrip()


    def get_42C(self):
        result = None
        pattern = re.compile("(42C\W+DRAFTS\W+AT:\W+)(.+)")
        result = re.findall(pattern, self.text)
        if result:
            return result[0][1] + ' OF THIS BILL OF EXCHANGE'
        return result



    def get_42A(self):
        result = []
        pattern = re.compile("42[A-Z]\W+DRAWEE:(\W+.+\s)+",  re.MULTILINE)
        match = pattern.search(self.text)
        if match:
            result = re.sub('42[A-Z]\W+DRAWEE:', '', match.group(0))
            result = list(map(self.stripping, result.split("\n")))
            len_result = len(result)
            return result[0:len_result-1]
        return result


    def get_20DC(self):
        pattern = re.compile("(20\W+DC\W+NO:\W+)(.+)")
        result = re.findall(pattern, self.text)#[0][1]
        if result:
            return result[0][1]
        return None


    def stripping(self, string):
        #string = re.sub('\.\.+', '',string)
        return string.strip()


    def get_50APPLICANT(self):
        start_pattern = re.compile("^(50\W+APPLICANT:\W+)(.+)", re.MULTILINE)
        stop_pattern = re.compile("^(59\W+BENEFICIARY:\W+)(.+)", re.MULTILINE)
        start_search = start_pattern.search(self.text)
        end_search = stop_pattern.search(self.text)
        if start_pattern and end_search:
            start_index = start_search.span(2)[0]
            end_index = end_search.start()
            result = self.text[start_index:end_index]
            result = list(map(self.stripping, result.strip().split("\n")))
            return result
        return None


def main(filename):
    '''
    input: filename
    return: dict list
    '''
    pc_dict = dict()
    bl_dict = dict()
    pc = ParsingCredit(filename)
    print("L/C NO.20DC", pc.get_20DC())
    print("SOLD TO: 50APP", pc.get_50APPLICANT())
    print("COUNTRY OF ORIGIN: 45GOODS", pc.get_45GOODS())
    print("LOGS:", pc.get_LOGS())
    print("PORT:", pc.get_TERMSPRICE())
    print("COUNTRY OF ORIGIN:", pc.get_COUNTRYORIGIN())
    print("BOF 둘째줄: 42C", pc.get_42C())
    print("BOF TO: 42A",pc.get_42A())
    print("BOF DRAWN UNDER C:", pc.get_drawn())
    #print("BOF DRAWN UNDER CASE1: 46A",pc.get_46A())
    #print("BOF DRAWN UNDER CASE2: 47A",pc.get_47A())
    print("BOF DATED: 31",pc.get_31())
    


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='file parser')
    parser.add_argument('--filename', '-f',
                        type=str,
                        required=True,
                        help='input credit file')
    args = parser.parse_args()
    main(args.filename)