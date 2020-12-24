import fileinput



def traverse( r, d, a ):
    j = 0 #start at top left
    i = d
    count = 0 #number of trees encountered
    length = len(a)
    lengthRow = len(a[0]) - 1 # - 1 to stay inbounds for indexes of array
    while i < length:
        #wrap around to beginning of line
        if( lengthRow < j+r ):
            j = ((j+r) - lengthRow - 1 ) #the rightmost - 1 is to account for zero index
        else:
            j = j+r
        if( a[i][j] == "#" ):
            count += 1
        i += d
    print( count )

def main():
    a = []
    for line in fileinput.input():
        a.append( line.replace("\n", "") )
    #print( a )
    traverse( 1,1,a)
    traverse( 3,1,a)
    traverse( 5,1,a)
    traverse( 7,1,a)
    traverse( 1,2,a)

main()
