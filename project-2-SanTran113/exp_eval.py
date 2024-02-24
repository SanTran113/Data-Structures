from stack_array import Stack

# You should not change this Exception class!
class PostfixFormatException(Exception):
    pass

def postfix_eval(inputelestr: str) -> float:
    """Evaluates a postfix expression"""
    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""
    newStr = inputelestr.split(" ")
    l = newStr
    s = Stack(32)
    opList = ["+", "-", "*", "**", "<<", ">>", "/", "//", "%"]
    for ele in l:
        # print(l)
        # print(ele)
        if l == ['']:
            raise PostfixFormatException("Insufficient operands")
        try:
            if ele not in opList:
                og = ele
                float(ele)
                s.push(og)
        except ValueError:
            raise PostfixFormatException("Invalid token")
        if ele in opList:
            try:
                x = s.pop()
                y = s.pop()
            except IndexError:
                raise PostfixFormatException("Insufficient operands")
            if ele == "+":
                value = float(x) + float(y)
                s.push(value)
            elif ele == "**":
                value = float(y) ** float(x)
                s.push(value)
            elif ele == "-":
                value = float(y) - float(x)
                s.push(value)
            elif ele == "/":
                if float(x) == 0:
                    raise PostfixFormatException("Insufficient operands")
                value = float(y) / float(x)
                s.push(value)
            elif ele == "//":
                if float(x) == 0:
                    raise PostfixFormatException("Insufficient operands")
                value = float(y) // float(x)
                s.push(value)
            elif ele == "<<":
                if x.isnumeric() is True and y.isnumeric() is True:
                    value = int(y) << int(x)
                    s.push(value)
                else:
                    raise PostfixFormatException("llegal bit shift operand")
            elif ele == ">>":
                if x.isnumeric() is True and y.isnumeric() is True:
                    value = int(y) >> int(x)
                    s.push(value)
                else:
                    raise PostfixFormatException("llegal bit shift operand")
            elif ele == "%":
                value = float(y) % float(x)
                s.push(value)
            elif ele == "*":
                value = float(y) * float(x)
                s.push(value)
    # except ZeroDivisionError:
    #     raise PostfixFormatException("Insufficient operands")
    print(f"stack: {s}")
    print(s.size())
    if s.size() > 1:
        raise PostfixFormatException("Too many operands")
    return s.peek()

def infix_to_postfix(inputelestr: str) -> str:
    """Converts an infix expression to an equivalent postfix expression"""
    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression """
    newStr = inputelestr.split(" ")
    l = ""
    s = Stack(32)
    RPN = Stack(32)
    opList = ["+", "-", "*", "**", "<<", ">>", "/", "//", "%"]
    pre_dict = {"(" : 0, ")": 0, "+": 1, "-": 1, "*": 2, "**": 3, "<<": 4, ">>": 4, "/": 2, "//": 2, "%": 2}
    for ele in newStr:
        if ele == "(":
            s.push(ele)
        elif ele == ")":
            while "(" in s.items:
                x = s.pop()
                if x != "(":
                    RPN.push(x)
                elif x == "(":
                    break
        elif ele in opList:
            if s.num_items >= 1:
                o1 = ele
                o2 = s.pop()
                s.push(o2)
                if (o1 != "**" and pre_dict.get(o1) <= pre_dict.get(o2)) or \
                        (o1 == "**" and pre_dict.get(o1) < pre_dict.get(o2)):
                    o2 = s.pop()
                    RPN.push(o2)
                s.push(o1)
            else:
                s.push(ele)
        elif type(float(ele)) is float:
            RPN.push(ele)
    while s.num_items != 0:
        x = s.pop()
        RPN.push(x)
    for ele in RPN.items:
        if ele is not None:
            l = l + " " + ele
    return l.strip()

def prefix_to_postfix(inputelestr: str) -> str:
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression(tokens are space separated)"""
    newStr = inputelestr.split(" ")
    l = newStr
    s = Stack(32)
    opList = ["+", "-", "*", "**", "<<", ">>", "/", "//", "%"]
    for ele in l[::-1]:
        if ele in opList:
            print("op push")
            operator = ele
            op1 = s.pop()
            op2 = s.pop()
            str = op1 + " " + op2 + " " + operator
            s.push(str)
        elif type(float(ele)) is float:
            s.push(ele)
            print("num push")
    postfix_eval(s.items[0])
    return s.items[0]






