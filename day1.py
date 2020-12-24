import fileinput
import math


def find( i, a ):
    j = 0
    r = len( a ) - 1
    while j <= r:
        m = math.floor((j+r)/2)
        if( i == a[m] ):
            return a[m]
        else:
            if( i < a[m] ):
                r = m-1
            else:
                i = m+1
    return -1

def main(): 
    arr = []
    for line in fileinput.input():
        arr.append( int(line) )
    arr.sort()
    for i in arr:
        n = find( 2020 - i, arr )
        if( n >= 0 ):
            print( n * i )
            break
main()
    
