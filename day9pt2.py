import fileinput
def findSub( l, a ):
    j = 0
    s = 0
    for i in range( 0, len(a) ):
        s += a[i]
        if( s > l ):
            while( s > l ):
                s -= a[j]
                j += 1
        if( s == l ):
            return a[j:i+1]
def main():
    a = []
    for line in fileinput.input():
        a.append( int(line) )
    i = findSub( 1124361034, a )
    i.sort()
    print( i )
    ans  = i[0] + i[len(i)-1]
    print('Answer:' + str(ans))
main()

"""
Block Comment
"""
