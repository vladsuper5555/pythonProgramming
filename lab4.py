import copy
class Stack: 
    
    def __init__(self):
        self.elements = []

    def push (self, element):
        self.elements.append(element)

    def pop (self):
        if len(self.elements) == 0:
            return None
        toReturn = self.elements[-1]
        self.elements = self.elements[:-1]
        return toReturn
    
    def peek(self):
        if len(self.elements) == 0:
            return None
        return self.elements[-1]

class Queue:
    def __init__(self):
        self.elements = []

    def push (self, element):
        self.elements.append(element)

    def pop (self):
        if len(self.elements) == 0:
            return None
        toReturn = self.elements[0]
        self.elements = self.elements[1:]
        return toReturn

    def peek(self):
        if len(self.elements) == 0:
            return None
        return self.elements[0]

class Matrix:
    
    def __init__(self, n, m) -> None:
        self.n = n
        self.m = m
        self.matrix = []
        for i in range(n):
            self.matrix.append([0 for _ in range(m)])

    def set(self, i, j, value):
        self.matrix[i][j] = value

    def get(self, i, j):
        if i >= self.n or j > self.m:
            return None
        return self.matrix[i][j]

    def transpose(self):
        matrixCopy = Matrix(self.m, self.n)

        for i in range(self.n):
            for j in range(self.m):
                matrixCopy.set(j, i, self.get(i, j))
        return matrixCopy
    
    def apply(self, lambdaExpression):
        for i in range (self.n):
            for j in range(self.m):
                self.set(i, j, lambdaExpression(self.get(i, j)))

    def multiply (self, otherMatrix):
        result = copy.deepcopy(self)

        for i in range(self.n):
            for j in range(otherMatrix.m):
                valuesSum = sum([self.get(i, k) * otherMatrix.get(k, j) for k in range(self.m)])
                result.set(i, j, valuesSum)

        return result


if __name__ == "__main__":
    # Test Stack class
    stack = Stack()
    print(stack.pop())  # Expected: None
    print(stack.peek())  # Expected: None
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.peek())  # Expected: 3
    print(stack.pop())   # Expected: 3
    print(stack.pop())   # Expected: 2
    print(stack.pop())   # Expected: 1
    print(stack.pop())   # Expected: None

    queue = Queue()
    print(queue.pop())  # Expected: None
    print(queue.peek())  # Expected: None
    
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.peek())  # Expected: 1
    print(queue.pop())   # Expected: 1
    print(queue.pop())   # Expected: 2
    print(queue.pop())   # Expected: 3
    print(queue.pop())   # Expected: None


    matrix = Matrix(2, 3)
    matrix.set(0, 0, 1)
    matrix.set(0, 1, 2)
    matrix.set(0, 2, 3)
    matrix.set(1, 0, 4)
    matrix.set(1, 1, 5)
    matrix.set(1, 2, 6)
    
    print(matrix.get(0, 0))  # Expected: 1
    print(matrix.get(1, 2))  # Expected: 6
    print(matrix.get(2, 2))  # Expected: None

    # Test transpose
    transposed = matrix.transpose()
    print(transposed.get(0, 1))  # Expected: 4
    print(transposed.get(1, 0))  # Expected: 2

    # Test matrix multiplication
    matrix2 = Matrix(3, 2)
    matrix2.set(0, 0, 1)
    matrix2.set(1, 1, 1)
    matrix2.set(2, 0, 1)
    product = matrix.multiply(matrix2)
    print(product.get(0, 0))  # Expected: 4
    print(product.get(1, 1))  # Expected: 5

    # Test apply method
    matrix.apply(lambda x: x * 2)
    print(matrix.get(0, 0))  # Expected: 2
    print(matrix.get(1, 1))  # Expected: 10