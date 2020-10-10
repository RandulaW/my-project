# Python Implementation of Modiefied Euler method
def func( A, B ): 
	return (3*(18-B))
 	
# Function for euler formula 
def euler( A0, B, h, A ): 
	# Iterating till the point at which we 
	# need approximation 
	while A0 < A: 
		B= B +h*(func(A0+(h/2), B+(h/2)*func(A0,B)))
		A0 = A0 + h 
	# Printing approximation 
	print("Approximate solution at A = ", A, " is ", "%.6f"% B) 
	 
# Initial Values 
A0 = 0
B0 = 14
h = 0.2
A = 1 # Value of A at which we need approximation 
euler(A0, B0, h, A)







