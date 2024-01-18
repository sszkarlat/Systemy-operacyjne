#include <stdio.h>
#include <unistd.h>

int main()
{
	int father_pid = 0;
	int grandfather_pid = getpid();
	printf("PID: %d\n", grandfather_pid);
	getchar();

	pid_t father_child_pid = fork();
	if (getpid() != grandfather_pid)
	{
		father_pid = getpid();
		printf("PID: %d\nParent PID: %d\n", getpid(), getppid());
	}
	getchar();

	pid_t another_child_pid = fork();
	if (father_pid && getpid() != father_pid)
	{
		printf("PID: %d\nParent PID: %d\n", getpid(), getppid());
	}
	getchar();
}
