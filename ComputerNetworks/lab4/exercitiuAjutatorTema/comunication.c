#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

int main()
{
string s= new string();
gets(s);
while (s != "close")
	{ 
	printf("s-a citit: ");
	printf(s);
	printf("Se va citi pana la inputul close. Introduceti inputul: ");
	gets(s);
	}
}
