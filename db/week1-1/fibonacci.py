#num = input("plese input n : ");
num=9;

def fib(n1):
	if(n1==0 or n1==1):
		return 1;
	else:
		return fib(n1-1) + fib(n1-2);

print fib(num);
