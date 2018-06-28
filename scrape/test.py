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

if __name__ == '__main__':
    cal = calculator()
    print('calculator instance = ',cal.sum_mul('mul',2,2,3))