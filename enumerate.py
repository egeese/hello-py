numbers=[2,5,45,21, 62, 111,42]
even = 0
print numbers
for index, num in enumerate(numbers):
    if num%2==0:
        print "number %i is even" % (num)
        even+=1
        numbers[index]=num**2
else:
    print "%i numbers checked, %i even" % (len(numbers),even)
    print numbers

def factorial(x):
    result = 1
    for c in range(1,x+1):
        result*=c
    return result

print factorial(5)
