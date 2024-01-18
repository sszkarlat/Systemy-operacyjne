#include <iostream>
#include <cstdio>
#include <unistd.h>

int main()
{
	printf("Hello, I'm exec program");
  	getchar();

  	execvp("/home/szymon/Systemy operacyjne", NULL);

  	return 0;
}
