'''
@author: Olivia Chen
'''

def averages(items, ratings):
    '''
    This function calculates the average ratings for items. 
    A two-tuple is returned, where the first element is a string and the second element is a float.
    '''
    rates = []
    for i in range(0, len(items)):
        ave = 0
        length = 0
        for n in ratings:
            ave += ratings[n][i]
            if ratings[n][i] != 0:
                length += 1
        if length != 0:
            ave = ave/length
        elif length == 0:
            ave = float(ave)
        tup = (items[i], ave)
        rates.append(tup)
        rates.sort()
        rates.sort(key=lambda x: x[1], reverse=True)
    return rates
    pass


def similarities(name, ratings):
    '''
    This function calculates how similar the rater called name is to all other raters.
    A two-tuple is returned, where the first element is a string and the second element is an integer.
    '''
    ls = ratings[name]
    sim = []
    for n in ratings:
        score = 0
        for i in range(0, len(ratings[n])):
            score += ls[i] * ratings[n][i]
        if n != name:
            sim.append((n, score))
    sim.sort()
    sim.sort(key=lambda x: x[1], reverse=True)
    return sim
    pass
 
def recommendations(name, items, ratings, numUsers):
    '''
    This function calculates the weighted average ratings and makes recommendations 
    based on the parameters and weighted average. A two-tuple is returned, where 
    the first element is a string and the second element is a float.
    '''
    simmeas = similarities(name, ratings)[0:numUsers]
    newRatings = {}
    for i in range(0, len(simmeas)):
        for n in ratings:
            if n == simmeas[i][0]:
                newLst = []
                for w in range(0, len(items)):
                    newLst.append(ratings[n][w]*simmeas[i][1])
                newRatings[n] = newLst
    weighted = averages(items, newRatings)
    return weighted
    pass   
        

if __name__ == '__main__':
    pass

"""print(recommendations('Liam', ["Cat", "Dog", 'Zebra'], {'Liam': [10, 2, 5], 'Man-Lin': [2,5,0], 'Max': [7, 9, 1], 'Jose': [1, 2, 3]}, 2))"""