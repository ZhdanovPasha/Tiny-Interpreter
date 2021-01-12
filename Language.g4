grammar Language;

prog:   stat+ ;

stat
    :   ID '=' expr NEWLINE                         # Assign
    |   NEWLINE                                     # Blank
    ;

expr
    :   '-' expr                                    # UnaryMinus
    |   NOT expr                                    # NotExpr
    |   '(' expr ')'                                # Parens
    |   expr op=('*'|'/') expr                      # MulDiv
    |   expr op=('+'|'-') expr                      # AddSub
    |   expr op=(GT | GE | LT | LE | EQ | NE) expr  # ComparatorExpr
    |   expr op=(AND | OR) expr                     # BinaryExpr
    |   BOOL                                        # BoolExpr
    |   ID                                          # Id
    |   NUM                                         # Num
    ;

BOOL
    : TRUE | FALSE
    ;

AND         : 'AND' ;
OR          : 'OR' ;
NOT         : 'NOT';
TRUE        : 'TRUE' ;
FALSE       : 'FALSE' ;
GT          : '>' ;
GE          : '>=' ;
LT          : '<' ;
LE          : '<=' ;
EQ          : '==' ;
NE          : '!=' ;
LPAREN      : '(' ;
RPAREN      : ')' ;
MUL         : '*' ;
DIV         : '/' ;
ADD         : '+' ;
SUB         : '-' ;
ID          : [a-zA-Z]+ ;
NUM         : [0-9]+ ;
NEWLINE     : '\r'? '\n' ;
WS          : [ \t]+ -> skip ;

