#include <iostream>
#include <cstdio>
#include <unistd.h>

int main()
{
	printf("Hello, I'm exec program");
	getchar();

	execvp("/home/szymon/bashScripts", NULL);

	return 0;
}
