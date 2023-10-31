class Universidade:
    def __init__(self):
        self.cursos = {}  # Dicionário para armazenar a associação entre cursos e professores
        self.professores = set()  # Conjunto para armazenar a lista de professores

    def designar_professor_curso(self, curso, professor):
        # Verifica se o professor já está na lista de professores da universidade
        if professor not in self.professores:
            self.professores.add(professor)

        # Associa o curso ao professor
        self.cursos[curso] = professor

    def listar_cursos_por_professor(self, professor):
        cursos_lecionados = [curso for curso, p in self.cursos.items() if p == professor]
        return cursos_lecionados

# Exemplo de uso
if __name__ == "__main__":
    universidade = Universidade()

    # Cria alguns cursos e professores
    curso1 = "Matemática"
    curso2 = "Física"
    curso3 = "História"
    professor1 = "João"
    professor2 = "Maria"
    professor3 = "Carlos"

    # Designa professores para cursos
    universidade.designar_professor_curso(curso1, professor1)
    universidade.designar_professor_curso(curso2, professor2)
    universidade.designar_professor_curso(curso3, professor1)

    # Lista os cursos lecionados por um professor
    cursos_joao = universidade.listar_cursos_por_professor(professor1)
    cursos_maria = universidade.listar_cursos_por_professor(professor2)
    cursos_carlos = universidade.listar_cursos_por_professor(professor3)

    print(f"Cursos lecionados por {professor1}: {cursos_joao}")
    print(f"Cursos lecionados por {professor2}: {cursos_maria}")
    print(f"Cursos lecionados por {professor3}: {cursos_carlos}")