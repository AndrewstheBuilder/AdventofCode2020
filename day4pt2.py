import fileinput,re

def hclCorrect( s ):
    for i in s:
        if( i.isdigit() ):
            i = int(i)
            if( i < 0 or i > 9 ):
                return False
        else:
            if( ord(i) < 97 or ord(i) > 102 ):
                return False
    return True

def isValid( a ):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    x = 0
    for i in a:
        arr = i.split(":")
        if( arr[0] == "byr" ):
            fields.remove(arr[0])
            x = int(arr[1])
            if( x < 1920 or x > 2002 ):
                return 0
        elif( arr[0] == "iyr" ):
            fields.remove(arr[0])
            x = int(arr[1])
            if( x < 2010 or x > 2020 ):
                return 0
        elif( arr[0] == "eyr" ):
            fields.remove(arr[0])
            x = int(arr[1])
            if( x < 2020 or x > 2030 ):
                return 0
        elif( arr[0] == "hgt" ):
            fields.remove(arr[0])
            c = arr[1].split("cm")
            if( not(c[0].isdigit()) ):
                c = arr[1].split("in")
                if( int(c[0]) < 59 or int(c[0]) > 76 ):
                    return 0
            else:
                if( int(c[0]) < 150 or int(c[0]) > 193 ):
                    return 0
        elif( arr[0] == "hcl" ):
            fields.remove(arr[0])
            if( arr[1][0] == "#" ):
                s = re.split("#", arr[1] )
                if( hclCorrect(s[1]) and len(s[1]) == 6 ):
                    continue
                else:
                    return 0
            else:
                return 0
        elif( arr[0] == "ecl" ):
            fields.remove(arr[0])
            ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if(arr[1] in ecl ):
                continue
            else:
                return 0
        elif( arr[0] == "pid" ):
            fields.remove(arr[0])
            if( arr[1].isdigit() and len(arr[1]) == 9 ):
                continue
            else:
                return 0
        elif( arr[0] == "cid" ):
            continue
        else:
            print( "WTF!!!!!!" )
    if( len(fields) == 0 ):
        return 1 #valid passport
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
