import fileinput

def isValid( a ):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for i in a:
        arr = i.split(":")
        if( arr[0] in fields ):
            fields.remove( arr[0] )
        elif( arr[0] == "cid" ):
            continue
        else:
            print( "wtf" )
            return 0 #multiple occurences of one key
    if( len(fields) == 0 ):
        return 1 #passport is valid
    else:
        return 0
    
def main():
    a = []
    temp = []
    for line in fileinput.input():
        if( len(line.strip()) == 0 and len(temp) != 0 ): 
            a.append( temp )
            temp = []
        else:
            #print( line, end="")
            temp += line.split()
    count = 0
    for n in range( 0, len(a)):
        #print( a[n] )
        if( len(a[n]) < 7 ):
            count += 0
        elif( len(a[n]) == 7 ):
            count += isValid( a[n] )
        elif( len(a[n]) == 8 ):
            count += isValid( a[n] )
        else:
            print( "wtf" )
    print( count )
main()
