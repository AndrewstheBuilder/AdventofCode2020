import fileinput, re

def popUntil( v, i ):
    while( True):
        x = v.pop()
        if( i == x ):
            return v
        
    
def pass2( a ):
    i = 0
    acc = 0
    while( True ):
        x = a[i].split()
        print( i )
        if( x[0] == 'nop' ):
            i += 1
        elif( x[0] == 'acc' ):
            #print( 'acc:' + (x[1][1:len(x[1])]) )
            if( x[1][0] == '+' ):
                acc += int(x[1][1:len(x[1])])
            else:
                acc -= int(x[1][1:len(x[1])])
            i += 1
        elif( x[0] == 'jmp' ):
            if( x[1][0] == '+' ):
                i += int(x[1][1:len(x[1])])
            else:
                i -= int(x[1][1:len(x[1])])
        if( i > len(a)-1 ):
            break
    return acc

def pass1( a ):
    i = 0
    visited = []
    last = [] #contains last nop or jmp
    x = []
    hist = None #if you have to go back multiple jmp or nop statements
    change = {}
    while( True ):
        #print( i )
        if( i in visited ):
            #print( 'i' + str(i) )
            #print( visited )
            change = {}
            hist = i = last.pop()
            #print( 'hist:' + str(hist) )
            visited = popUntil( visited, i )
            x = a[i].split()
            if( x[0] == 'jmp' ):
                x[0] = 'nop'
            else:
                x[0] = 'jmp'
            change[i] =  x[0] + ' ' + x[1]
        else:
            x = a[i].split()
        #print( i )
        if( x[0] == 'nop' ):
            if( hist == None ):
                last.append( i )
            visited.append( i )
            i += 1
        elif( x[0] == 'acc' ):
            visited.append( i )
            i += 1
        elif( x[0] == 'jmp' ):
            if( hist == None ):
                last.append( i )
            visited.append( i )
            if( x[1][0] == '+' ):
                i += int(x[1][1:len(x[1])])
            else:
                i -= int(x[1][1:len(x[1])])
        if( i > len(a)-1 ):
            break
    print( change )
    index = list(change.keys())[0]
    a[index] =  change.get(index)
    return a

def main():
    a = []
    for line in fileinput.input():
        a.append( line.strip() )
    a = pass1( a )
    acc = pass2( a )
    print( 'Answer:' + str(acc) )
main()

"""
pt2
pass1: determines which instruction to change
3:jmp to 4 visited.appned(3)
4:jmp to 3 
pass2: returns value of accumlator
"""
