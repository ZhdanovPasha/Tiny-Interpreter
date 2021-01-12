# Tiny Interpreter

## About

Tiny Interpreter is an interpreter written in Python and ANTLRv4.  
Grammatic description:

```
Language : Program
Program : Statement
Statement : Assign | Newline
Assign : Identifier '=' Expression
Expression : '-' Expression 
    | Not Expression
    | '(' Expression ')'
    | Expression Operator Expression
    | Boolean
    | Identifier
    | Number
Operator: '+' | '-' | '*' | '/' | '==' | '!=' | '<=' | '>=' | '>' | '<' | '&&' | '||'
Boolean: True | False
Identifier: [a-zA-Z]+ 
Number:  [0-9]+ 
Newline: '\r'? '\n' 
```  

## Installation
Install [ANTLR4 Python3 runtime](https://github.com/antlr/antlr4/blob/master/doc/python-target.md) and [ANTLR](https://www.antlr.org/download.html).

## Usage
1. Create parser: ```antlr4 -Dlanguage=Python3 -visitor Language.g4```.
2. Add code in .txt file.
3. Launch interpeter: ```python interpeter.py your_txt_file.txt```.  
You may find code samples in tests.py.
