# Frontend design
En este caso hemos aplicado un modelo de tres capas, separando la lógica, los datos y la vista.

Hemos intentado cumplir en la mayor medida posible los principios **SOLID**, como por ejemplo en la clase dbmanager, que hemos creado para intentar crear la mayor cantidad posible de funciones útiles de la base de datos, para cumplir con el Open/Close, en vez de hacerlo en diferentes clases como habíamos pensado en un principio.

## Patrones de diseño empleados
En aquellos apartados a los que hemos añadido un asterisco (\*title) significa que lo hemos tenido como consideración, no que ha sido implementado.

### Patrones Creacionales

#### \*Singleton

La idea original era la de aplicar un singleton sobre una instancia sobre la base de datos, sin embargo, hemos aplicado las una de las funcionalidades de flask, global.

Con esto aplicamos el mismo comportamiento, asegurando que solamente exista una instancia de este tipo.


### Patrones Estructurales

#### Adapter

Para la conexión con la capa de datos hemos aplicado el siguiente adaptador:
![](https://images-ext-2.discordapp.net/external/myQSW49sI8WiByEtbxRb5XRsgJ6WY6OvkuErQT_kCI8/https/i.imgur.com/hhLKy7V.png?width=557&height=473)

#### \*Proxy

Se sonsideró el aplicar este patrón a la hora de responder las preguntas, para comprobar si estas han sido respondidas correctamente.

Sin embargo, pensamos que usarlo en este caso sería desviarse un poco del funcionamiento de este patrón, por lo que simplemente realizamos este trámite en una función directamente, para no matar moscas a cañonazos.


### Patrones Comportamiento

#### Iterator

Este patrón se ha aplicado para cumplir con el requisito de permitir responder las preguntas no contestadas de uno en uno.

#### \*State

Habría sido interesante añadir un State para la impresión de roles, así dejaríamos abierta la posibilidad de añadir nuevos roles (cumplir el Open/Closed) y mejorar el mantenimiento.

Teníamos la idea de visualizar directamente todas las preguntas, pero al final decidimos hacerlo de forma individual, por lo que la implementación de este patrón sería un tanto innecesaria.
