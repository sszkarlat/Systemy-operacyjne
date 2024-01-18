#include <stdio.h>
#include <unistd.h>

int main()
{
	int father = 0;
	int grandfather = getpid();
	printf("PID: %d\n", grandfather);
	getchar();

	pid_t grandchild = fork();
	if(getpid() != grandfather)
	{
		father = getpid();
		printf("PID: %d\nParent PID: %d\n", getpid(), getppid());
	}
	getchar();

	pid_t anotherChild = fork();
	if(father && getpid() != father)
	{
		printf("PID: %d\nParent PID: %d\n", getpid(), getppid());
	}
	getchar();
}
