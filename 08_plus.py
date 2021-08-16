import re
statement = '丘處機本名不詳，不知道是不是長子的長子的長子的長子的長子，字通密，號丘處機長春子。'
name_re = re.compile(r'是(長子的)+長子')#搜到長子的次數至少一次
result = name_re.search(statement)
print(result.group())
statement = '丘處機本名不詳，不知道是不是長子，字通密，號丘處機長春子。'
name_re = re.compile(r'是(長子的)+長子')
result = name_re.search(statement)
print(result.group())