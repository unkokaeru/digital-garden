# Greatest Common Divisor (GCD)

The Greatest Common Divisor (GCD), also known as the Greatest Common Factor (GCF) or Highest Common Factor (HCF), is a fundamental concept in number theory. It refers to the largest number that divides two or more integers without leaving a remainder.

## Understanding GCD

The GCD of two numbers is the largest positive integer that divides each of the numbers without leaving a remainder. For instance, the GCD of 8 and 12 is 4. 

### Historical Context

The concept of GCD dates back to ancient times and is prominently featured in Euclid's Elements. Euclid's algorithm, which he presented around 300 BCE, remains one of the most efficient methods for computing the GCD.

## Techniques for Finding the GCD

1. **Prime Factorization**: This involves breaking down each number into its prime factors. The GCD is the product of the highest power of common primes in the factorization of the numbers.

2. **Euclidean Algorithm**: A more efficient method, especially for large numbers, is the Euclidean Algorithm. This algorithm is based on the principle that the GCD of two numbers also divides their difference.

3. **Extended Euclidean Algorithm**: This is an extension of the Euclidean Algorithm that also finds integer coefficients x and y such that `GCD(a, b) = ax + by`.

4. **Consecutive Integer Checking Algorithm**: This is a less efficient method that involves checking each integer from 1 up to the smaller of the two numbers to see if it divides both numbers without a remainder.

5. **Binary GCD Algorithm**: This is an optimization of the Euclidean Algorithm that is more efficient on binary computers.

## Examples

1. **Prime Factorization**:
   - Find the GCD of 18 and 24.
   - Prime factorization of 18: 2 × 3²
   - Prime factorization of 24: 2³ × 3
   - GCD: 2 × 3 = 6

2. **Euclidean Algorithm**:
   - Find the GCD of 48 and 18.
   - 48 = 18 × 2 + 12
   - 18 = 12 × 1 + 6
   - 12 = 6 × 2
   - GCD: 6

## Test Questions

1. Use the prime factorization method to find the GCD of 20 and 30.
2. Apply the Euclidean Algorithm to find the GCD of 56 and 98.
3. What is the GCD of two prime numbers?

The study of GCD is essential in number theory and has applications in various fields, including cryptography, computer science, and algebra. Understanding different methods to find the GCD is crucial in mathematical problem-solving and computational efficiency.