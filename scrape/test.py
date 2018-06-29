class calculator:
    m_text_list = []

    def __init__(self):
        self.text_list=[]

    def sum_mul(self, choice, *args):
        if choice == "sum":
            result = 0
            for i in args:
                result = result + i
        elif choice == "mul":
            result = 1
            for i in args:
                result = result * i
        return result

class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            current = self.current
            self.current +=1
            return current
        else:
            raise StopIteration()

def YourRange(start, end):
    current = start
    while current<end:
        yield current
        current += 1
    return


################################################################
if __name__ == '__main__':
    cal = calculator()
    print('calculator instance = ',cal.sum_mul('mul',2,2,3))

for i in MyRange(0,5):
    print(i)

    print()
for i in YourRange(0, 5):
    print(i)
