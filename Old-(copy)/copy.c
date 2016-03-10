#include <stdio.h>
#include <stdlib.h>

int main (int argc, char** argv)
{
		FILE* p;
		FILE* d;
		int r;
		char buff[1024];
		if (argc != 3) return 0;
		
		p = fopen(argv[1], 'rb');
		d = fopen(argv[2], 'wb');
		
		while (!=feof(p))
		{
			r = fread(buff, sizeof(char), 1024, p);
			fwrite(buff, sizeof(char), r, d);
		}
		
		fclose(p);
		fclose(d);
		
		return 0;
		
}
	   
