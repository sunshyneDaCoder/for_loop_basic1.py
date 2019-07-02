# num 1 print all integers from 0 to 150

for x in range(0,151,1):
    print (x)
    


# num 2 print multiples of 5 from 5 to 1000

for y in range(5,1001,5):
    print (y)

# num 3 print intergers 1 to 100 if divisible by 5 print coding if divisible by 10 print coding dojo

for z in range(1,101,1):
    print (z)
    if ( z % 10 ==0):
        print ("coding dojo")
    elif (z % 5 ==0):
        print ("coding") 
        
# num 4 Add odd intergers and print final sum
sum = 0
for a in range(0,500001,1):
    if ( a % 2 == 1):
        sum = sum + a
print(sum) 

#count dofwn by fours from 2018 to 0

for b in range (2018,0,-4):
    print (b)

#flexible Counter

lownum = 2
highnum = 25
mult = 3
for c in range ( lownum,highnum,1):
    if (c % mult == 0 ):
        print (c)