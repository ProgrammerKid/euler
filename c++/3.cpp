#include <iostream>
using namespace std;

bool isPrime(long x) {
	for(int i = 2; i <= (x/2) + 1; i++) {
		if(x % i == 0 && i != x) {
			return false;
		}
	}
	return true;
}

long * primesTill(long max) {
	long x[max];
	int currPos = 0;
	for(long i = 1; i <= max; i++) {
		if(isPrime(i)) {
			x[currPos] = i;
		}
	}
	return x;
}

int main() {
	long * x = primesTill(10);
	for(int i = 0; i < sizeof(x); i++) {
		cout << x[i] << endl;
	}
	return 0;
}
