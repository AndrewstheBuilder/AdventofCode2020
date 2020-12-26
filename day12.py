import fileinput, re

def checkD( d1, d2, f, n ):
        if( f[0] == 'E' ):
            if( d1[0] == 'E' ):
                d1[1] += int(n)
            elif( d1[0] == 'W' ):
                d1[1] -= int(n)
                if( d1[1] < 0 ):
                    d1[0] = 'E'
                    d1[1] *= -1
        elif( f[0] == 'W' ):
            if( d1[0] == 'W' ):
                d1[1] += int(n)
            elif( d1[0] == 'E' ):
                d1[1] -= int(n)
                if( d1[1] < 0 ):
                    d1[0] = 'W'
                    d1[1] *= -1
        elif( f[0] == 'N' ):
            if( d2[0] == None ):
                d2[0] = 'N'
                d2[1] += int(n)
            elif( d2[0] == 'N' ):
                d2[1] += int(n)
            elif( d2[0] == 'S' ):
                d2[1] -= int(n)
                if( d2[1] < 0 ):
                    d2[0] = 'N'
                    d2[1] *= -1
        elif( f[0] == 'S' ):
            if( d2[0] == None ):
                d2[0] = 'S'
                d2[1] += int(n)
            elif( d2[0] == 'S' ):
                d2[1] += int(n)
            elif( d2[0] == 'N' ):
                d2[1] -= int(n)
                if( d2[1] < 0 ):
                    d2[0] = 'S'
                    d2[1] *= -1

        
def main():
    a = []
    for line in fileinput.input():
        a.append(line)
        
    f = ['E', 0] #direction ship is intially facing
    d1 = ['E', 0 ] #stores east/west
    d2 = [None, 0] #stores north/south
    for i in range( 0, len(a) ):
        if( a[i][0] == 'F' ):
            checkD(d1,d2,f,a[i][1:])
        elif( a[i][0] == 'E' ):
            if( d1[0] == 'E' ):
                d1[1] += int(a[i][1:])
            elif( d1[0] == 'W' ):
                d1[1] -= int(a[i][1:])
                if( d1[1] < 0 ):
                    d1[0] = 'E'
                    d1[1] *= -1
        elif( a[i][0] == 'W' ):
            if( d1[0] == 'W' ):
                d1[1] += int(a[i][1:])
            elif( d1[0] == 'E' ):
                d1[1] -= int(a[i][1:])
                if( d1[1] < 0 ):
                    d1[0] = 'W'
                    d1[1] *= -1
        elif( a[i][0] == 'N' ):
            if( d2[0] == None ):
                d2[0] = 'N'
                d2[1] += int(a[i][1:])
            elif( d2[0] == 'N' ):
                d2[1] += int(a[i][1:])
            elif( d2[0] == 'S' ):
                d2[1] -= int(a[i][1:])
                if( d2[1] < 0 ):
                    d2[0] = 'N'
                    d2[1] *= -1
        elif( a[i][0] == 'S' ):
            if( d2[0] == None ):
                d2[0] = 'S'
                d2[1] += int(a[i][1:])
            elif( d2[0] == 'S' ):
                d2[1] += int(a[i][1:])
            elif( d2[0] == 'N' ):
                d2[1] -= int(a[i][1:])
                if( d2[1] < 0 ):
                    d2[0] = 'S'
                    d2[1] *= -1
        elif( a[i][0] == 'R' ):
            f[1] += int(a[i][1:])
            f[1] = f[1] % 360
            if( f[1] == 0 ):
                f[0] = 'E'
            elif( f[1] == 90 ):
                f[0] = 'S'
            elif( f[1] == 180 ):
                f[0] = 'W'
            elif( f[1] == 270 ):
                f[0] = 'N'
        elif( a[i][0] == 'L' ):
            f[1] -= int(a[i][1:])
            f[1] += 360
            f[1] = f[1] % 360
            if( f[1] == 0 ):
                f[0] = 'E'
            elif( f[1] == 90 ):
                f[0] = 'S'
            elif( f[1] == 180 ):
                f[0] = 'W'
            elif( f[1] == 270 ):
                f[0] = 'N'
    print('Answer:' + str(d1[1] + d2[1]) )
    print( f, d1, d2 )
            
main()
"""
Block Comment
"""
