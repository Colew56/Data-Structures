This project consists of algorithms to interconvert prefix,infix,and postfix notations.
Prefix: For example, the first line in the Prefixinputs.txt file "++A-*^BCD/+EF*GHI" will be converted to both infix and postfix notation using the stack algorithm. The outputs should be "A+B^C*D-E+F/G*H+I" and "ABC^D*EF+GH*/-+I+".
Postfix: For example, the first line in the Postfixinputs.txt file "AB+C-" will be converted to both infix and postfix notation using the stack alorithm. The outputs should be "A+B-C" and "-+ABC".
Infix: The alorithm will first convert an infix expression into postfix, and then convert that postfix expression into a prefix expression. For example the first line in InfixInputs.txt file "(A+B)*(C^(D-E)+F)-G" will be converted to "-*+AB+^C-DEFG".

This code was built using the IDE: Thonny and run on Python 3.9.13. To run this code unzip the file on your machine and save all the files in the same directory. Download the Thonny IDE and execute the script.
The Infix_ script will read data from InfixInputs.txt and write to InfixOutputs.txt
The Postfix_ script will read data from PostfixInputs.txt and write to PostfixOutputs.txt
The Prefix_ script will read data from PrefixInputs.txt and write to PrefixOutputs.txt
