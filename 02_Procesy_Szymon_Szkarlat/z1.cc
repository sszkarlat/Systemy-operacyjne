#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <fcntl.h>

int const LOCAL_VARIABLE = 100;  
int *dynamic_memory_global = (int*)malloc(sizeof(int));

int main()
{
	pid_t pid;

	int file_descriptor = open("output.txt", O_WRONLY | O_CREAT, 0644);
	int local_variable = 10;
  
	int *dynamic_memory = (int*)malloc(sizeof(int));
	*dynamic_memory = 100;

 	pid = fork();

	printf("Child PID: %d\nParent PID: %d\n", getpid(), getppid());

	int reply;
  	if (pid < 0) 
  	{ 	
		//error occurred
		fprintf(stderr, "Fork Failed");
		return 1;
  	}
  	else if (pid == 0) 
  	{ 	
		//child process
		printf("Child scanf: \n");
		scanf("%i",&reply);
		printf("Child scanf completed\n");
  	}
  	else 
  	{
		// parent process
		// parent will wait for the child to complete
		wait(NULL);
		printf("Child Complete\n");
		getchar();
	}

	return 0;
}
