def FlattenList( l ):
    lst=[]
    for i in l:
        if type(i)==int:
            lst.append(i)
        elif type(i)==list:
            for j in i:
                lst.append(j)
    return lst



if __name__=='__main__':
    r = FlattenList( [1, [2], [3,4,5], [6,7], 8] )
    assert r == [1, 2, 3, 4, 5, 6, 7, 8]
