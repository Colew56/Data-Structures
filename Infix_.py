class Stack:
    
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        return len(self.stack) == 0
        
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return print("cannot pop from empty stack")   
        
    def push(self,element):
        self.stack.append(element)
    
    def peek(self):
        return self.stack[-1]
   
   #define precedence function to assign numerical values to opertators
def precedence(c):
    
    if c == '^':
        return 3
    if c == '*' or c == '/':
        return 2
    if c == '+' or c == '-':
        return 1
    else:
        return -1

    #defines function to convert infix to postfix, uses empty string as argument
def infixtopostfix(infix_exp):
   
    #creates stack for the function 
    stack = Stack()
    #creates empty string for adding final result too 
    ans = ""
    
    for i in infix_exp:
        
        if i >= 'A' and i <= 'Z':# if I is an operand
            ans += i# add to string 
        
        elif i == '(':# if i is an open parenthesis
            stack.push(i)#push into stack 
        
        elif i == ')':#if i is a closed parenthesis 
            
            while stack and stack.peek() != '(':#iterates through stack until matching parenthesis is found 
                ans += stack.pop()#pops elements inbetween parenthesis
            stack.pop()#pops the open parenthesis 
         
        elif i == '–' or i == ' ':#error checking for spaces and invalid characters
            return print('Input expression containes spaces or invalid characters')
        
        #if i is an operator 
        elif i == '^' or i == '*' or i == '/' or i == '+' or i == '-':
            
            #gives left to right associativity by only popping operators if they have less precedence than the incoming operator            
            while not stack.isEmpty() and precedence(i) <= precedence(stack.peek()):
                ans += stack.pop()#pops operator with less precedence and appends them to ans using left right associativity
            stack.push(i)#appends operators which have higher precedence than the top of the stack 
    
    while not stack.isEmpty():
        ans += stack.pop()#will empty the rest of the stack and append it to the final output
         
    return ans #returns final postfix answer

    #defines function to convert postfit expression to prefix
def postfixtoprefix(postfix_exp):
    
    #creates new stack for this function 
    stack = Stack()
    
    for x in postfix_exp:
        #if x is operator 
        if x == '^' or x == '*' or x == '/' or x == '+' or x == '-':
            
            a= stack.pop()#pops top of stack
            b= stack.pop()#pops top of stack 
            temp = x + b + a #concatinates x with stack[-2] and stack[-1] to create prefix notation 
            stack.push(temp)#pushes temp variable into stack
            
        else:
            stack.push(x)#appends operands
                
    return stack.peek()#Returns whole prefix expression
    
    #define function to extract input files, and write to output file
def extractinputfiles(filename,outputfile):
   
   #opens and reads input file
    with open(filename, 'r') as file:
        lines = file.readlines() #makes lines equal to the lines in input file  
        with open(outputfile, 'w') as Infixoutputs:#opens and writes to InfixOutputs.txt
            for line in lines:#iterates through input file
                line = line.strip()#strips white spaces from lines  
                if line:#ignores blank spaces
                
                    postfix = infixtopostfix(line)#performs postfix conversion on input 
                    prefix = postfixtoprefix(postfix)#performs prefix conversion to postfix expression 
                    Infixoutputs.write(f"The original infix expression is: {line}\n")
                    Infixoutputs.write(f"The new prefix expression is: {prefix}\n")#writes to output file


extractinputfiles('InfixInputs.txt','InfixOutputs.txt')#calls function to execute on input file          
     
        
