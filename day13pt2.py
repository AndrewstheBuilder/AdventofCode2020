import fileinput
import math

def findInverse( ni, n ):
    newni = ni % n
    r = 0
    i = 0
    # newni = 1 (mod n) -> newni*(number) % mod n = 1 -> return number
    while( r != 1 ):
        i += 1
        r = (newni * i) % n
    return i

def newDisp( a, m ):
    i = len(a) - 1
    while( i >= 0 ):
        a[i][1] = m - a[i][1]
        i -= 1
    
def main():
    i = 0
    a = []
    e = 0
    for line in fileinput.input():
        if( i == 0 ):
            i += 1
        else:
            a = line.split(',')
            a = [ [int(a[i]), i] for i in range(len(a)) if(a[i] != 'x') ]
    product = 1
    for i in range( len(a) ):
        product *= a[i][0]
    # using the Chinese Remainder Theorem
    ans = 0
    maxOffset = a[len(a)-1][1]
    newDisp( a, maxOffset ) #The last element in a with the max offset will have a 0 offset
                     #this is because 19%5 = 4 and not 1 -> (5 * 4 = 20)
                     #using the chinese theorem I was intially going to do the offsets like in the problem, but the offsets will not be the correct remainders
                     #19%5 != 1 look at the problem and see how each offset is increasing from the answer 7:0, 13:1. 1068781%13 != 1
    for i in range( len(a) ):
        bi = a[i][1]
        Ni = int(product/a[i][0]) 
        xi = findInverse( Ni, a[i][0] )
        ans += bi * Ni * xi
    print('Answer:', (ans%product)-maxOffset )
            

        
        
main()

"""
Block Comment
"""
