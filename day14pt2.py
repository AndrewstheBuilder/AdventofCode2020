import fileinput, copy

def find( b ):
    t = "".join(b)
    index = t.find('X')
    return index

def findAll( addr ):
    arr = []
    arr.append( addr )

    while( len(arr) != 0 ):
        binList = arr[0][:] #'[:]' slices list and makes a new copy instead of passing the reference
        index = find(binList)

        #find() returns -1 if 'X' is not found
        if( index != -1 ):
            binList[index] = '0'
            arr.append(binList[:])

            binList[index] = '1'
            arr.append(binList[:])
        else:
            return arr
        arr.pop(0)


def main():
    a = []
    for line in fileinput.input():
        a.append([i for i in line.split() if i != '='])
    mask = []
    addr = []
    mem = {}
    res = []
    for i in range( len(a) ):
        if( a[i][0] == 'mask' ):
            mask = a[i][1]
            res = []
        else :
            index = int(a[i][0].strip('mem[]'))
            addr = [char for char in '{0:036b}'.format(index)] #using 'list comprehension' to convert a number string to a list of binary numbers
            for j in range(len(mask)):
                if(mask[j] == 'X' or mask[j] == '1'):
                    addr[j] = mask[j]
            res = findAll( addr )

            #convert lists in res to ints
            for n in range(len(res)):
                 res[n] = "".join(res[n])
                 res[n] = int(res[n],2)

            for n in res:
                mem[n] = int(a[i][1])
        i += 1
    ans = sum(mem.values())
    print("Answer:", ans)
        
main()


"""
Block Comment
"""

