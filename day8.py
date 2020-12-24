import fileinput, re

def process( a ):
    i = 0
    acc = 0
    while( True ):
        x = a[i].split() #modify this in pt2 if you need to make more
                         #than one cycle
        print( i )
        if( x[0] == 'nop' ):
            a[i] = '!'
            i += 1
        elif( x[0] == 'acc' ):
            #print( 'acc:' + (x[1][1:len(x[1])]) )
            if( x[1][0] == '+' ):
                acc += int(x[1][1:len(x[1])])
            else:
                acc -= int(x[1][1:len(x[1])])
            a[i] = '!'
            i += 1
        elif( x[0] == 'jmp' ):
            a[i] = '!'
            if( x[1][0] == '+' ):
                i += int(x[1][1:len(x[1])])
            else:
                i -= int(x[1][1:len(x[1])])
        else:
            break
    return acc

def main():
    a = []
    for line in fileinput.input():
        a.append( line.strip() )
    acc = process( a )
    print( 'Answer:' + str(acc) )
main()

"""
add line into array
have a separate accumulator variable
if line gets visited modify it in array
so on the first visit to a modified spot in array return
"""
