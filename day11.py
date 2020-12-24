import fileinput, copy, sys

def check( e, a, i, j ):
    adj = []
    x1 = y1 = x2 = y2 = -1
    if( i - 1 >= 0 ):
        x1 = i - 1
    if( j - 1 >= 0 ):
        y1 = j - 1
    if( i + 1 < len(a) ):
        x2 = i + 1
    if( j + 1 < len(a[i]) ):
        y2 = j + 1
        
    if( x1 != -1 ):
        adj.append( a[x1][j] )
        if( y1 != -1 ):
            adj.append( a[x1][y1] )
        if( y2 != -1 ):
            adj.append( a[x1][y2] )
    if( y1 != -1 ):
        adj.append( a[i][y1] )
    if( y2 != -1 ):
        adj.append( a[i][y2] )
    if( x2 != -1 ):
        adj.append( a[x2][j] )
        if( y1 != -1 ):
            adj.append( a[x2][y1] )
        if( y2 != -1 ):
            adj.append( a[x2][y2] )
            
    if( e == 'L' ):
        b = True
        for x in adj:
            b = b and x != '#'
        if( b ):
            t[i][j] = '#'
            return True
    elif( e == '#' ):
        count = 0
        for x in adj:
            if( x == '#' ):
                count += 1
        if( count >= 4 ):
            t[i][j] = 'L'
            return True
    return False

def output( a ):
    for i in range( 0, len(a) ):
        print( ''.join(a[i]) )
    print()
def countOccupied( a ):
    c = 0
    for i in range( 0, len(a) ):
        for j in range( 0, len(a[i]) ):
            if( a[i][j] == '#' ):
                c += 1
    print('Occupied Seats:' +  str( c ) )
    
def main():
    a = []
    global t
    t = []#temp array holds the changes made to seating in between rounds
    for line in fileinput.input():
       a.append(list(line.strip()))
       
    changes = 1
    while( changes != 0 ):
        changes = 0
        t = copy.deepcopy(a)
        #output( a )
        for i in range(0, len(a)):
            for j in range(0, len(a[i])):
                if( a[i][j] == '.' ):
                    continue
                elif( a[i][j] == 'L' ):
                    if( check( a[i][j], a, i, j ) ):
                        changes += 1
                elif( a[i][j] == '#' ):
                    if( check( a[i][j], a, i, j ) ):
                        changes += 1
        a = copy.deepcopy(t)
        
    #the answer
    output( a ) 
    countOccupied( a )
main()

"""
Block Comment
"""
