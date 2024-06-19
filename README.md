# Practica de refactor

### Integrantes

+ **Fabrizzio Vilchez**
+ **Jeffrey Monja**

Se aplicacion técnicas de refactorización a la clase `CalculaGanador` en el archivo `app.py`.

+ Se refactorizó el código para que sea más legible y mantenible.
+ Se agregaron pruebas unitarias para la clase `CalculaGanador` en el archivo `testcalcularganador.py`.

### Refactorización

+ Se eliminaron comentarios innecesarios.
+ Se modificó el nombre de algunos métodos y variables para que sean más descriptivos.
+ Se extrajeron métodos para que cada uno realice una sola tarea y pueda ser reutilizable
+ Se simplificaron las condicionales para evitar anidaciones y redundancias.


### Pruebas unitarias

Se crearon 4 pruebas unitarias con èl módulo `pytest`. Cada prueba se identifica con un nombre de función descriptivo para facilitar la lectura y comprensión de los resultados.

+ ``test_dni_valido()``: Verifica que el DNI ingresado sea válido.
+ `test_calcular_votos_validos()`: Verifica que los votos ingresados sean válidos.
+ `test_obtener_ganador()`: Verifica que el ganador sea el correcto.
+ `test_calcularganador()`: Verifica que el ganador sea un string dentro de una lista

