import re
number_re = re.compile(r'\d{10}')
result = number_re.search('My phone number is 0922222222')
print('找到電話號碼:',result.group())