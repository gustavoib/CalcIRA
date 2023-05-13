print("sobre trancamentos:\n")
num_trancadas = int(input("número de disciplinas trancadas: "))

soma_trancadas = 0
for i in range(num_trancadas):
  sem_trancadas = int(input(f"semestre da {i+1}ª disciplinas trancada: "))
  carga_horaria_trancadas = int(input(f"carga horária da {i+1}ª disciplina trancada: "))

  soma_trancadas += (sem_trancadas*carga_horaria_trancadas)  

print("sobre as disciplinas:\n")
n = int(input("disciplinas cursadas ou trancadas até o momento: "))

C = 0
nota_final = 0
parcial = 0
for i in range(n): 
 
  nota = float(input(f"nota da disciplina {i+1}: "))
  carga_horaria = float(input(f"carga horaria da disciplina {i+1}: "))
  semestre = float(input(f"semestre da disciplina {i+1}: "))
  
  C = C + carga_horaria
  nota_final += (semestre * carga_horaria * nota)
  parcial += (semestre * carga_horaria)

ira = (1 - (0.5 * carga_horaria_trancadas) / C) * (nota_final / (parcial - soma_trancadas)) * 1000

print(parcial)
print(soma_trancadas)
print(ira)