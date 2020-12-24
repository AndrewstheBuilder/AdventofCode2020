import fileinput, re
d = {}

def search( item ):
    v = d.get(item)
    result = 0

    if( isinstance( v, list ) ):
        for i in v :
            #base case
            if( d.get(i.replace(i[0], '').strip()) == None ):
                if( i == 'no other'):
                    return 0
                else:
                    return int(i[0])
            else:
                result += int(i[0]) + int(i[0])*search(i.replace(i[0], '').strip())
    else:
            #base case
            if( d.get(d.replace(v[0], '').strip()) == None ):
                if( i == 'no other'):
                    return 0
                else:
                    return int(i[0])
            else:
                result += int(v[0]) + int(v[0])*search(v.replace(v[0], '').strip())
    return result

def process(a):
    for i in range( 0, len(a) ):
        word = re.split("contain|,|\.", a[i])
        #print('Word ' + str(word) )
        #print( [x.replace('bags', '').replace('bag', '').strip() for x in word[1:len(word)] if x != ''] )
        d[word[0].replace('bags', '').strip()] = [ x.replace('bags', '').replace('bag', '').strip() for x in word[1:len(word)] if( x!='' and x!=' ')]
    #print( d )
    result = search( 'shiny gold' )
    return result

def main():
    a = []
    for line in fileinput.input():
        a.append( line.strip() )
    x = process(a)
    print( x )
main()
