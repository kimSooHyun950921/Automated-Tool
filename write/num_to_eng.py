from collections import deque

def change_value(value):
    value = value.replace(',','')
    under_20 = ["", "one", "two", "three", "four","five","six","seven","eight","nine","ten",
                "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen", "eighteen","nineteen"]
    ten_to_hundred = ['',"ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninty","hundred"]
    over_hundred = ["","thousand","million","billion","trillion"]
    value = value[::-1]

    num_list = list()
    
    for i in range(0, len(value), 3):
        indiviual_num = value[i:i+3]
        indiviual_num = indiviual_num[::-1]
        #print(indiviual_num)

        num_list.append(indiviual_num)

    eng_list = deque()
    hundred_idx = 0
    for num in num_list:
        print(num)
        num = str(int(num))
        eng = list()
        if num != '0':
            if len(num)==1:
                eng.append(under_20[int(num[0])])
            elif len(num)==2:
                if int(num) < 20:
                    eng.append(under_20[int(num)])
                else:
                    eng.append(ten_to_hundred[int(num[0])])
                    eng.append(under_20[int(num[1])])
            elif len(num)==3:
                eng.append(under_20[int(num[0])])
                eng.append(ten_to_hundred[10])
                if int(num[1:]) != 0:
                    if int(num[1:]) < 20:
                        eng.append(under_20[int(num[1:])])
                    elif int(num[1:]) % 10 == 0:
                        eng.append(ten_to_hundred[int(num[1])])
                    else:
                        eng.append(ten_to_hundred[int(num[1])])
                        eng.append(under_20[int(num[2])])

        
        if len(num) > 0 or ''.join(eng)!= '':
            eng.append(over_hundred[hundred_idx])

        hundred_idx += 1
        #print(eng)
        #print(' '.join(eng))
        eng_list.appendleft(' '.join(eng))
    
    return ' '.join(eng_list).lstrip().rstrip()

if __name__ == "__main__":
    value = input("number:")
    print(change_value(value))