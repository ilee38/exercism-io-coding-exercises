#!/usr/bin/env python3

def roman(n):
	#1000's
	thousands = ''
	times = n // 1000
	n = n % 1000
	if times > 0:
		for i in range(times):
			thousands += 'M'

	#100's
	hundreds = ''
	times = n // 100
	n = n % 100
	if times == 9:
		hundreds = 'CM'
	elif times == 5:
		hundreds = 'D'
	elif times == 4:
		hundreds = 'CD'
	else:
		for i in range(times):
			hundreds += 'C'

	#10's
	tens = ''
	times = n // 10
	n = n % 10
	if times == 9:
		tens = 'XC'
	elif times == 5:
		tens = 'L'
	elif times == 4:
		tens = 'XL'
	else:
		if times > 5:
			tens += 'L'
			times -= 5
		for i in range(times):
			tens += 'X'

	#1's
	ones = ''
	if n == 9:
		ones = 'IX'
	elif n == 5:
		ones = 'V'
	elif n == 4:
		ones = 'IV'
	else:
		if n > 5:
				ones += 'V'
				n -= 5
		for i in range(n):
			ones += 'I'

	return f'{thousands}{hundreds}{tens}{ones}'