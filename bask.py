a = int(input("Valor do A ? "))
b = int(input("Valor do B ? "))
c = int(input("Valor do C ? "))

delta = b*b-(4*a*c)

if a == 0:
    print("O valor de a, deve ser diferente de 0")
elif delta < 0:
    print("Sem raízes reais")
    

print("Valor de Delta = ",delta)
print()
d = pow(delta,0.5)
a1 = (2*a)
x1 = (-b + d ) / a1
print("Primeiro valor de x = ",x1)
print()

x2 = (-b - d ) / a1
print("Segundo valor de x = ",x2)
print()