#5
theInput = raw_input("Enter an integer: ")
#Your code here
#hahaa my code
theInput = int(theInput)
if(theInput%2==0):print "Even "
else:
    print "odd "

#6
primarySchAge = 4
legalVotingAge = 18
ageForPresidency = 40
retirementAge = 60
personsAge = input("Enter an age: ")

#check check
if personsAge < primarySchAge: print "Too young\n---------"

if personsAge >=legalVotingAge: print "Remember to vote\n---------"

if personsAge >=ageForPresidency: print "vote for me\n-----------"
elif personsAge< ageForPresidency: print "You can't vote\n------------"

if personsAge>= retirementAge: print "Too old\n-----------\n----------"

#7
#multiples of 3
i = 40
print "\n\nThe multiples of 3 from 40 all the way down to 0\n"
while i>=0:
    if (i%3==0):
        print  ". ",i
    i-=1

#8
#all numbers between 6 and 30 that are not divisible by 2,3 or 5.

k =6
print "\n\n All numbers between 6 and 30 that are not divisible by 2,3 or 5"
while k<=30:
    if (k%2 !=0 and k%3 !=0 and k%5 != 0):
        print ". ",k
    k+=1

#9
#finding the smallest positive n, such that 79*n/97 =1
i=1
#the least positive integer,n such that 79*n/97 has a rememder of one.
while i>0:
    if ((79*i)%97 ==1):
        print "\n\nleast positive n = ",i
        break
    i+=1
