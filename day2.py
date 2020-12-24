import fileinput
i = 0
for line in fileinput.input():
    a = line.split()
    num = a[0].split("-")
    numl = int(num[0])
    numm = int(num[1])
    l = a[1].split(":")
    if( a[2].count(l[0]) >= numl and a[2].count(l[0]) <= numm ):
        i += 1
print( i )
    
