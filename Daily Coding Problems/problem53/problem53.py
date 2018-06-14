class Queue():
    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, item):
        # Push all of the contents of the first stack into the second stack
        while len(self.stack) != 0:
            self.temp.append(self.stack.pop())

        self.stack.append(item)

        # Push everything back onto the original queue
        while len(self.temp) != 0:
            self.stack.append(self.temp.pop())

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            self.stack.pop()

    def size(self):
        return len(self.stack)
    
    def peek(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

def main():
    queue = Queue()

    for i in range(10):
        queue.push(i)

    for i in range(queue.size()):
        print(queue.pop())

if __name__ == '__main__':
    main()
