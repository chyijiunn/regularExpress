import re
number_re = re.compile(r'(\(\d\d\))(\d{7})(\#\d\d)')#分成三組資料，特殊符號前須加\
result = number_re.search('My Home number is (06)6563129#25')
print('group+s',result.groups())
group_1 , group_2 ,group_3 = result.groups()
print('區碼:',group_1)
print('市內電話:',group_2)
print('分機:',group_3)
print(group_1,group_2,sep='')