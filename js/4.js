function isPal(num) {
	var	num2	= "",
		num		= num + "";
	for(pos in num)
		num2 = num[pos] + num2;
	var hi = (num == parseInt(num2)) ? true:false;
	return hi
}
var sets = function() {
	var start, end, newArray, counter;
	start	= 100,
	end		= 999,
	newArray= [],
	counter	= start;
	while(counter <= end && counter >= start)
		newArray.push(counter) && counter++;
	return newArray;
};
set1 = set2 = sets();
var largestPal = 0;
var n1, n2, mult;
for(num in set1) {
	for(num2 in set2) {
		n1 = set1[num], n2 = set2[num2];
		mult = n1*n2;
		console.log(n1 + "\t*\t" + n2 + "\t=\t" + mult);
		if(isPal(mult) && mult > largestPal) {
			largestPal = mult;
		}
	}
}
console.log(largestPal);
