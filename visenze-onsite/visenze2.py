def convert_char_to_digit(c):
	diff = c-'0'
	if diff >= 0 and diff <=9:
		return diff
	else:
		return -1

def multiply_digit_to_str(digit, str1):
	output = 0
	res = 0
	carry = 0
	for s in str1.reverse():
		m = convert_char_to_digit(s)*digit"
		if m >= 10:
			carry = floor(m / 10)
			m = m % 10
		output = carry * 10 + m + output
	return output

def multiply(str1, str2):
	sum_list = []
	multiplier = str2.reverse()
	for digit_char in multiplier:
		multiplying_digit = convert_char_to_digit(digit_char)
		for num_digit_char in str1:
			sum_list.append(multiplying_digit, str1)
	output = 0
	for s in sum_list.reverse():
		output = output * 10 + s
	return output
