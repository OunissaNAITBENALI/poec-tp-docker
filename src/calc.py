
import sys


def apply_percent(v_free_price:float, percent:float):


# vérifier que le prix est un nombre:
    if not isinstance(v_free_price, float):
        raise ValueError(f'Price ({v_free_price}) is not a number')

# sinon vérifier  si le price est positif:
    if v_free_price < 0:
        raise ValueError(f'Price ({v_free_price}) is negative')

# confirmer que le pourcentage de TVA doit être compris entre 0 et 100:

    if not 0 <= percent <= 100:
        raise ValueError(f'Invalid percentage: {percent}')

    if not isinstance(percent, float):
        raise ValueError((f'Percent ({percent}) is not a number'))

    v_included_price: float = v_free_price * (1 + percent/100)
    return v_included_price





"""valeur = apply_percent(100, 20)
print(valeur)"""



"""def apply_percent():"""



"""price = sys.argv[1]
   percent = sys.argv[2]
55
if __name__ == "__main__":
    price = sys.argv[1]
    percent = sys.argv[2]
    result = apply_percent(price, percent)

    print(f'result : {result}')"""


