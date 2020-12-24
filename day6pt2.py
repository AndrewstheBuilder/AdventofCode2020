import fileinput

def split(word): 
    return [char for char in word]

def process( arr ):
    a = []
    temp = []
    count = 0
    for i in range( 0, len(arr)):
        if( i == 0 ):
            for char in arr[i]:
                a.append( char )
            continue
        for char in arr[i]:
            if( not(char in a) ):
                continue
            else:
                temp.append( char )
        a = temp
        temp = []          
    return len( a )
def main():
    temp = []
    a = []
    for line in fileinput.input():
        if( len(temp) != 0 and len(line.strip())== 0 ):
            a.append( temp )
            temp = []
        else:
            temp.append( line.strip() )
    if( len(temp) != 0 ):
        a.append( temp )
        temp = []
    x = 0
    #print( a )
    for item in a:
        x += process( item )
    print( x )
main()
