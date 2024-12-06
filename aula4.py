# greedy e non-greedy(lazy)

# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )

# | OU
# . qualquer caractere (com excessão da quebra de linha)
# [] conjunto de caracteres 

# quantificadores 
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
# {n} 
# {min, max} 
# {10,} 10 ou mais 
# {,10} 0 até 10 
# {10} especificamente 10 

import re

texto = '''
<p> frase 1 </p> <p> frase 1 </p> <p> frase 2 </p> <p> frase 3 </p> <div> frase 4 </div>
'''

print(re.findall(r'<[p,div]{1,3}>.*</[p,div]{1,3}>', texto)) # greedy
print(re.findall(r'<[p,div]{1,3}>.*?</[p,div]{1,3}>', texto)) # non-greedy
