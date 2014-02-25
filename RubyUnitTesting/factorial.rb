# factorial(n) is defined as n*n-1*n-2..1 for n > 0
# factorial(n) is 1 for n=0
# Let's raise an exception if factorial is negative
# Let's raise an exception if factorial is anything but an integer

def factorial(n)
	#(1..n).inject(:*) || 1
	if n <= 1
		1
	else
		n * factorial(n-1)
	end
end
