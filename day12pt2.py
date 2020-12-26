import fileinput, re

# if I had said east, north was positive and west and south were negative my implementation would have been easier
def checkD( d1, d2, f, n ):
        if( f[0] == 'E' ):
            if( d1[0] == 'E' ):
                d1[1] += f[1] * int(n)
            elif( d1[0] == 'W' ):
                d1[1] -= f[1] * int(n)
                if( d1[1] < 0 ):
                    d1[0] = 'E'
                    d1[1] *= -1
        elif( f[0] == 'W' ):
            if( d1[0] == 'W' ):
                d1[1] += f[1] * int(n)
            elif( d1[0] == 'E' ):
                d1[1] -= f[1] * int(n)
                if( d1[1] < 0 ):
                    d1[0] = 'W'
                    d1[1] *= -1
        elif( f[0] == 'N' ):
            if( d2[0] == 'N' ):
                d2[1] += f[1] * int(n)
            elif( d2[0] == 'S' ):
                d2[1] -= f[1] * int(n)
                if( d2[1] < 0 ):
                    d2[0] = 'N'
                    d2[1] *= -1
        elif( f[0] == 'S' ):
            if( d2[0] == 'S' ):
                d2[1] += f[1] * int(n)
            elif( d2[0] == 'N' ):
                d2[1] -= f[1] * int(n)
                if( d2[1] < 0 ):
                    d2[0] = 'S'
                    d2[1] *= -1

        if( f[2] == 'N' ):
            if( d2[0] == 'N' ):
                d2[1] += f[3] * int(n)
            elif( d2[0] == 'S' ):
                d2[1] -= f[3] * int(n)
                if( d2[1] < 0 ):
                    d2[0] = 'N'
                    d2[1] *= -1
        elif( f[2] == 'S' ):
            if( d2[0] == 'S' ):
                d2[1] += f[3] * int(n)
            elif( d2[0] == 'N' ):
                d2[1] -= f[3] * int(n)
                if( d2[1] < 0 ):
                    d2[0] = 'S'
                    d2[1] *= -1
        elif( f[2] == 'E' ):
            if( d1[0] == 'E' ):
                d1[1] += f[3] * int(n)
            elif( d1[0] == 'W' ):
                d1[1] -= f[3] * int(n)
                if( d1[1] < 0 ):
                    d1[0] = 'E'
                    d1[1] *= -1
        elif( f[2] == 'W' ):
            if( d1[0] == 'W' ):
                d1[1] += f[3] * int(n)
            elif( d1[0] == 'E' ):
                d1[1] -= f[3] * int(n)
                if( d1[1] < 0 ):
                    d1[0] = 'W'
                    d1[1] *= -1      

        
def main():
    a = []
    for line in fileinput.input():
        a.append(line)
    f = ['E', 10, 'N', 1]   #waypoint: f[0:1] stores east waypoint intially, f[2:3] stores north waypoint intially
    comp = [0, 270]         #my compass: east:0 degrees, west:180, south:90, and north:270 degrees
                            #(comp[0] corresponds to f[0:1] and comp[1] corresponds to f[2:3])
    
    #distance ship has traveled
    d1 = ['E', 0 ]          #stores east/west
    d2 = ['N', 0]           #stores north/south
    
    for i in range( 0, len(a) ):
        if( a[i][0] == 'F' ):
            checkD(d1,d2,f,a[i][1:])
        elif( a[i][0] == 'E' ):
            if( f[0] == 'E' ):
                f[1] += int(a[i][1:])
            elif( f[0] == 'W' ):
                f[1] -= int(a[i][1:])
                if( f[1] < 0 ):
                    f[0] = 'E'
                    comp[0] = 0
                    f[1] *= -1
            elif( f[2] == 'E' ):
                f[3] += int(a[i][1:])
            elif( f[2] == 'W' ):
                f[3] -= int(a[i][1:])
                if( f[3] < 0 ):
                    f[2] = 'E'
                    comp[1] = 0
                    f[3] *= -1
        elif( a[i][0] == 'W' ):
            if( f[0] == 'W' ):
                f[1] += int(a[i][1:])
            elif( f[0] == 'E' ):
                f[1] -= int(a[i][1:])
                if( f[1] < 0 ):
                    f[0] = 'W'
                    comp[0] = 180
                    f[1] *= -1
            elif( f[2] == 'W' ):
                f[3] += int(a[i][1:])
            elif( f[2] == 'E' ):
                f[3] -= int(a[i][1:])
                if( f[3] < 0 ):
                    f[2] = 'W'
                    comp[1] = 180
                    f[3] *= -1
        elif( a[i][0] == 'N' ):
            if( f[2] == 'N' ):
                f[3] += int(a[i][1:])
            elif( f[2] == 'S' ):
                f[3] -= int(a[i][1:])
                if( f[3] < 0 ):
                    f[2] = 'N'
                    comp[1] = 270
                    f[3] *= -1
            elif( f[0] == 'N' ):
                f[1] += int(a[i][1:])
            elif( f[0] == 'S' ):
                f[1] -= int(a[i][1:])
                if( f[1] < 0 ):
                    f[0] = 'N'
                    comp[0] = 270
                    f[1] *= -1
        elif( a[i][0] == 'S' ):
            if( f[2] == 'S' ):
                f[3] += int(a[i][1:])
            elif( f[2] == 'N' ):
                f[3] -= int(a[i][1:])
                if( f[3] < 0 ):
                    f[2] = 'S'
                    comp[1] = 90
                    f[3] *= -1
            elif( f[0] == 'S' ):
                f[1] += int(a[i][1:])
            elif( f[0] == 'N' ):
                f[1] -= int(a[i][1:])
                if( f[1] < 0 ):
                    f[0] = 'S'
                    comp[0] = 90
                    f[1] *= -1
        elif( a[i][0] == 'R' ):
            comp[0] += int(a[i][1:])
            comp[1] += int(a[i][1:])
            comp[0] = comp[0] % 360
            comp[1] = comp[1] % 360
            if( comp[0] == 0 ):
                f[0] = 'E'
            elif( comp[0] == 90 ):
                f[0] = 'S'
            elif( comp[0] == 180 ):
                f[0] = 'W'
            elif( comp[0] == 270 ):
                f[0] = 'N'

            if( comp[1] == 0 ):
                f[2] = 'E'
            elif( comp[1] == 90 ):
                f[2] = 'S'
            elif( comp[1] == 180 ):
                f[2] = 'W'
            elif( comp[1] == 270 ):
                f[2] = 'N'
        elif( a[i][0] == 'L' ):
            comp[0] -= int(a[i][1:])
            comp[0] += 360
            comp[0] = comp[0] % 360
            comp[1] -= int(a[i][1:])
            comp[1] += 360
            comp[1] = comp[1] % 360
            if( comp[0] == 0 ):
                f[0] = 'E'
            elif( comp[0] == 90 ):
                f[0] = 'S'
            elif( comp[0] == 180 ):
                f[0] = 'W'
            elif( comp[0] == 270 ):
                f[0] = 'N'
                
            if( comp[1] == 0 ):
                f[2] = 'E'
            elif( comp[1] == 90 ):
                f[2] = 'S'
            elif( comp[1] == 180 ):
                f[2] = 'W'
            elif( comp[1] == 270 ):
                f[2] = 'N'
        print( 'For instruction:',a[i],end="" )
        print("Waypoint:", f, "Ship after instruction:", d1, d2 )
        print("Compass:", comp )
        print()
    print('Answer:' + str(d1[1] + d2[1]) )
    #print( f, d1, d2, comp )
          
main()

"""
Block Comment
"""
