import re
import sys


def find_info(lines):
    result = None
    print(lines)
    lines = ' '.join(lines)
    pattern = re.compile('((\W)(\d\.\W)|-\W|\+)')
    result = pattern.sub('\n', lines)

    print(result)
    #pattern = re.comile("('DRAWN\W+UNDER)")
    
        




def get_47A(line):
    result = None
    start_pattern = re.compile("^(47A\W+ADDITIONAL\W+CONDITIONS:\W+)(.+)", re.MULTILINE)
    end_pattern = re.compile("^(71D\W+DETAILS\W+OF\W+CHARGES:\W+)(.+)", re.MULTILINE)
    start_search = start_pattern.search(line)
    end_search = end_pattern.search(line)
    if start_search and end_search:
        start_index = start_search.span(2)[0]
        end_index = end_search.start()
        result = line[start_index:end_index]
        result = list(map(stripping, result.strip().split("\n")))
        find_info(result)
        #result = find_info(' '.join(result[0:2]))
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
        return result
    return None


def get_42C(line):
    pattern = re.compile("(42C\W+DRAFTS\W+AT:\W+)(.+)")
    return re.findall(pattern, line)[0][1]


def get_42A(line):
    pattern = re.compile("(42A\W+DRAWEE:\W+)(.+)")
    return re.findall(pattern, line)[0][1]


def get_20DC(line):
    pattern = re.compile("(20\W+DC\W+NO:\W+)(.+)")
    return re.findall(pattern, line)[0][1]


def stripping(string):
    #string = string.replace('+','')
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
        #print(get_20DC(data))
        #print(get_50APPLICANT(data))
        #print(get_45GOODS(data))
        #print(get_42C(data))
        #print(get_42A(data))
        #print(get_46A(data))
        get_47A(data)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='file parser')
    parser.add_argument('--filename', '-f',
                        type=str,
                        required=True,
                        help='input credit file')
    args = parser.parse_args()
    main(args.filename)