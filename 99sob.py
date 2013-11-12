#===============================================================================
# 99 Slices of Beer
#-------------------------------------------------------------------------------
# Version: 1.0.1
# Updated: 11-11-2013
# Author: Alex Crawford
# License: MIT
#===============================================================================

s = 'bottles{0} {1} of beer on the wall{2} {3} {1} of beer.Take one down and ' \
    'pass it around, morebottleGo to the store and buy some more,'

f = [s[0:7], s[7:37], s[7:54], s[54:87], s[87:92], s[92:98], s[98:132]]

p, n, c = '.', '\n', ','

v = '{0} {1}{2}'

for b in range(99, 0, -1):
    if b > 1:
        print f[2].format(b, f[0], c, b, f[0])
        if b - 1 > 1:
            print v.format(f[3], f[1].format(b - 1, f[0], p), n)
        else:
            print v.format(f[3], f[1].format(b - 1, f[5], p), n)
    else:
        print f[2].format(b, f[5], c, b, f[5])
        print v.format(f[3], f[1].format('no' + f[4], f[0], p), n)
        print f[2].format('No' + f[4], f[0], c, 'no' + f[4])
        print v.format(f[6], f[1].format('99', f[0], p), n)