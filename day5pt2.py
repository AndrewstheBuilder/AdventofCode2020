import fileinput, math

def process( l ):
    arrRow = [0, 127]
    arrCol = [0, 7]
    for i in range(0, 8):
        x = arrRow[1] - arrRow[0]
        if(l[i] == 'F'):
            arrRow[1] = math.floor(arrRow[1] - (x/2))
        elif(l[i] == 'B'):
            arrRow[0] = math.ceil(arrRow[0] + (x/2))
    if( arrRow[0] != arrRow[1] ):
        print( "WTF" )
        exit()
        
    for i in range( 7, len(l) ):
        x = arrCol[1] - arrCol[0]
        if( l[i] == 'R' ):
            arrCol[0] = math.ceil(arrCol[0] + (x/2))
        elif( l[i] == 'L' ):
            arrCol[1] = math.floor(arrCol[1] - (x/2))
    if( arrCol[0] != arrCol[1] ):
        print( "WTF" )
        exit()
    return [arrRow[0], arrCol[0]]
            
def findSeat( t ):
    temp = []
    for i in range(0, len(t)):
        if( i != 0 and t[i]-1 != t[i-1] ):
            print( t[i], t[i-1] )
        
def main():
    t = []
    for line in fileinput.input():
        arr = process(line)
        j = ((arr[0]*8) + arr[1])
        t.append(int(j))
        #print( arr[0], arr[1], ((arr[0]*8) + arr[1]))
    t.sort()
    findSeat( t )
    print( t )
main()
