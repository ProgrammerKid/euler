#include <iostream>
using namespace std;

int main() {
	int fib[2] = {1, 2};
	int sum = 0;

	while(fib[1] < 4000000) {	
		if(fib[1] % 2 == 0) {
			sum += fib[1];
		}

		int tmp = fib[0];
		fib[0] = fib[1];
		fib[1] = fib[0] + tmp;
	}

	cout << sum << endl;
	return 0;
}
