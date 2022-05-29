'''
@author: Olivia Chen
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    f = open('data/movies.txt')
    lines = f.readlines()
    movielst = []
    linelst = []
    ratedict = {}
    for l in lines:
        lst1 = l.split(',')
        lst1[2] = lst1[2].strip('\n')
        lst1[2] = int(lst1[2])
        """if lst1[0] not in ratedict:
            ratedict[lst1[0]] = [lst1[2]]
        else:
            ratedict[lst1[0]].append(lst1[2])"""
        linelst.append(lst1)
        if lst1[1] not in movielst:
            movielst.append(lst1[1])
    linelst.sort(key=lambda x: x[1])
    for i in linelst:
        if i[0] not in ratedict:
            ratedict[i[0]] = [i[2]]
        else:
            ratedict[i[0]].append(i[2])
    movielst.sort()
    return(movielst, ratedict)
    pass

if __name__ == '__main__':
    pass

print(getdata())