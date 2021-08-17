import re
genome_File = open('genome','r')
output = str(genome_File.read())
search_re = re.compile(r'(AAA){3,5}')#比對時，可接受3~5個AAA進行貪婪比對
result = search_re.search(output)
print('Got it!Greed search result is ',result.group())#或者輸出找到了！

search_re = re.compile(r'(AAA){3,5}?')#比對時，接受3~5個AAA進行非貪婪比對
result = search_re.search(output)
print('Got it!Nongreed search result is ',result.group())

genome_File.close()