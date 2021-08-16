import re
name_re = re.compile(r'丹陽子|長真子|長生子|長春子|玉陽子|廣寧子|清靜散人')#第一次比對就出現的
result_1 = name_re.search('長生子丹陽子')
print(result_1.group())
result_2 = name_re.search('丹陽子長生子')
print(result_2.group())
name_re = re.compile(r'(丹陽|長真|長生|長春|玉陽|廣寧)子|清靜散人')#使用括弧節省字串長度
result_3 = name_re.search('丘處機本名不詳，金熙宗皇統八年農曆正月十九日（1148年2月10日）生於山東登州棲霞。1166年開始學道。1167年拜全真道祖師王重陽為師，王重陽為他訓名處機，字通密，號長春子。')
print(result_3.group())