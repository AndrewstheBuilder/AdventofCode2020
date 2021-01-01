import fileinput


def main():
    a = []
    for line in fileinput.input():
        a.append([i for i in line.split() if i != '='])
    mask = ""
    mem = {}
    for i in range( len(a) ):
        if( a[i][0] == 'mask' ):
            string = a[i][1]
            mask = [[string[x], x] for x in range(len(string)) if(string[x] != 'X')]
        else :
            index = int(a[i][0].strip('mem[]'))
            binNum = [char for char in '{0:036b}'.format(int(a[i][1]))]
            for x in mask: 
                binNum[x[1]] = x[0]
            binNum = ''.join(binNum)
            mem[index] = int(binNum, 2)
            #print(mem[index])
        i += 1
    ans = sum(mem.values())
    print("Answer:", ans)
        
main()

"""
Block Comment
"""
