# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )

# | OU
# . qualquer caractere (com excessão da quebra de linha)
# [] conjunto de caracteres 

import re

texto = '''
O rato roeu a roupa do rei de Roma.
A rápida raposa marrom pula sobre o cão preguiçoso.
Em tempos de tempestade, todos os gatos são pardos.
Quem com ferro fere, com ferro será ferido.
Água mole em pedra dura, tanto bate até que fura.
A pressa é inimiga da perfeição.
De grão em grão, a galinha enche o papo.
Quem ri por último, ri melhor.
Mais vale um pássaro na mão do que dois voando.
A cavalo dado não se olha os dentes.
Quem não arrisca, não petisca.
Devagar se vai ao longe.
Quem semeia ventos, colhe tempestades.
Antes tarde do que nunca.
Quem tem boca vai a Roma.
Água mole em pedra dura, tanto bate até que fura.
João foi à feira comprar frutas.
Maria foi ao mercado comprar legumes.
João encontrou Maria na feira.
Maria e joão decidiram almoçar juntos.
João e Maria foram ao parque depois do almoço.
Maria comprou um presente para João.
João agradeceu a Maria pelo presente.
'''

print(re.findall(r'João|Maria', texto))
print(re.findall(r'Jo.o', texto))
print(re.findall(r'[a-zA-Z0-9]oão', texto))
                   # ^- é um range de a até z 
print(re.findall(r'JOÃO', texto, flags=re.IGNORECASE))
