digit	[0-9]
letter	[A-Za-z]
reserved	"int"|"float"|"char"|"do"|"for"|"while"|"if"|"else"
logic_ops "<"|"<="|">"|">="|"!="|"=="|"||"|"&&"
%%
		/*ignore*/
[ \t]	;

		/*reserved words*/
{reserved}								printf("[RESERVED_WORD, %s]", yytext);

		/*delimiters*/
[(){};]									printf("[DELIMITER, %s]", yytext);

		/*floats*/
{digit}+"."{digit}+						printf("[FLOAT, %s]", yytext);

		/*ints*/
{digit}+								printf("[INT, %s]", yytext);

		/*indentifiers*/
{letter}({letter}|{digit})*				printf("[ID, %s]", yytext);

		/*arithmetic ops*/
[+\-*/%=]								printf("[ARITHMETIC_OP, %s]", yytext);

		/*line comment*/
"//".*									printf("[COMMENT, %s]", yytext);

		/*comment*/
"/*"[^*]*[*]+([^*/][^*]*[*]+)*[/]		printf("[COMMENT, %s]", yytext);
"/*"									printf("Lexical error. Unterminated comment.");

		/*logic ops*/
{logic_ops}								printf("[LOGIC_OP, %s]", yytext);
