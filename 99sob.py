#===============================================================================
# 99 Slices of Beer
#-------------------------------------------------------------------------------
# Version: 1.0.0
# Updated: 10-11-2013
# Author: Alex Crawford
# License: MIT
#===============================================================================

s = '{0} {1} of beer on the wall{2} {3} {1} of beer.bottlesTake one down and ' \
'pass it around,noNo moreGo to the store and buy some more,bottle,.99\n'

f = [s[0:30], s[0:47], s[47:54], s[54:87], s[87:89], s[89:91], s[91:96],
     s[96:130], s[130:136], s[136:137], s[137:138], s[138:140], s[140:142]]

x = '{0} {1}{2}'

for b in range(99, 0, -1):
    if b > 1:
        print f[1].format(b, f[2], f[9], b, f[2])
        if b - 1 > 1:
            print x.format(f[3], f[0].format(b - 1, f[2], f[10]), f[12])
        else:
            print x.format(f[3], f[0].format(b - 1, f[8], f[10]), f[12])
    else:
        print f[1].format(b, f[8], f[9], b, f[8])
        print x.format(f[3], f[0].format(f[4] + f[6], f[2], f[10]), f[12])
        print f[1].format(f[5] + f[6], f[2], f[9], f[4] + f[6])
        print x.format(f[7], f[0].format(f[11], f[2], f[10]), f[12])