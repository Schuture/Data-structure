class Calculator():
    def postfix(self, s): # 把中缀表达式转换成后缀表达式
        output = [] # 不用字符串存储是因为会造成多位数字无法读取的问题
        stack = []
        order = {'+':0, '-':0, '*':1, '/':1, '(':-1} # 乘除优先级高于加减
        
        i = 0
        while i < len(s):
            if s[i] in '0123456789': # 可能读到长数字开头，要读完所有连续数字
                num = ''
                while i < len(s):
                    if s[i] in '0123456789':
                        num += s[i]
                        i += 1
                    else:
                        break
                output.append(int(num)) # 数字放入output中
                
            if i >= len(s): # 读完数字可能到了s末尾，不进行下一步操作符的判断了
                break
                
            if s[i] in '+-*/':
                if len(stack)>=1:
                    if order[s[i]] > order[stack[-1]]: # 放入比栈顶优先级更高的操作符
                        stack.append(s[i])
                    else: # 栈顶字符优先级较高或相同
                        while len(stack)>=1:
                            if order[s[i]] <= order[stack[-1]]: # 遍历优先级较高或相同的栈顶字符并弹出
                                output += stack.pop()
                            else:
                                break
                        stack.append(s[i]) # 先去掉优先级更高的再将运算符压入栈
                else:
                    stack.append(s[i])
                i += 1
                    
            if s[i]=='(':
                stack.append(s[i])
                i += 1
            if s[i]==')':
                while stack[-1]!='(':
                    output += [stack.pop()]
                stack.pop() # 弹出左括号，不放进output中
                i += 1
                
        while len(stack)>0: # 将栈中剩余的操作符弹出
            output += stack.pop()
        return output
    
    def calculate(self, s: str) -> int:
        '''用栈实现'''
        s = s.replace(' ','')
        s = self.postfix(s)
        print(s) # 输出后缀表达式
        stack = []
        for character in s:
            if isinstance(character, int):
                stack.append(character)
            elif character in '+-*/':
                b = stack.pop() # 后面的那个数
                a = stack.pop()
                if character == '+':
                    result = a + b
                elif character == '-':
                    result = a - b
                elif character == '*':
                    result = a * b
                elif character == '/':
                    result = a / b
                stack.append(result)
        return stack[0]
    
s = '1+2-3+4-5+(6-4+2)/3+4*2/(4+345)-32'
method = Calculator()
result = method.calculate(s)
print(result)













