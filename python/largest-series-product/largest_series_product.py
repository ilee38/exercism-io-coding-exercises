def largest_product(series, size):
	if len(series) < size or size < 0:
		raise ValueError("Incorrect parameters")
	
	max_prod = 0
	product = 1
	for i in range((len(series) - size) + 1):
		for j in range(i, i + (size)):
			product *= int(series[j])
		if product > max_prod:
			max_prod = product
		product = 1
	return max_prod
	 
