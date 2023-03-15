x = int (input("Cual es el primer numero? "))
y = int (input("Cual es el segundo numero? "))
z = int (input("Cual es el tercer numero? "))

def PRO(x:float,y:float,z:float) -> float:
   promedio = (x+y+z)/3
   return float(promedio)



result = PRO(x,y,z)

print("El promedio es: ", result)
