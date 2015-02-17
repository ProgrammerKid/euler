class p3 {
	public static void main(String args[]) {
		long x = 600851475143; //the product we are checking for
		for(long i = x - 1; i > 0; i--) {
			if(isPrime(i) && x % i == 0)
				System.out.println(i);
		}
	}

	static boolean isPrime(long i) {
		//d for divisor
		for(int d = 2; d < i; d++) {
			if(i % d == 0)
				return false;
		}
		return true;
	}
}
