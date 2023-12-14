# Writing Numbers in Different Bases

## Introduction
Numbers can be represented in various base systems, with the decimal system (base-10) being the most commonly used. However, other bases like binary (base-2), octal (base-8), and hexadecimal (base-16) are also important, especially in fields like computer science. Understanding how to write numbers in different bases is a fundamental skill in mathematics.

## The Concept of Base Systems
A base system is a way of representing numbers using a set number of digits. The base indicates the number of unique digits, including zero, used to represent numbers.

- **Decimal (Base-10):** Uses digits 0-9.
- **Binary (Base-2):** Uses digits 0 and 1.
- **Octal (Base-8):** Uses digits 0-7.
- **Hexadecimal (Base-16):** Uses digits 0-9 and letters A-F (where A=10, B=11, C=12, D=13, E=14, F=15).

## Conversion Between Bases

### From Decimal to Other Bases
1. **To Binary:** Divide the decimal number by 2 and record the remainder. Repeat the process with the quotient until the quotient is 0. The binary number is the sequence of remainders read in reverse.
2. **To Octal:** Similar to binary, but divide by 8.
3. **To Hexadecimal:** Similar to binary, but divide by 16.

### From Other Bases to Decimal
Multiply each digit by its base raised to the power of its position (starting from 0) and sum the results.

## Examples

- Converting the decimal number 156 to binary:
  $$156_{10} = 10011100_2$$
- Converting the binary number 1011 to decimal:
  $$1011_2 = 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0 = 11_{10}$$

## Historical Context
The concept of base systems has been around for centuries. The decimal system, likely originated in India, gained widespread use due to its simplicity and practicality. Binary, octal, and hexadecimal systems have gained prominence with the advent of digital computers.

## Test Questions

1. Convert the decimal number 45 to a binary number.
2. What is the hexadecimal equivalent of the binary number 110101?
3. Convert the octal number 17 to a decimal number.

---

This note provides a foundational understanding of different base systems and their conversions, integral to many areas of mathematics and computer science. For further exploration, delve into specific applications in computing or the historical evolution of numeral systems.