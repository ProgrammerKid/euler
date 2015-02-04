function multiples(min, max) {
	var curr	= min,
		mults	= new Array();
	while(curr < max) {
		if(curr % min == 0) {
			mults.push(curr);
		}
		curr++;
	}
	return mults;
}

var	multOf3		= multiples(3, 1000),
	multOf5		= multiples(5, 1000),
	multOf15	= multiples(15, 1000),
	sums		= 0

for(num in multOf3)
	sums += multOf3[num];

for(num in multOf5)
	sums += multOf5[num];

for(num in multOf15)
	sums -= multOf15[num];

console.log(sums);
