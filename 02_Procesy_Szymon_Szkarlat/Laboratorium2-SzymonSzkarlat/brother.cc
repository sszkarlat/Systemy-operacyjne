#include <stdio.h>
#include <unistd.h>

int main()
{ 
	int grandfather = getpid();
	printf("Pid: %d\n", grandfather);
	getchar();

	pid_t grandchild;
	grandchild = fork();
	int father = 0;
	if(getpid() != grandfather)
	{
		father = getpid();
	 	printf("2nd PID: %d\nParent: PID: %d\n\n", getpid(),getppid());
	}
	getchar();	
	
	if (getpid() == grandfather) 
	{
	  	pid_t brother;
	  	brother = fork();
	  	if (getpid() != grandfather)
		{
			printf("Brother PID: %i\nParent PID: %i\n\n", getpid(), getppid());
	  }
	}

	pid_t anotherchild;
	anotherchild = fork();
	if(father && getpid() != father)
	{
	  	printf("3rd PID: %d\nParent PID: %d\n\n", getpid(), getppid());
	}
	getchar();
}
