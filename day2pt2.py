import fileinput
import math

def findAll( l, s ):
    arr = []
    i = 0
    i = s.find( l, i )
    while( i != -1 ):
        i += 1
        arr.append( i )
        i = s.find( l, i )
    return arr
def find( n, a ):
    for k in a:
        if( k == n ):
            return n
    return -1

def main():
    i = 0
    for line in fileinput.input():
        a = line.split()
        num = a[0].split("-")
        numl = int(num[0])
        numm = int(num[1])
        l = a[1].split(":")
        arr = findAll( l[0], a[2] )
        f1 = find( numl, arr )
        f2 = find( numm, arr )
        if( f1 != -1 and f2 != -1 ):
            continue
        elif( f1 != -1 or f2 != -1):
            i += 1
    print( i )
main()
    
