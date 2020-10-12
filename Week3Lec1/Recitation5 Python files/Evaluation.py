class Empty(Exception):
    ''' Raise this class for exceptions '''
    pass

class ArrayStack:
    ''' Stack implemented with python list append/pop'''
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def is_empty(self):
        return len(self.array) == 0

    def push(self, e):
        self.array.append(e)

    def top(self):
        if self.is_empty():
            raise Empty()
        return self.array[-1]

    def pop(self):
        if self.is_empty():
            raise Empty()
        return self.array.pop(-1)

    def __repr__(self):
        return str(self.array)
    

def evaluate(string):
    """
    :param string: Str -- The string arithmetic expression input

    :return: Float -- the float answer for the given arithmetic expression.
    """
    operator_stack = ArrayStack()
    operand_stack = ArrayStack()
    table = {"+":2, "-":2, "*":3, "/":3, "(":1, ")":1}
    splitedStr = string.split()
    for a in splitedStr:
        if a =="1" or a =="2" or a =="3" or a =="4" or a =="5" or a =="6" or a =="7" or a =="8" or a =="9" or a =="10":
            operand_stack.push(int(a))
        else:
            if a == ")":
                while operator_stack.top() != "(":
                    a = operand_stack.pop()
                    b = operand_stack.pop()
                    c = operator_stack.pop()
                    if c =="+":
                        operand_stack.push(a+b)
                    elif c =="-":
                        operand_stack.push(b-a)
                    elif c =="*":
                        operand_stack.push(a*b)
                    else:
                        operand_stack.push(b/a)
                operator_stack.pop()

            else:
                operator_stack.push(a)
    while operator_stack.is_empty() == False :
        a = operand_stack.pop()
        b = operand_stack.pop()
        c = operator_stack.pop()
        #while table[c] >= table[operator_stack.top]:
        if c =="+":
            operand_stack.push(a+b)
        elif c =="-":
            operand_stack.push(b-a)
        elif c =="*":
            operand_stack.push(a*b)
        else:
            operand_stack.push(b/a)
    return operand_stack.top()

if __name__ == '__main__':
    print(evaluate("9 + 8 * ( 7 - 6 ) / ( 2 / 8 )"))  #41
    print(evaluate("9 + 8 * 7 / ( 6 + 5 ) - ( 4 + 3 ) * 2"))  # 0.0909090909
    print(evaluate("9 + 8 * 7 / ( ( 6 + 5 ) - ( 4 + 3 ) * 2 )")) # -9.66666666667
     
