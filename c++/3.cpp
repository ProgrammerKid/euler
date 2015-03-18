#include <iostream>
using namespace std;

bool isPrime(long x) {
	long test = 2;

	//just some special cases
	if(x == 0 or x == 1 or x == 2 or x == 3)
		return true;
	
	while(test < x / 2 + 1) {
		if(x % test == 0)
			return false;
		test++;
	}
	return true;
}

int main() {
	long number = 600851475143;
	long test = 2;
	long largest = 0;

	while(test < number) {
		if(isPrime(test) and number % test == 0 and test > largest) {
			largest = test;
			cout << largest << endl;
		}
		test += 2;
	}
	
	cout << largest << endl;
}
