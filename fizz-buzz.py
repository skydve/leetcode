# Write a program that outputs the string representation of numbers from 1 to n. But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

def fizzBuzz(n):
    m = [0, 0, 'Fizz', 0, 'Buzz', 'Fizz',
         0, 0, 'Fizz', 'Buzz', 0, 'Fizz', 0, 0, 'FizzBuzz']
    return [m[x%15-1] if m[x%15-1] else str(x) for x in range(1, n+1)]

print(fizzBuzz(30))