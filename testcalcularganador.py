import pytest
from app import CalculaGanador


def test_dni_valido():
    c = CalculaGanador()
    assert c.es_dni_valido('12345678') == True
    assert c.es_dni_valido('1234567') == False
    assert c.es_dni_valido('123456789') == False
    assert c.es_dni_valido('1234abcd') == False


def test_calcular_votos_validos():
    c = CalculaGanador()
    data = [
        ['Áncash', 'Asunción', 'Acochaca', '12345678', 'Eddie Hinesley', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '87654321', 'Aundrea Grace', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '11111111', 'Eddie Hinesley', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '22222222', 'Aundrea Grace', '0']
    ]
    votos_por_candidato, total_votos_validos = c.calcular_votos_validos(data)
    assert votos_por_candidato == {'Eddie Hinesley': 2, 'Aundrea Grace': 1}
    assert total_votos_validos == 3


def test_obtener_ganador():
    c = CalculaGanador()
    votos_por_candidato = {'Eddie Hinesley': 3, 'Aundrea Grace': 2}
    total_votos_validos = 5
    assert c.obtener_ganador(votos_por_candidato, total_votos_validos) == [
        'Eddie Hinesley']

    votos_por_candidato = {'Eddie Hinesley': 2, 'Aundrea Grace': 3}
    total_votos_validos = 5
    assert c.obtener_ganador(votos_por_candidato, total_votos_validos) == [
        'Aundrea Grace']

    votos_por_candidato = {'Eddie Hinesley': 2, 'Aundrea Grace': 2}
    total_votos_validos = 4
    assert c.obtener_ganador(votos_por_candidato, total_votos_validos) == [
        'Eddie Hinesley', 'Aundrea Grace']

    votos_por_candidato = {'Eddie Hinesley': 0, 'Aundrea Grace': 0}
    total_votos_validos = 0
    assert c.obtener_ganador(votos_por_candidato, total_votos_validos) == []


def test_calcularganador():
    c = CalculaGanador()
    data = [
        ['Áncash', 'Asunción', 'Acochaca', '12345678', 'Eddie Hinesley', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '87654321', 'Aundrea Grace', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '11111111', 'Eddie Hinesley', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '22222222', 'Aundrea Grace', '0']
    ]
    assert c.calcularganador(data) == ['Eddie Hinesley']

    data = [
        ['Áncash', 'Asunción', 'Acochaca', '12345678', 'Eddie Hinesley', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '87654321', 'Aundrea Grace', '1']
    ]
    assert c.calcularganador(data) == ['Eddie Hinesley', 'Aundrea Grace']
