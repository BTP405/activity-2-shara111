# (10 points) Write a Python function `getPrimeNumbers(n)` which returns a list containing all prime numbers between 2 and _n_.  
# Create a helper function to determine if a particular number is prime and then use a comprehension to generate your list.

def getPrimeNumbers(n):
  # Write your code here
  prime = []
  for j in range(2, n+1): #iterates each number in J starting from 2 up to the including n (range function gts the last number which which is in this case 11)
    ok = True
    for i in range(2,j):
        if j%i == 0: #checks if J is divisible by i and if so, j is not a prime number
            ok = False
            break
    if ok:
      prime.append(j) #adds items at the end of the list itself
  return prime #returns the list
print(getPrimeNumbers(11)) #prints the list]

#Question answers