import NetworkProfessor as prof

professor = prof.NetworkProfessor()
professor.ler_arquivo("professores.csv", "disciplinas.csv")
matf = professor.scm(professor.dic[professor.s],professor.dic[professor.t])

for i in range(professor.dic[professor.t]):
    print(matf[i])
