import fileinput
import math

def main():
    i = 0
    a = []
    e = 0
    for line in fileinput.input():
        if( i == 0 ):
            e = int(line)
            i += 1
        else:
            a = [int(i) for i in line.split(',') if( i != 'x')]
            
    ans = [10000000, 0 ]
    for i in range(len(a)):
        if( a[i] > e ):
            r = a[i] - e
            if( ans[0] > r ):
                ans[0] = r
                ans[1] = a[i] 
        else:
            q = math.floor(e/a[i])
            r = (q*a[i]) - e
            if( r == 0 ):
                ans[0] = r
                break
            elif( r < 0 ):
                r = ((q+1)*a[i])
                r = r - e
                if( ans[0] > r ):
                    ans[0] = r
                    ans[1]= a[i] 
    print( ans[0] * ans[1] )
        
        
main()

"""
Block Comment
"""
