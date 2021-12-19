# Frontend design
Para el diseño del backend solamente contamos con dos capas, la capa de presentación y la capa de datos, por lo que podríamos considerarlo un modelo de dos capas.

Hemos intentado cumplir en la mayor medida posible los principios SOLID, como por ejemplo en la clase dbmanager, que hemos creado para intentar crear la mayor cantidad posible de funciones útiles de la base de datos, para cumplir con el Open/Close, en vez de hacerlo en diferentes clases como habíamos pensado en un principio.

## Patrones de diseño empleados
En aquellos apartados a los que hemos añadido un asterisco (\*title) significa que lo hemos tenido como consideración, no que ha sido implementado.

### Patrones Creacionales

#### \*Singleton

La idea original era la de aplicar un singleton sobre una instancia sobre la base de datos, sin embargo, hemos aplicado las una de las funcionalidades de flask, global.

Con esto aplicamos el mismo comportamiento, asegurando que solamente exista una instancia de este tipo.


### Patrones Estructurales
#### Adapter
#### Composite
#### Decorator
#### Facade
#### Proxy

### Patrones Comportamiento
#### Iterator
#### Command
#### Strategy
#### State
#### Observer
#### Mediator
#### Template
