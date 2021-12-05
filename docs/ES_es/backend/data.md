# Diseño de Datos
Para el diseño de datos hemos utilizado un enfoque relacional, con SQLite como base de datos y SQLAchemy como ORM.

El diseño de datos es extreamadamente simple, y a la hora de almacenar las respuestas incorrectas (una lista de strings) y las estadísticas de una pregunta (cuantas veces se ha respondido a cada pregunta) hemos necesitado almacenar un JSON como string.

Las clases añadidas son las siguientes:
- UserStats, se encarga de almacenar los datos individuales de los usuarios.
- Questions, almacena los datos.
- AnsweredQuestions, contiene las respuestas de cada usuario a cada pregunta.

![Datos](https://i.imgur.com/UTyE0u3.png)
