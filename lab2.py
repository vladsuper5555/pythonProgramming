import math
import copy


def problema1(n):
    fibo = [0, 1]
    for i in range(2, n + 1):
        fibo.append(fibo[i - 1] + fibo[i - 2])
    return fibo


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def problema2(lista):
    return [a for a in lista if isPrime(a)]


def problema3(listA, listB):
    listA = set(listA)
    listB = set(listB)

    return [listA | listB, listA & listB, listA - listB, listB - listA]


def problema4(notes, moves, start):
    currentIndex = start
    answer = []
    for move in moves:
        answer.append(notes[currentIndex])
        currentIndex += move
        currentIndex %= len(notes)
    answer.append(notes[currentIndex])
    return answer


def problema5(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if j < i:
                matrix[i][j] = 0
    return matrix


def problema6(*lists, number):
    counts = {}
    for _list in lists:
        for element in _list:
            if not element in counts:
                counts[element] = 1
            else:
                counts[element] += 1
    answer = []
    for element in counts:
        if counts[element] == 2:
            answer.append(element)
    return answer


def isPalindrome(number):
    reverse = 0
    copy = number

    while number:
        reverse = reverse * 10 + number % 10
        number = number // 10
    print(copy, reverse)
    return copy == reverse


def problema7(_list):
    greatest = _list[0]
    count = 0
    for element in _list:
        if isPalindrome(element):
            count += 1
            greatest = max(greatest, element)
    return (count, greatest)


def problema8(x=1, _list=[], flag=True):
    responses = []
    for element in _list:
        responses.append([])
        print(element)
        for letter in element:
            if ord(letter) % x == 0 and flag:
                responses[len(responses) - 1].append(letter)
            elif ord(letter) % x != 0 and not flag:
                responses[len(responses) - 1].append(letter)
    return responses


def problema9(matrix):
    maxMatrix = copy.deepcopy(matrix)
    answers = []
    for line in range(1, len(matrix)):
        for col in range(0, len(matrix[0])):
            if matrix[line][col] <= maxMatrix[line - 1][col]:
                answers.append((line, col))
            maxMatrix[line][col] = max(maxMatrix[line - 1][col], matrix[line][col])


    return answers

def problema10(*lists):
    answers = []
    
    max_number_of_elements = 0
    for _list in lists:
        max_number_of_elements = max(max_number_of_elements, len(_list))
        
    for index in range(0, max_number_of_elements):
        answers.append([])
        
    for index in range(0, max_number_of_elements):
        for _list in lists:
            if index < len(_list):
                answers[index].append(_list[index])
            else:
                answers[index].append(None)
    
    return answers

from functools import cmp_to_key

def custom_comparator(tuple1, tuple2):
    if tuple1[1][2] < tuple2[1][2]:
        return -1
    return 1

def problema11(tuples): 
    tuples.sort(key = cmp_to_key(custom_comparator))
    return tuples

def problema12(words): 
    dictionary = {}
    
    for word in words:
        lastTwo = word[-2:]
        if not (lastTwo in dictionary):
            dictionary[lastTwo] = []
        dictionary[lastTwo].append(word)
    answers = []
    for key in dictionary:
        answers.append(dictionary[key])
    return answers
    
if __name__ == "__main__":
    print(problema1(20))
    print(problema2([5, 6, 8, 11]))
    print(problema3([1, 2, 3, 4], [3, 4, 5, 6]))
    print(problema4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
    print(
        problema5(
            [
                [2, 3, 5],
                [5, 6, 7],
                [1, 2, 4],
            ]
        )
    )
    print(problema6([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], number=2))
    print(problema7([1, 2, 4, 11, 123321, 423, 2]))
    print(problema8(2, ["test", "hello", "lab002"], flag=False))
    print(
        problema9(
            [
                [1, 2, 3, 2, 1, 1],
                [2, 4, 4, 3, 7, 2],
                [5, 5, 2, 5, 6, 4],
                [6, 6, 7, 6, 7, 5],
            ]
        )
    )
    
    print(problema10([1,2,3], [5,6,7], ["a", "b", "c"]))
    print(problema11([('abc', 'bcd'), ('abc', 'zza')]))
    print(problema12(['ana', 'banana', 'carte', 'arme', 'parte']))