// call_shellcode2.c  
int main(int argc, char **argv)
{
   void(*f)();
   f = (void(*)()) argv[1];
   f();
} 
