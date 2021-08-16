import re
number_re = re.compile(r'AATGCTGTTGTTAAAATTTATTGTCCAGCATGTCACA')
genome_File = open('genome','r')
out = str(genome_File.read())
print('The size of the genome is =',len(out))
result = number_re.search(out)
if result == None:
    print('No')
else:
    print('Got it')
genome_File.close()