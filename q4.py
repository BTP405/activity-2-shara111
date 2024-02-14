# (25 points) Write a Python function printStats(t) which retrives data in a text 
# file t which reads in lines of numbers. For each line read in, the function 
# must call a decorator function which prints

# the numbers read
# the count of the numbers read
# the average of the numbers
# the maximum of the numbers

def printStats(t):
        
      #defining a decorator
    def print_stats_decorator(func):
            #wrapper function
            def wrapper(*args, **kwargs):  # This allows the wrapper to accept any number of arguments
                  numbers = func(*args, **kwargs)
                  count = len(numbers)
                  average = sum(numbers) / count
                  maximum = max(numbers)

                  print("Numbers:", numbers)
                  print("Count", count)
                  print("Average", average)
                  print("Maximum", maximum)

                  return numbers, count, average, maximum #returning the result of the function
            return wrapper

    with open(t, 'r') as file:
      for line in file:
            numbers = [int(x) for x in line.split()] #converting strings to numbers

            @print_stats_decorator
            def my_function():
                  return numbers
             
            results = my_function() #calling the decoratorated function
    return results


#Example usage
results = printStats("numbers.txt")

      
