    #defines function to convert postfixtoprefix, uses empty string as argument
def postfixtoprefix(post_expression):
    
    #creates empty stack for this function 
    stack = []
        
    for x in post_expression:
        
        #if x in the post expression is an operator
        if x == '^' or x == '*' or x == '/' or x == '+' or x == '-':
            
            a= stack.pop()#pops top element from stack 
            b= stack.pop()#pop top element from stack 
            temp = x + b + a#concatenates x then the bottom element, then the top element to achieve prefix notation 
            stack.append(temp)#appends temp variable to stack 
        
        elif x == '–' or x == ' ':#error checking for spaces and invalid characters
            return print('Input expression containes spaces or invalid characters')  
        
        else:
            stack.append(x)#appends operands to stack 
            
    return stack[-1]#Returns whole prefix expression    

def postfixtoinfix(post_expression):
    
    #creates empty stack for this function 
    stack_infix = []
        
    for x in post_expression:
        
        #if x is an operator 
        if x == '^' or x == '*' or x == '/' or x == '+' or x == '-':
            
            a= stack_infix.pop()#pops top element
            b= stack_infix.pop()#pops top element
            temp = b + x + a#concatenates bottom element, then x, then the top element to achieve infix notation 
            stack_infix.append(temp)#pushes temp variable to the stack 
        
        elif x == '–' or x == ' ':#error checking for spaces and invalid characters
            return print('Input expression containes spaces or invalid characters')    
        
        else:
            stack_infix.append(x)#pushes operands into the stack 
               
    return stack_infix [-1]#Returns whole infix expression  
    
    #defines function to extract from input file and write to output file
def extractinputfiles(filename,outputfile):
    
    #reads from and open file 
    with open(filename, 'r') as file:
        lines = file.readlines()#reads all line in the file  
        with open(outputfile, 'w') as Postfixoutputs:#opens and writes to PostfixOutputs.txt
            for line in lines:#iterates through txt file lines 
                line = line.strip()#removes white spaces  
                if line:#skips empty lines  
                    post_expression = line #sets post expression = line within the txt file 
                    prefix = postfixtoprefix(post_expression)#converts to prefix   
                    infix = postfixtoinfix(post_expression)#converts to infix  
                    Postfixoutputs.write(f"Prefix expression is: {prefix}\n")
                    Postfixoutputs.write(f"Infix expression is: {infix}\n")


extractinputfiles('PostfixInputs.txt','PostfixOutputs.txt')#calls function to extract data from txt file 
post_expression = ""#creates empty string which can be called by conversion functions
     
