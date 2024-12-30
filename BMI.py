high = input('請輸入身高cm: ')
weight = input('請輸入體重kg: ')
high = (float(high) / 100)
weight = float(weight)
BMI = weight / (high ** 2)
BMI = round(BMI,2)
if BMI < 18.5:
	weight1 = 18.5 * (high ** 2) - weight
	weight1 = round(weight1,2)
	print('你的BMI值為:', BMI, '，屬於體重過輕，需要至少增加', weight1, 'kg')
elif BMI < 24:
	print('你的BMI值為:', BMI, '，屬於體重正常')
elif BMI < 27:
	weight1 = weight - (24 * (high ** 2))
	weight1 = round(weight1,2)
	print('你的BMI值為:', BMI, '，屬於體重過重，需要至少減少', weight1, 'kg')
elif BMI < 30:
	weight1 = weight - (24 * (high ** 2))
	weight1 = round(weight1,2)
	print('你的BMI值為:', BMI, '，屬於輕度肥胖，需要至少減少', weight1, 'kg')
elif BMI < 35:
	weight1 = weight - (24 * (high ** 2))
	weight1 = round(weight1,2)
	print('你的BMI值為:', BMI, '，屬於中度肥胖，需要至少減少', weight1, 'kg')
else:
	weight1 = weight - (24 * (high ** 2))
	weight1 = round(weight1,2)
	print('你的BMI值為:', BMI, '，屬於重度肥胖，需要至少減少', weight1, 'kg')
