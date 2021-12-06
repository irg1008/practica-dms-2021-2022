# Backend design
Para el diseño del backend solamente contamos con dos capas, la capa de presentación y la capa de datos, por lo que podríamos considerarlo un modelo de dos capas.

Hemos intentado cumplir en la mayor medida posible los principios SOLID, como por ejemplo en la clase dbmanager, que hemos creado para intentar crear la mayor cantidad posible de funciones útiles de la base de datos, para cumplir con el Open/Close, en vez de hacerlo en diferentes clases como habíamos pensado en un principio.
## Patrones de diseño empleados
### Patrones Estructurales
#### Adaptador
- En la clase question, un atributo se almacena como string y es utilizado como un json.
#### Decorador 
- En los endpoints, cada funcion esta decorada con un decorador que comprueba que el rol y el token sean válidos.
