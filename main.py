import NetworkProfessor as prof

#nomeProf = input("Informe o nome do arquivo de professores: Ex:Nome.csv\n")
#nomeDisc = input("Informe o nome do arquivo de disciplinas: Ex:Nome.csv\n")

professor = prof.NetworkProfessor()

professor.ler_arquivo("professores.csv", "disciplinas.csv")
