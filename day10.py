import fileinput

def convertListToInt( line ):
    length = len( line )
    arr = [0] * length
    for j in range(0, length):
        arr[j] = int( line[j] )
    arr.sort()
    return arr

def main():
    i = 0
    arr = []
    for line in fileinput.input():
        arr.append( int(line) )
    arr = convertListToInt( arr )
    num = 0
    num1 = 0
    num3 = 1
    if( arr[0] > 3 or arr[0] < 0 ):
        exit()
    elif( arr[0] == 1):
        num1 += 1
    elif( arr[0] == 3 ):
        num3 += 1
    for i in range( 0, len( arr ) - 1 ):
        num = arr[i + 1] - arr[i]
        if( num == 0 ):
            continue
        elif( num == 1 ):
            num1 += 1
        elif( num == 3 ):
            num3 += 1
        elif( num > 3 ):
            print( 'num1:' + num1 )
            print( 'num3:' + num3 )
            exit()
    print( 'num1:' + str(num1) )
    print( 'num3:' + str(num3) )
       
main()
