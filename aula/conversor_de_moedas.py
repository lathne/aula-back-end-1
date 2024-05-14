taxa_euro = 5.55
taxa_iene = 30.19
valor_real = float(input('Digite o valor em R$: '))

print(valor_real / taxa_euro)

valor_convertido_euro = f'{valor_real / taxa_euro:.2f}'
valor_convertido_iene = f'{valor_real / taxa_iene:.2f}'

print(f'Euro: {valor_convertido_euro} | Iene: {valor_convertido_iene}')