ar_valuedef convert_to_int(string_int):
	output = 0
	is_error = False
	for char in string_int:
		char_value = char - '0'
		if (char_value >=0 and char_value <=9):
			output = output * 10 + char_value
		else:
			is_error = True
			print("error")
			return -1
	return output
