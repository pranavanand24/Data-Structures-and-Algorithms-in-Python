class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # isEmpty

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False


    # push

    def push(self,value):
        self.list.append(value)
        return "the element has been successfully inserted"

    # pop

    def pop(self):
        if self.isEmpty():
            return "the element has been successfully inserted"

        else:
            return self.list.pop()

    # peek

    def peek(self):
        if self.isEmpty():
            return "there is not any element in the stack"

        else:
            return self.list[len(self.list)-1]

    # delete
    def delete(self):
        self.list = None
        



# Printing Accordingly

customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)

print(customStack)

customStack.pop()

customStack.peek()

print(customStack)



