#Find the sum of all the multiples of 3 or 5 below 1000.
sum = 0                 
iterative = 0

while iterative < 1000:     #Loop through all 1000 iterables, see if it's evenly divisable by 5 or 3, add it to sum if it is
    if iterative % 5 == 0 or iterative % 3 == 0:
        sum += iterative
    iterative += 1

print(sum)