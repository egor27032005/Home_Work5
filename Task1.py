
file=open('tekst.txt', 'r')
list=[file.read()]
file.close
t=''.join(list)
res_str = t.replace('abc', '')
file2=open('tekst.txt', 'w')
file2.write(res_str)
file2.close
##на русской раскладке почему-то не работало