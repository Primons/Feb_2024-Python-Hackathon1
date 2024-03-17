def fibonacci_sequence(n):
    sequence = []
    if n == 1:
        sequence = [0]
    elif n >= 2:
        sequence = [0, 1]
        for i in range(2, n):
            sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence

n = int(input("Enter the value of n: "))

fib_sequence = fibonacci_sequence(n)
    
print("Generated Fibonacci sequence:")
print(fib_sequence)
