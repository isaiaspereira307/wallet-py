# get_resultado - https://www.fundamentus.com.br/resultado.php
# get_papel - https://www.fundamentus.com.br/detalhes.php?papel=WEGE3
# list_papel_setor - https://www.fundamentus.com.br/resultado.php?setor=27

import fundamentus
# df = fundamentus.get_resultado()
# print(df.columns)
# print(df[df.pl > 0])


# df = df[ df.pl  > 0   ]
# df = df[ df.pl  < 100 ]
# df = df[ df.pvp > 0   ]


df = fundamentus.get_papel('VALE3')  ## or...
# df = fundamentus.get_papel(['ITSA4','WEGE3'])
print(df.columns)
print(df)


# fin = fundamentus.list_papel_setor(35)  # finance
# seg = fundamentus.list_papel_setor(38)  # seguradoras

# print(fin)

# print(seg)