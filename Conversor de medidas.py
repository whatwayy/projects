m = float(input('Digite um valor em metros: '))
mm = m * 1000
c = m * 100
dm = m * 10
dam = m / 10
hm = m / 100
km = m / 1000
print('Valor convertido:')
print('milímetros {}\ncentímetros {}\ndecímetro {}\nmetros {}\ndecâmetro {}\nhectômetros {}\nquilômetros {}'.format(mm, c, dm, m, dam, hm,km))
