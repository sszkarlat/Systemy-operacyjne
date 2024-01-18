#include <stdio.h>
#include <stdlib.h>

int main() 
{
	printf("Hello, I'm a system program!\n");
   	getchar();

    
    	int return_code = system("ls -al /var/log/");

    	if (return_code == 0)
	{
        	printf("Command executed successfully.\n");
    	} else {
        	fprintf(stderr, "Command failed with return code: %d\n", return_code);
    	}

    	return 0;
}

