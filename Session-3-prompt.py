#defining a function 
def f(x):
	return float(x**3 + 8)

#defining a main fuction setting x equal to 9
def main():
	x = 9

	f(x)               #run f(x) with new x value
	print (f(x))          #print the result

	#if f(x) has a result larger than 27, print YAY!
	if (f(x) > 27):
		print("YAY!")

if __name__ == "__main__":
	main()

