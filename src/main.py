
import sys
from calc import apply_percent

vat_free_price = float(sys.argv[1])
percent = float(sys.argv[2])

vat_included_price = apply_percent(vat_free_price, percent)

print(f'Vat Free Price : {vat_free_price}')
print(f'Percent : {percent} %')
print(f'Vat Included Price: {vat_included_price}')

 # si l'exec ne fonctionne pas j'execute dans le terminal avec le chamin "python.\src\main.py 100 20
 # et ça donne vet free price : 100, percent: 20%  et vat included price: 120.






