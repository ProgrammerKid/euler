class p2 {
	public static void main(String args[]) {
		int two, three, newNum, sum;
		
		two		= 1;
		three	= 2;
		newNum	= two + three; //da logic
		sum = 2; //because out of the existing sequence (1, 2, 3 (newNum)) we already have 2 as an even sum
		
		while(newNum <= 4000000) {
			newNum	= two + three;
			two		= three;
			three	= newNum;
			if(newNum % 2 == 0)
				sum += newNum;
		}
		System.out.println(sum);
	}
}
