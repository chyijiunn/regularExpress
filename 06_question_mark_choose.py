import re
statement = '丘處機本名不詳，王重陽為他訓名處機，字通密，號丘處機長春子。'
name_re = re.compile(r'長(真|生|長|春)?子')#長?子 , ?=真 or 生 or 長 or 春 or none
result = name_re.search(statement)
print(result.group())
statement = '丘處機本名不詳，不知道是不是長子，字通密，號丘處機長春子。'
name_re = re.compile(r'長(真|生|長|春)?子')
result = name_re.search(statement)
print(result.group())#先搜到長子