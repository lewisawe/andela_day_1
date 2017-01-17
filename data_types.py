def data_type(x):
	if type(x) == str:
		return len(x)
	if x == None:
		return 'no value'

	if type(x) == bool:
		return x

	if type(x) == int:
		if x < 100:
			return 'less than 100'
		elif x == 100:
			return 'equal to 100'
			
		else:
			return 'more than 100'

	if type(x) == list:
		y = x[2:3]
		if y:
			return y[0]
		else:
			return None
