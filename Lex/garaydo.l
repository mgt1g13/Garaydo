digit	[0-9]
letter	[A-Za-z]
reserved	"int"|"float"|"char"|"do"|"for"|"while"|"if"|"else"
logic_ops "<"|"<="|">"|">="|"!="|"=="|"||"|"&&"
%%
		/*ignore*/
[ \t\n]	;

		/*reserved words*/
{reserved}								printf("[RESERVED_WORD, %s]\n", yytext);

		/*delimiters*/
[(){};]									printf("[DELIMITER, %s]\n", yytext);

		/*floats*/
{digit}+"."{digit}+						printf("[FLOAT, %s]\n", yytext);
{digit}+"."{digit}+e{digit}+			printf("[FLOAT, %s]\n", yytext);
{digit}+"."{digit}+e[-+]{digit}+		printf("[FLOAT, %s]\n", yytext);
{digit}+e{digit}+						printf("[FLOAT, %s]\n", yytext);
{digit}+e[-+]{digit}+					printf("[FLOAT, %s]\n", yytext);

		/*ints*/
{digit}+								printf("[INT, %s]\n", yytext);

		/*indentifiers*/
{letter}({letter}|{digit})*				printf("[ID, %s]\n", yytext);

		/*arithmetic ops*/
[+\-*/%=]								printf("[ARITHMETIC_OP, %s]\n", yytext);

		/*line comment*/
"//".*									printf("[COMMENT, %s]\n", yytext);

		/*comment*/
"/*"[^*]*[*]+([^*/][^*]*[*]+)*[/]		printf("[COMMENT, %s]\n", yytext);
"/*"									{printf("Lexical error. Unterminated comment.\n"); exit(1);} 

		/*logic ops*/
{logic_ops}								printf("[LOGIC_OP, %s]\n", yytext);

.			{ printf("Lexical error %s\n", yytext);  exit(1);}
