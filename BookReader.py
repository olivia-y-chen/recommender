'''
@author: Olivia Chen
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    f = open('data/books.txt')
    lines = f.readlines()
    booklst = []
    ratedict = {}
    for l in lines:
        templst = l.split(',')
        tempdct = {}
        ratedict[templst[0]] = []
        templst[-1] = templst[-1].strip('\n')
        for i in range(0, len(templst)):
            if i%2 == 1 and templst[i] not in booklst:
                booklst.append(templst[i])
            if i%2 == 1:
                tempdct[templst[i]] = int(templst[i+1])
        tempdct = sorted(tempdct.items())
        for i in tempdct:
            ratedict[templst[0]].append(i[1])
    booklst.sort()
    return (booklst, ratedict)
    pass

if __name__ == '__main__':
    pass

print(getdata())