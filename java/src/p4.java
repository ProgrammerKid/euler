class p4 {
	public static void main(String args[]) {
		isPalTest();
	}

	static boolean isPal(int num) {
		String num_str = num + "";
		String num_arr[] = num_str.split("");
		String backwards = "";
		for(String i: num_arr)
			backwards = i + backwards;
		
		System.out.println(backwards + "\t" + num_str);
		if(backwards == num_str)
			return true;

		return false;
	}

	static void isPalTest() {
		//expected output
		//true, false, true, false
		System.out.printf("%b, %b, %b, %b \n", isPal(515), isPal(551), isPal(151), isPal(115));
	}
}
