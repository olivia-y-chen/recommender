'''
@author: Olivia Chen
'''
import RecommenderEngine


def makerecs(name, items, ratings, numUsers, top):
    '''
    This function calculates the top recommendations and returns a two-tuple consisting of two lists. 
    The first list is the top items rated by the rater called name (string).
    The second list is the top items not seen/rated by name (string)
    '''
    weighted = RecommenderEngine.recommendations(name, items, ratings, numUsers)
    user = ratings[name]
    topseen = []
    topunseen = []
    seen = []
    for i in range(0, len(user)):
        if user[i] != 0:
            seen.append(items[i])
    for w in weighted:
        if w[0] not in seen:
            topunseen.append(w)
        if w[0] in seen:
            topseen.append(w)
    topseen = topseen[0:top]
    topunseen = topunseen[0:top]
    return (topseen, topunseen)
    pass


if __name__ == '__main__':
    pass

