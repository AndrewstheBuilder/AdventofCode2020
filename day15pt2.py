import fileinput


def main():
    for line in fileinput.input():
        a = [int(x) for x in line.split(',')]
    d = {}
    length = len(a)
    for i in range(length):
        prev = d.get(a[i])
        d[a[i]] = [i+1, prev]
        prevKey = a[i]
    i += 1
    while( i < 30000000 ):
        val = d.get(prevKey)
        if( val[1] == None ):
            curKey = 0
            val = d.get(0)
            if( val != None ):
                d[0] = [i+1, val[0]]
            else:
                d[0] = [i+1, None]
            prevKey = 0
        else:
            curKey = val[0] - val[1]
            val = d.get(curKey)
            if( val != None ):
                d[curKey] = [i+1, val[0]]
            else:
                d[curKey] = [i+1, None]
            prevKey = curKey
        if( i == 29999999 ):
            print( curKey )
        i += 1

        
if __name__=="__main__":
    main()

"""
Data structure:dictionaries
stores value and most recent index
"""
