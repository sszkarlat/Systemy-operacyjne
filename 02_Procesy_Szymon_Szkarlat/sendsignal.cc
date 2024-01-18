#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

int main(int argc, char *argv[])
{
	if (argc != 3)
	{
		fprintf(stderr, "Usage: %s <PID> <signal>\n", argv[0]);
		return 1;
	}

	pid_t dest_pid = atoi(argv[1]);
	int signal_number = atoi(argv[2]);

	if (kill(dest_pid, signal_number) == 0)
	{
		printf("Signal %d sent to process with PID %d\n", signal_number, dest_pid);
	}
	else
	{
		perror("kill");
		return 1;
	}

	return 0;
}
