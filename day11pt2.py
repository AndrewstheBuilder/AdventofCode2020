import fileinput, copy, sys

def findFLD( a, i, j ):
    i -= 1
    j -= 1
    while( i >= 0 and j >= 0 ):
        if( a[i][j] != '.' ):
            return a[i][j]
        i -= 1
        j -= 1
    return None

def findFront(a, i, j ):
    i -= 1
    while( i >= 0 ):
        if( a[i][j] != '.' ):
            return a[i][j]
        i -= 1
    return None

def findFRD( a, i, j ):
    j += 1
    length = len( a[i] )
    i -= 1
    while( i >= 0 and j < length ):
        if( a[i][j] != '.' ):
            return a[i][j]
        i -= 1
        j += 1
    return None

def findLeft( a, i, j ):
    j -= 1
    while( j >= 0 ):
        if( a[i][j] != '.' ):
            return a[i][j]
        j -= 1
    return None

def findRight( a, i, j ):
    j += 1
    length = len(a[i])
    while( j < length ):
        if( a[i][j] != '.' ):
            return a[i][j]
        j += 1
    return None

def findBLD( a, i, j ):
    i += 1
    j -= 1
    length = len(a)
    while( i < length and j >= 0 ):
        if( a[i][j] != '.' ):
            return a[i][j]
        i += 1
        j -= 1
    return None

def findBack( a, i, j ):
    i += 1
    length = len(a)
    while( i < length ):
        if(a[i][j] != '.' ):
            return a[i][j]
        i += 1
    return None

def findBRD( a, i, j ):
    j += 1
    length1 = len(a)
    length2 = len(a[i])
    i += 1
    while( i < length1 and j < length2 ):
        if( a[i][j] != '.' ):
            return a[i][j]
        i += 1
        j += 1
    return None

    
def check( e, a, i, j ):
    adj = []
    
    fld = findFLD(a, i, j)
    if( fld ):
        adj.append( fld )
    front = findFront( a, i, j )
    if( front ):
        adj.append( front )
    frd = findFRD( a, i, j )
    if( frd ):
        adj.append( frd )
    left = findLeft( a, i, j )
    if( left ):
        adj.append( left )
    right = findRight( a, i, j )
    if( right ):
        adj.append( right )
    bld = findBLD( a, i, j )
    if( bld ):
        adj.append( bld )
    back = findBack( a, i, j )
    if( back ):
        adj.append( back )
    brd = findBRD( a, i, j )
    if( brd ):
        adj.append( brd )
        
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
        if( count >= 5 ):
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
        t = copy.deepcopy(a) #this deep copy probably takes up a lot in terms of space and time complexity
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
