    #defines function for postfix conversion, uses empty string as argument 
def prefixtopostfix(pre_expression):
    
    #create an empty stack to be appended too
    stack = []
    
    for x in pre_expression:
        #if x in the prefix expression is an operator
        if x == '^' or x == '*' or x == '/' or x == '+' or x == '-':
            
            a= stack.pop()#pops the top of the stack
            b= stack.pop()#pops the top of the stack 
            temp = a + b + x #temp variable that concatenates the popped items to the operator at the end, creating post fix notation 
            stack.append(temp)#pushes temp variable into stack 
        
        elif x == '–' or x == ' ':#error checking for spaces and invalid characters
            return print('Input expression containes spaces or invalid characters')
        
        else:
            stack.append(x)#pushes operands into the stack 
    
    return stack [-1]# ensures that the top element of the stack is returned first 
    
    #defines function for infix conversion, uses empty string as argument
def prefixtoinfix(pre_expression):
    
    #creates new stack for this function 
    stack_infix = []
        
    for x in pre_expression:
        
        #if x in the prefix expression is an operator
        if x == '^' or x == '*' or x == '/' or x == '+' or x == '-':
           
            a= stack_infix.pop()#pop the top element 
            b= stack_infix.pop()#pop the top element 
            temp = a + x + b# temporary variable concatenates operator between the two popped elements, creating infix notation 
            stack_infix.append(temp)#pushes temporary variable into stack
        
        elif x == '–' or x == ' ':#error checking for spaces and invalid characters
            return print('Input expression containes spaces or invalid characters')
        
        else:
            stack_infix.append(x)#pushes operands into stack 
    
    return stack_infix [-1] #ensures that the top element of the stack is returned first     
        
    #define function to read from input.txt files and write to output.txt files  
def extractinputfiles(filename,outputfile):
    
    #reads from an open file 
    with open(filename, 'r') as file:
        lines = file.readlines()#reads all lines in the file  
        with open(outputfile, 'w') as Prefixoutputs:#opens and writes to PrefixOutputs.txt
            for line in lines:#iterates through txt file lines 
                line = line.strip()#removes white spaces from lines 
                if line:# skips empty lines   
                
                    pre_expression = line[::-1]#reverses the input string so that it can be read from left to right and still have the proper orientation within the stack  
                    postfix = prefixtopostfix(pre_expression)#calls on function to convert prefix to postfix   
                    infix = prefixtoinfix(pre_expression)#calls on function to convert prefix to infix 
                    Prefixoutputs.write(f"Postfix expression is: {postfix}\n")
                    Prefixoutputs.write(f"Infix expression is: {infix}\n")
                


extractinputfiles('Prefixinputs.txt','PrefixOutputs.txt')#calls on function to read input file 
pre_expression = ""#creates empty string which is the arument for the conversion functions