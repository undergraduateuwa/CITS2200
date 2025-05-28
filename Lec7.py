
class Stack :

    def __init__(self):
        self.data = []

    def push(self,num):
        self.data.append(num)

    def peek(self):
        if self.empty():
            return self.data[-1]

    def empty(self):
        return len(self.data)!=0

    def pop(self):
        if self.empty():

            return self.data.pop()




def Parentheses_Matching(str):
    stack = Stack()
    dic = {
        ')': '(',
        ']':'[' ,
        '}' : '{'

    }
    for char in str:
        if char in dic.values():
            stack.push(char)

        elif char in dic.keys():
            if dic[char] != stack.peek():
                return False
            else:
                stack.pop()

    return not stack.empty()



if __name__ == "__main__":
    test1 = [
        ("(xdfsdfs)sdfsdf", True),
        ("()[sdf]s{s}", True),
        ("(]", False),
        ("([{}])", True),
        ("([)]", False),
        ("", True),
        ("{[()()]}", True),
        ("{[(])}", False),
    ]

    for s, expected in test1:
        print(s, Parentheses_Matching(s), "expected:", expected)

    test2 = [
        ("<html><body><h1>Title</h1></body></html>", True),
        ("<div><p>Hi</div></p>",                     False),
        ("<ul><li>One<li>Two</li></ul>",             False),
        ("<br/><img src='a.png'/>",                  True),
        ("<a href='#'>Link</a><span>Text</span>",    True),
        ("<div><span>Nested</span>",                 False),
    ]







