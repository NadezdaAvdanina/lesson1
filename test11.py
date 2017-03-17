def get_vat(payment, percent):
	try:
		payment = float(payment)
		percent = int(percent)
		vat = payment / 100 * percent
		vat = round (vat,2)
		return 'сумма ндс: {}'.format(vat)
	except TypeError: 
		print('Не выходит')	


result = get_vat(100, 12)
print(result)

