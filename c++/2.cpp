#include <iostream>
using namespace std;

int main() {
	int fib[3] = {1, 2, 3};
	int sum = 2; //make sure to include the '2' {1, 2, 3}

	for(int i = 0; i < 10; i++)
		if(fib[2] % 2 == 0) {
			sum += fib[2];
		}

		int tmp = fib[1];
		fib[0] = fib[1];
		fib[1] = fib[2];
		fib[2] = fib[1] + tmp;
	
	cout << sum << endl;
	return 0;
}
