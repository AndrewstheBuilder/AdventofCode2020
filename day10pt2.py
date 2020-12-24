
import fileinput
import sys

#dynamic programming solution
def process( arr ):
    paths = [0]*(len(arr))
    paths[0] = 1
    for i in range( 0, len(arr) ):
        try:
            if( arr[i+1] - arr[i] <= 3 ):
                 #print( arr[i+1], arr[i] )
                 paths[i+1] += paths[i]
            if( arr[i+2] - arr[i] <= 3 ):
                 #print( arr[i+2], arr[i] )
                 paths[i+2] += paths[i]
            if( arr[i+3] - arr[i] <= 3 ):
                 #print( arr[i+3], arr[i] ) 
                 paths[i+3] += paths[i]
        except IndexError:
            pass
    return paths[i]
    
def main():
    arr = []
    arr.append( 0 )
    for line in fileinput.input():
        arr.append( int(line) )
    arr.sort()
    #print(arr)
    t = process( arr )
    print( t )
main()

