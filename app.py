import csv


class CalculaGanador:

    def leerdatos(self, filename='0204.csv'):
        data = []
        with open(filename, 'r') as csvfile:
            next(csvfile)  # Skip header
            datareader = csv.reader(csvfile)
            for fila in datareader:
                data.append(fila)
        return data

    # Refactorización: Extracción de método para validar el DNI
    def es_dni_valido(self, dni):
        return len(dni) == 8 and dni.isdigit()

    # Refactorización: Renombramiento de métodos
    def calcular_votos_validos(self, data):
        # Refactorización: Renombramiento de variables
        votos_por_candidato = {}
        total_votos_validos = 0

        for fila in data:
            region, provincia, distrito, dni, candidato, esvalido = fila

            # Refactorización: Simplificación de condicionales
            if not self.es_dni_valido(dni):
                continue  # Ignorar votos con DNI inválido

            if candidato not in votos_por_candidato:
                votos_por_candidato[candidato] = 0

            if esvalido == '1':
                votos_por_candidato[candidato] += 1
                total_votos_validos += 1

        return votos_por_candidato, total_votos_validos

    # Refactorización: Extracción de método para obtener el ganador
    def obtener_ganador(self, votos_por_candidato, total_votos_validos):
        if total_votos_validos == 0:
            return []

        ordenado = sorted(votos_por_candidato.items(), key=lambda item: item[1], reverse=True)

        for candidato, votos in ordenado:
            if votos > total_votos_validos / 2:
                return [candidato]

        if len(ordenado) >= 2:
            return [ordenado[0][0], ordenado[1][0]]
        elif len(ordenado) == 1:
            return [ordenado[0][0]]
        else:
            return []

    def calcularganador(self, data):
        votos_por_candidato, total_votos_validos = self.calcular_votos_validos(data)
        return self.obtener_ganador(votos_por_candidato, total_votos_validos)


# Ejemplo de uso
if __name__ == "__main__":
    c = CalculaGanador()
    print(c.calcularganador(c.leerdatos()))

    # Datos de prueba
    datatest = [
        ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
        ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
    ]
    print(c.calcularganador(datatest))
