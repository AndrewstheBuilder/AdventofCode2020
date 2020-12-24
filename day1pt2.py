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
                j = m+1
    return -1

def main(): 
    arr = []
    for line in fileinput.input():
        arr.append( int(line) )
    arr.sort()
    for i in range( 0, len(arr) ):
        for k in range( i + 1, len( arr ) ):
            x = 2020 - arr[i] - arr[k]
            #print( x )
            if( x > 0 ):
                n = find( x, arr )
                print("n is:" + str(n) )
                if( n > 0 ):
                    print( n * arr[i] * arr[k] )
                    exit()
main()
    
