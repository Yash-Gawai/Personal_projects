n = int(input("enter lines: "))
#for i in range (n):
#        print(" "*(n-i-1) + "#"*(i+1))

#****** OR ******#

c = "*"
for i in range(0,n+1):
        print((c*i).rjust(n))