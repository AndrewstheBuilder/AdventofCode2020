import fileinput



def traverse( r, d ):
    j = 0 #start at top left
    count = 0 #number of trees encountered
    for i in range( 0, (len(a)-1)):

        #wrap around to beginning of line
        if( (len(a[i])-1) < j+3 ):
            j = ((j+3) - (len(a[i])-1) - 1 ) #the rightmost -1 is to account for zero index
        else:
            j = j+3
        if( a[i+1][j] == "#" ):
            count += 1
    print( count )

def main():
    a = []
    for line in fileinput.input():
        a.append( line.replace("\n", "") )
    print( a )

main()
