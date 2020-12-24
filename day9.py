import fileinput
def search( pre, num ):
    #if( num == 403 ):
        #print( pre )
    for i in range( 0, len(pre)):
        x = num - pre[i]
        if( x != pre[i] and x in pre ):
            return True
    return False
    
def badNum( a ):
    j = 0
    for i in range( 25, len(a) ):
        pre = a[j:j+25]
        print( i, j )
        x = search( pre, a[i] )
        j += 1
        if( not(x) ):
            print( 'index' + str(i) )
            return a[i]
    return -1

def main():
    a = []
    for line in fileinput.input():
        a.append( int(line) )
    i = badNum( a )
    print('Answer:' + str(i))
main()

"""
Block Comment
"""
