
a = int(input("Enter the valvue of a  "))
b = int(input("Enter the valvue of b  "))
c = int(input("Enter the valvue of c  "))
n = int(input("Enter the valvue of n  "))

def check_fermat(a,b,c,n):
	if n<2:	
		print(" ")
	elif a**n+b**n==c**n:
		print("Holy smokes,Fermat was worng")
	else:
		print("no,that doesn't work")
check_fermat(a,b,c,n)
