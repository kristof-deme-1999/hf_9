import numpy

def recode_values(list_1, list_2):

    for i in list_1:
        if i == 'NAP': # 97
            list_2.append(-1)
        elif i == 'DK': # 98
            list_2.append(-1)
        elif i == 'NA': # 99
            list_2.append(-1)
        elif i == 'nan': # üres
            list_2.append(-1)
        else: # valid érték
            list_2.append(int(i))

def categorize(list_1,list_2):
    for i in list_1:
        if 0 < i < 9:
            list_2.append(1) #általános
        elif 8 < i < 13:
            list_2.append(2) #gimnázium
        elif i > 12:
            list_2.append(3)#továbbtanulás
        else:
            list_2.append(i)#invalid értékek