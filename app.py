import csv
# el programa deberá calcular el ganador de votos validos considerando que los siguientes datos son proporcionados:
# region,provincia,distrito,dni,candidato,esvalido
# Si hay un candidato con >50% de votos válidos retornar un array con un string con el nombre del ganador
# Si no hay un candidato que cumpla la condicion anterior, retornar un array con los dos candidatos que pasan a segunda vuelta
# Si ambos empatan con 50% de los votos se retorna el que apareció primero en el archivo
# el DNI debe ser valido (8 digitos)


class CalculaGanador:
    def leerdatos(self):
        data = []
        with open('0204.csv', 'r') as csvfile:
            next(csvfile)
            datareader = csv.reader(csvfile)
            for fila in datareader:
                data.append(fila)
        return data

    def calcular_votos_validos(self, data):
        votosxcandidato = {}
        total_votos_validos = 0

        for fila in data:
            region, provincia, distrito, dni, candidato, esvalido = fila

            if len(dni) != 8 or not dni.isdigit():
                continue  # Ignorar votos con DNI inválido

            if candidato not in votosxcandidato:
                votosxcandidato[candidato] = 0

            if esvalido == '1':
                votosxcandidato[candidato] += 1
                total_votos_validos += 1

        return votosxcandidato, total_votos_validos

    def calcularganador(self, data):
        votosxcandidato, total_votos_validos = self.calcular_votos_validos(
            data)

        if total_votos_validos == 0:
            return []

        ordenado = sorted(votosxcandidato.items(),
                          key=lambda item: item[1], reverse=True)

        for candidato, votos in ordenado:
            if votos > total_votos_validos / 2:
                return [candidato]

        if len(ordenado) >= 2:
            return [ordenado[0][0], ordenado[1][0]]
        elif len(ordenado) == 1:
            return [ordenado[0][0]]
        else:
            return []


# Ejemplo de uso:
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
