#include <stdio.h>
#include <unistd.h>


int main()
{

	int parentsPID = getpid(); 
	printf("PID: %i\n", parentsPID);
  	getchar();
  
  	pid_t childPID = fork();

  	if (getppid() == parentsPID)
  	{
		printf("Child PID: %i\n", getpid());
		printf("Parent PID: %i\n", getppid());
  	}
  	getchar();

  	return 0;
}
