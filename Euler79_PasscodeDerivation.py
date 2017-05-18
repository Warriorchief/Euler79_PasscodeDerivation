"""Euler79_PasscodeDerivation
    A common security method used for online banking is to ask the user for three
random characters from a passcode. For example, if the passcode was 531278, 
they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
     Given that the three characters are always asked for in order,determine the
shortest possible secret passcode of unknown length.
"""
with open('Euler79_helper.txt') as f:
    codes=[line[:-1] for line in f]
    arr=[[int(c) for c in codes[i]] for i in range(len(codes))]
    firsts=set([a[0] for a in arr])#--> {1, 2, 3, 6, 7, 8}
    secs=set([a[1] for a in arr])  #--> {1, 2, 3, 6, 8, 9}
    thirds=set([a[2] for a in arr])#--> {0, 1, 2, 6, 8, 9}         
"""
print(arr)
[[3, 1, 9], [6, 8, 0], [1, 8, 0], [6, 9, 0], [1, 2, 9], [6, 2, 0], [7, 6, 2], [6, 8, 9],
 [7, 6, 2], [3, 1, 8], [3, 6, 8], [7, 1, 0], [7, 2, 0], [7, 1, 0], [6, 2, 9], [1, 6, 8],
 [1, 6, 0], [6, 8, 9], [7, 1, 6], [7, 3, 1], [7, 3, 6], [7, 2, 9], [3, 1, 6], [7, 2, 9],
 [7, 2, 9], [7, 1, 0], [7, 6, 9], [2, 9, 0], [7, 1, 9], [6, 8, 0], [3, 1, 8], [3, 8, 9],
 [1, 6, 2], [2, 8, 9], [1, 6, 2], [7, 1, 8], [7, 2, 9], [3, 1, 9], [7, 9, 0], [6, 8, 0],
 [8, 9, 0], [3, 6, 2], [3, 1, 9], [7, 6, 0], [3, 1, 6], [7, 2, 9], [3, 8, 0], [3, 1, 9],
 [7, 2, 8], [7, 1, 6]]
"""
#uses the eight digits {0,1,2,3,6,7,8,9}
startsWithOne=[[a[1],a[2]] for a in arr if a[0]==1]#-->  {0,2,6,8}
startsWithTwo=[[a[1],a[2]] for a in arr if a[0]==2]#-->  {0,8,9}
startsWithThree=[[a[1],a[2]] for a in arr if a[0]==3]#--> {1,2,6,8,9}
startsWithSix=[[a[1],a[2]] for a in arr if a[0]==6]#--> {0,2,8,9}
#startsWithSeven=[[a[1],a[2]] for a in arr if a[0]==7]#--> {0,1,2,6,8,9}
startsWithEight=[[a[1],a[2]] for a in arr if a[0]==8]#--> {0,9}
#THAT 7 ONLY EVER APPEARS IN THE FIRST SLOT HINTS AT THE FACT THAT THE CODE STARTS WITH 7
#ALSO CAN GUESS THAT ENDS IN EITHER 9 OR 0 BASED ON THOSE BEING MOST COMMON LAST 
#PLAYING AROUND BY HAND BELOW
"""
A     B     C     D     E     F     G     H
7     3     1     6     2     8     9     0
"""
#73162890 --> 