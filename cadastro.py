import numpy as np
import pandas as pd

col = 'Preço produto marca desconto'.split()
lin = 'funcionário'.split()
produto =''

venda = pd.DataFrame(data=produto, index=lin, columns=col)
venda.to_excel( 'venda.xlsx', sheet_name='Hoje' )
print( venda )
