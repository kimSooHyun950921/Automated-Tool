import re
import sys


def get_31(line):
    date = ''
    pattern = re.compile('(31C\W+DATE\WOF\WISSUE:\W+)(.+)')
    hypen_pattern = re.compile('([0-9]+)([A-Z]+)([0-9]+)')
    if pattern:
        date = pattern.search(line)
        return '-'.join(hypen_pattern.findall(date[2])[0])
            

    return date[2]


def find_info(lines):
    result = None
    lines = ' '.join(lines)
    sub_pattern = re.compile('((\W)(\d\.\W)|-\W|\+)')
    target_pattern = re.compile('(.+DRAWN\W+UNDER\W)(.+)')
    lines = sub_pattern.sub('\n', lines).split('\n')
    for line in lines:
        search = target_pattern.search(line)
        if search:
            result = search.group(2)
            break
    return result


def get_47A(line):
    result = None
    start_pattern = re.compile("^(47A\W+ADDITIONAL\W+CONDITIONS:\W+)(.+)", re.MULTILINE)
    end_pattern = re.compile("^(71D\W+DETAILS\W+OF\W+CHARGES:\W+)(.+)", re.MULTILINE)
    start_search = start_pattern.search(line)
    end_search = end_pattern.search(line)
    if start_search and end_search:
        start_index = start_search.span(2)[0]
        end_index = end_search.start()
        lines = line[start_index:end_index]
        lines = list(map(stripping, lines.strip().split("\n")))
        result = find_info(lines)
    return result
  

def find_bank_name(lines):
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
        result = list(map(stripping, result.strip().split("\n")))[0]
    return result


def get_46A(line):
    result = None
    start_pattern = re.compile("^(46A\W+DOCUMENTS\W+REQUIRED:\W+)(.+)", re.MULTILINE)
    stop_pattern = re.compile("^(47A\W+ADDITIONAL\W+CONDITIONS:\W+)(.+)", re.MULTILINE)
    start_search = start_pattern.search(line)
    end_search = stop_pattern.search(line)
    if start_pattern and end_search:
        start_index = start_search.span(2)[0]
        end_index = end_search.start()
        result = line[start_index:end_index]
        result = list(map(stripping, result.strip().split("\n")))
        result = find_bank_name(result)
    return result


def get_45GOODS(line):
    start_pattern = re.compile("^(45A\W+GOODS:\W+)(.+)", re.MULTILINE)
    stop_pattern = re.compile("^(46A\W+DOCUMENTS\W+REQUIRED:\W+)(.+)", re.MULTILINE)
    start_search = start_pattern.search(line)
    end_search = stop_pattern.search(line)
    if start_pattern and end_search:
        start_index = start_search.span(2)[0]
        end_index = end_search.start()
        result = line[start_index:end_index]
        result = list(map(stripping, result.strip().split("\n")))
        result = [line.replace('+','') for line in result]
        return result
    return None


def get_42C(line):
    result = None
    pattern = re.compile("(42C\W+DRAFTS\W+AT:\W+)(.+)")
    result = re.findall(pattern, line)
    if result:
        return result[0][1] + ' OF THIS BILL OF EXCHANGE'
    return result



def get_42A(line):
    result = []
    pattern = re.compile("42[A-Z]\W+DRAWEE:(\W+.+\s)+",  re.MULTILINE)
    match = pattern.search(line)
    if match:
        result = re.sub('42[A-Z]\W+DRAWEE:', '', match.group(0))
        result = list(map(stripping, result.split("\n")))
        len_result = len(result)
        #print(list(map(stripping, result.split("\n"))))
        return result[0:len_result-1]
    return result


def get_20DC(line):
    pattern = re.compile("(20\W+DC\W+NO:\W+)(.+)")
    result = re.findall(pattern, line)#[0][1]
    if result:
        return result[0][1]
    return None


def stripping(string):
    #string = re.sub('\.\.+', '',string)
    return string.strip()


def get_50APPLICANT(line):
    start_pattern = re.compile("^(50\W+APPLICANT:\W+)(.+)", re.MULTILINE)
    stop_pattern = re.compile("^(59\W+BENEFICIARY:\W+)(.+)", re.MULTILINE)
    start_search = start_pattern.search(line)
    end_search = stop_pattern.search(line)
    if start_pattern and end_search:
        start_index = start_search.span(2)[0]
        end_index = end_search.start()
        result = line[start_index:end_index]
        result = list(map(stripping, result.strip().split("\n")))
        return result
    return None


def main(filename):
    '''
    input: filename
    return: dict list
    '''
    parsing_data = dict()
    with open(filename, 'r') as reader:        
        data = reader.read()
        print("L/C NO.", get_20DC(data))
        print("SOLD TO:", get_50APPLICANT(data))
        print("COUNTRY OF ORIGIN:", get_45GOODS(data))
        print("BOF 둘째줄: ", get_42C(data))
        print("BOF TO: ",get_42A(data))
        print("BOF DRAWN UNDER CASE1: ",get_46A(data))
        print("BOF DRAWN UNDER CASE2: ",get_47A(data))
        print("BOF DATED: ",get_31(data))
    return ''


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='file parser')
    parser.add_argument('--filename', '-f',
                        type=str,
                        required=True,
                        help='input credit file')
    args = parser.parse_args()
    main(args.filename)