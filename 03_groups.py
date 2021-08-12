import re
number_re = re.compile(r'(\d{4})(\d{6})')#將電話號碼的10碼以括弧分成兩組
result = number_re.search('My phone number is 0922456789')
print('group+s',result.groups())#group+s 得到所有群的資料
group_1 , group_2 = result.groups()
print(group_1)
print(group_2)
print(group_1,group_2,sep='')