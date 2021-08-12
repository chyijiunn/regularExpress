import re
number_re = re.compile(r'(\d{4})(\d{6})')#將電話號碼的10碼以括弧分成兩組
result = number_re.search('My phone number is 0922456789')
print('第1組號碼:',result.group(1))
print('第2組號碼:',result.group(2))
print('全部號碼:',result.group(0))
print('全部號碼:',result.group())