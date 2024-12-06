# greedy e non-greedy(lazy)

# Meta caracteres: ^ $  ( )



import re
texto = '''
<p> frase 1 </p> <p> frase 1 </p> <p> frase 2 </p> <p> frase 3 </p> <div> frase 4 </div>
'''

cpf = '123.456.189-10'
print(cpf)
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))


# tags = re.findall(r'(<([dpiv]{1,3})>(?:.+?)<\/\2>)', texto)
# tags = re.findall(r'(?P<element><([dpiv]{1,3})>(?:.+?)<\/\(?P=element)>)', texto) # grupo nomeado

print(re.sub(r'(<(.+?)>)(.+?)<(\/\2>)', r'\1"\3"\4', texto))