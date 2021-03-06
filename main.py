from Pessoa import Pessoa, PF, PJ

p = Pessoa(111, 'Samael', 'Rua ARACAJU, 001', '(51) 99999 - 1111')
pf = PF(222, 'Celso', 'Rua B, 002', '(51) 99999 - 2222', '111.222.333-44', 33, 50, 1.85)
pj = PJ(333, 'Telma', 'Rua C, 003', '(51) 99999 - 3333', '111.222.334-55', 1234567, 111)

print('Pessoa: ')
p.ImprimirNome()
p._ImprimirEndereco()
p._ImprimirEndereco()
print('#'*30)
print('Pessoa Física: ')
pf.ImprimirNome()
pf.ImprimirCPF()
pf.ImprimirIdade()
pf.ImprimirIMC()
print('#'*30)
print('Pessoa Jurídica: ')
pj.ImprimirRegistroEstadual()
pj.ImprimirCNPJ()