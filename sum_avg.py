#Program to find Sum and Average of N Natural Numbers - FOR loop
 
num=int(input("Enter any Number"))
sum=0

for value in range(1,num+1):
    sum=sum+value

avg=sum/num

print("The Sum of Natural Numbers from 1 to {0} =  {1}".format(num,sum))
print("Average of Natural Numbers from 1 to {0} =  {1}".format(num,avg))


#Program to find Sum and Average of N Natural Numbers - WHILE loop
 
num=int(input("Enter any Number"))

sum=0
value=1

while(value<=num):
    sum=sum+value
    value=value+1

avg=sum/num

print("The Sum of Natural Numbers from 1 to {0} =  {1}".format(num,sum))
print("Average of Natural Numbers from 1 to {0} =  {1}".format(num,avg))
