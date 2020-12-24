import fileinput, re
d = {}

#searches values and returns number of keys recursively
#example: if gold is in green is in blue search( gold ) will return that gold can be in two bags
#example cont: green and blue can contain gold
def search( item ):
    result = []
    if( len(item) == 0 ):
        return 0
    for k, v in d.items():
        #print( v )
        if( isinstance( item, list ) ):
            for i in range(0, len(item)):
                #print ( i )
                if( item[i] in v and k not in result ):
                    result.append( k )
        elif( item in v and k not in result):
            result.append( k )
    #print( item )
    for k in result:
        d.pop( k, None ) #for part 1 count number of bags that can hold at least one 'shiny gold'
    return len(result) + search( result )

def process(a):
    for i in range( 0, len(a) ):
        word = re.split("\d|contain|,|\.", a[i])
        #print('Word ' + str(word) )
        #print( [ x.replace('bags', '').replace('bag', '').strip() for x in word[1:len(word)] if x != ' '] )
        d[word[0].replace('bags', '').strip()] = [ x.replace('bags', '').replace('bag', '').strip() for x in word[1:len(word)] if( x != ' ' )]
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
