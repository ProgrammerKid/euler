var sequence	= new Array(),
	sum			= 0;
sequence = [1, 2, 3]

while(sequence[sequence.length - 1] <= 4000000)
	sequence.push( sequence[sequence.length - 2] + sequence[sequence.length - 1] );

for(pos in sequence) {
	if(sequence[pos] % 2 == 0)
		sum += sequence[pos];
}

console.log(sum);
