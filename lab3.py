import math
import copy


def problema1(listA, listB):
    setA, setB = set(listA), set(listB)
    return [setA & setB, setA | setB, setA - setB, setB - setA]



def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def problema2(lista):
    dictionary = {}
    for char in lista:
        if char in dictionary.keys():
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary


def problema3(dictionary1, dictionary2):
    if type(dictionary1) != type(dictionary2):
        return False
    if not isinstance(dictionary1, dict):
        # we try to process as list else it means they are normal values (int) and we can compare normally
        try:

            dictionary1 = list(dictionary1)
            dictionary2 = list(dictionary2)

            if len(dictionary1) != len(dictionary2):
                return False

            for index, value in enumerate(dictionary1):
                if dictionary1[index] != dictionary2[index]:
                    return False
        except: 
            return dictionary2 == dictionary1

    if isinstance(dictionary1, dict):
        for key in dictionary1.keys():
            if not key in dictionary2:
                return False
            res = problema3(dictionary1[key], dictionary2[key])
            if res == False:
                return False

    return True

def problema4(tag, content, **attributes):
    return f'<{tag} {"".join(f"{key} = {chr(34)}{attributes[key]}{chr(34)} " for key in attributes.keys())}>{content}</{tag}>'


def problema5(rules, d):
    rules_dict = {}
    for rule in rules:
        rules_dict[rule[0]] = (rule[1], rule[2], rule[3])
    for key, value in d.items():
        if not key in rules_dict.keys():
            return False
        if len(value) == 0:
            continue
        rule = rules_dict[key]
        try:
            index1 = value.index(rule[0], 0, len(rule[0]))
            index2 = value.index(rule[1], 1, len(value) - len(rule[1]) - 1)
            index3 = value.index(rule[2], len(value) - len(rule[2]), len(value))
        except:
            return False
    return True

def problema6(list):
    return (len(set(list)), len(list) - len(set(list)))

def problema7(*sets):
    dict = {}
    for index1, value in enumerate(sets):
        for index2, value in enumerate(sets):
            if index1 < index2:
                set1 = sets[index1]
                set2 = sets[index2]
                dict[f'{set1} | {set2}'] = set1 | set2
                dict[f'{set1} & {set2}'] = set1 & set2
                dict[f'{set1} - {set2}'] = set1 - set2
                dict[f'{set2} - {set1}'] = set2 - set1
    return dict

def problema8(dict):
    currentValue = dict['start']
    foundValues = [currentValue]
    currentValue = dict[currentValue]
    while not currentValue in foundValues:
        foundValues.append(currentValue)
        currentValue = dict[currentValue]
    return foundValues

def problema9(*list, **dict):
    return sum(1 for el in list if el in dict.values())
    
if __name__ == "__main__":
    # Test for problema1
    print(problema1([1, 2, 3], [2, 3, 4]))  # Expected: [{2, 3}, {1, 2, 3, 4}, {1}, {4}]

    # Test for problema2
    print(problema2("Ana has apples."))  
    # Expected: {'A': 1, 'n': 1, 'a': 3, ' ': 2, 'h': 1, 's': 2, 'p': 2, 'l': 1, 'e': 1, '.': 1}

    # Test for problema3
    d1 = {'a': 1, 'b': {'c': 3, 'd': [1, 2, 3]}}
    d2 = {'a': 1, 'b': {'c': 3, 'd': [1, 2, 3]}}
    print(problema3(d1, d2))  # Expected: True

    # Test for problema4
    print(problema4("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))
    # Expected: '<a href="http://python.org" _class="my-link" id="someid">Hello there</a>'

    # Test for problema5
    rules = {("key1", "", "inside", ""), ("key2", "start", "something", "winter")}
    dictionary = {"key1": "come inside, it's too cold out", "key2": "start something in winter", "key3": "asdoinasdl"}
    print(problema5(rules, dictionary))  # Expected: True

    # Test for problema6
    print(problema6([1, 2, 3, 2, 4, 4, 5]))  # Expected: (5, 2)

    # Test for problema7
    print(problema7({1, 2}, {2, 3}))  
    # Expected: {
    #    "{1, 2} | {2, 3}": {1, 2, 3},
    #    "{1, 2} & {2, 3}": {2},
    #    "{1, 2} - {2, 3}": {1},
    #    "{2, 3} - {1, 2}": {3}
    # }

    # Test for problema8
    mapping = {'start': 'a', 'a': '6', '6': 'z', 'z': '2', '2': '2'}
    print(problema8(mapping))  # Expected: ['a', '6', 'z', '2']

    # Test for problema9
    print(problema9(1, 2, 3, 4, x=1, y=2, z=3, w=5))  # Expected: 3
