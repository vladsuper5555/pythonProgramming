import math
import re
def problema1(numbers):
    gcd = numbers[0]
    for num in numbers[1:]:
        gcd = math.gcd(gcd, num)
    return gcd

def problema2(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def problema3(substring, string):
    return string.count(substring)

def problema4(camel_case_str):
    snake_case = ''
    for char in camel_case_str:
        if char.isupper():
            if len(snake_case) != 0: 
                snake_case += '_'
            snake_case += char.lower()
        else:
            snake_case += char
    return snake_case

def problema5(number):
    num_str = str(number)
    for i in range(len(num_str) // 2):
        if num_str[i] != num_str[-(i + 1)]:
            return False
    return True


def problema6(text):
    match = re.search(r'\d+', text)
    if match:
        return int(match.group())
    return None

def problema7(number):
    return bin(number).count('1')

def problema8(text):
    if not text:
        return 0
    words = text.split(' ')
    return len(words)

def main():
    input_numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [int(num) for num in input_numbers]
    print(problema1(numbers))
    print(problema2("Hello World!"))
    print(problema3("test", "This is a test string for testing purposes."))
    print(problema4("ThisIsAnExampleString"))
    print(problema5(12321))
    print(problema6("An apple is 123 USD."))
    print(problema7(24))
    print(problema8("I have Python exam"))

if __name__ == "__main__":
    main()
