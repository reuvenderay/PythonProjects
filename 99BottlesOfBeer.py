

beer = 99

while beer >= 0:
    if beer == 2:
        print beer, "bottles of beer on the wall,", beer, "bottles of beer."
        print "Take one down and pass it around,no more bottles of beer on the wall."

    elif beer == 1:
        print beer, "bottle of beer on the wall,", beer, "bottle of beer."
        print "Take one down and pass it around, no more bottles of beer on the wall."

    elif beer == 0:
        print "No more bottles of beer on the wall, no more bottles of beer."
        print "Go to the store and buy some more, 99 bottles of beer on the wall."

    else:
        print beer, "bottles of beer on the wall,", beer, "bottles of beer."
        print "Take one down and pass it around,", beer - 1, "bottles of beer on the wall."
    beer -= 1