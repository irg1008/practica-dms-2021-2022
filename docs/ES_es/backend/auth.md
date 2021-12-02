<!-- vscode-markdown-toc -->
## Tabla de Contenidos
1. [Introducción](#Introducción)
2. [Cabecera](#Cabecera)
3. [Comunicación](#Comunicación)
4. [Validación del Token y Rol](#ValidacióndelTokenyRol)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->
# Autenticación del Backend
##  1. <a name='Introduccin'></a>Introducción

Para mejorar la seguridad de la aplicación disponemos de un contenedor dedicado a las operaciones de autenticación de los usuarios.
![enter image description here](https://i.imgur.com/UDikfU7.png)
El contenedor DMS2122Auth permite generar tokens json firmados (JWS) que contienen información relevante que puede ser consumida en otros contenedores así como para la validación de ciertas operaciones. 

Estos tokens, en la versión actual de la aplicación, únicamente almacenan el id del usuario y su username, pero podrían almacenar más datos, como los roles del usuario. 

Por ejemplo, para el control del Frontend se utilizan Roles para impedir el acceso a ciertas páginas (como por el ejemplo que un estudiante pueda crear preguntas), además de que se re-valida el token en cada operación para verificar que este no haya caducado.

Por otro lado, nuestra API puede ser vulnerable a operaciones similares a las mencionadas en el párrafo anterior, por suerte, todas las peticiones que se realizan a DMS2122Backend requieren de dos elementos de autenticación

##  2. <a name='Cabecera'></a>Cabecera
Para poder dialogar con el backend es necesario incluir dos parámetros de autenticación en la cabecera HTTP.

 - Clave secreta exclusiva del Backend
 - Token usuario (JWS)
 
La clave secreta exclusiva del Backend es conocida por todos los contenedores que vayan a dialogar con este, y si la clave es errónea las peticiones se rechazan. 
Este mecanismo de seguridad permite que únicamente los contenedores puedan comunicarse entre sí, y si se quieren realizar consultas sobre la API del contenedor es necesario incluir la clave secreta. 

**¿Y por qué se debe incluir el token de usuario si las comunicación es entre contenedores?**
Para mejorar la seguridad y limitar el acceso a ciertos endpoints vamos a utilizar un segundo parámetro en la cabecera que nos permita identificar al usuario de manera segura. 

Una opción insegura sería utilizar solo la clave secreta, y pasar como parámetro los roles del usuario (o mismamente no incluimos verificación de los roles, ya que consideramos que esta se realiza desde el frontend).
En una situación en la que esta clave se filtre, o un error de programación en el contenedor DMS2122Frontend permita acceder a un endpoint sin tener un rol específico, la seguridad de nuestra aplicación se verá comprometida. 

##  3. <a name='Comunicacin'></a>Comunicación
En el siguiente diagrama representaremos el ciclo de vida de un TOKEN JWS, el diagrama está relativamente simplificado (ya que se realizan bastantes más comprobaciones sobre la validez de este), pero nos ayuda a visualizar como funciona la autenticación en el backend. 
![https://i.imgur.com/max3YKf.png](https://i.imgur.com/max3YKf.png)
Por un lado tenemos el login o registro, que nos permite obtener un token fresco en el backend con el que poder validar los accesos a páginas. 

El token generado tiene el siguiente formato:
![JWS Token](https://i.imgur.com/Avwxkyl.png)
Podemos observar como se almacenan los datos del usuario, que podemos utilizar para obtener los roles en cualquier momento. 
Cada uno de los elementos que forman el token (Cada elemento está separado por un punto) está codificado en Base64, por lo que podemos obtener la información del token sin necesidad de conocer la clave de firma. 

Cuando Paco intenta crear una pregunta, el frontend verifica que el token sea válido y comprueba que tenga el rol de profesor en ese momento. 
Una vez creada la pregunta, DMS2122Frontend envía una petición a DMS2122Backend con el token creado en el primer paso, la clave secreta que le permite dialogar con el backend y el JSON con los parámetros de la pregunta. 

Cuando el endpoint reciba la petición, decodificara los datos del JWS y validará que la clave secreta sea válida, si todo es correcto, le pasará un objeto con los siguientes elementos 

```json
user_token = {
	auth_token: "very.long.token",
	sub: "admin", 
	user: "admin"
}
```

Y esta información se guardará con el resto de los datos de la cabecera en 
```json
token_info = {
	user_token: user_token,
	...
}
```

Además, OpenAPI nos añadirá los parámetros con información relevante a los argumentos de la función, como por el ejemplo el `body, questionID, username`, etc. 

##  4. <a name='ValidacindelTokenyRol'></a>Validación del Token y Rol
Por último, para limitar el acceso a un endpoint a usuarios que no tengan un rol específico y comprobar que el token es válido, hemos de añadir algún sistema que nos permita comprobar estos elementos con el contenedor DMS2122Auth. 

Para facilitarnos esta tarea y mejorar la mantenibilidad de la aplicación hemos utilizado el **patrón decorador** sobre cada uno de los endpoints. 
![enter image description here](https://res.cloudinary.com/practicaldev/image/fetch/s--EZKxegnb--/c_limit,f_auto,fl_progressive,q_auto,w_880/https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Decorator_UML_class_diagram.svg/400px-Decorator_UML_class_diagram.svg.png)

Si bien el patrón que hemos utilizado no sigue la estructura del diagrama anterior (al no utilizar clases), hemos aplicado los mismo conceptos en un paradigma funcional.

El decorador @protected_endpoint tiene dos argumentos:

 - Función a decorar
 - Lista de Roles a comprobar

![Decorador](https://i.imgur.com/1SQE1RJ.png)
Python le pasa automáticamente la función new al decorador, mientras que nosotros debemos indicarle los roles que pueden tener acceso mediante el argumento roles=

Si no le pasamos ningún rol al decorador, o la lista está vacía, el decorador únicamente comprobará que el token sea válido.

Si la lista de roles tiene elementos, el decorador se encargará de llamar a /user/{username}/roles en el contenedor DMS2122.
El parámetro username lo hemos obtenido de JWS, ya que supuestamente identifica al usuario actual. Si el token ha sido modificado para tener un usuario diferente, la firma no coincidirá y la verificación del token no será válida. 

Si la respuesta es satisfactoria se comprobará que alguno de los roles del usuario coincida con los roles que permite el observador, si no el observador devolverá una respuesta HTTP antes que el propio endpoint, con el código HTTP 403.

Por último, como el usuario tiene acceso al endpoint el decorador ejecutará la función decorada, y devolverá su mismo retorno. 

```
"""Decorator that validates a Token and asserts that the user has any of the roles.

If the Role List is empty, there is no role check 

Args:
	route_fun (Callable[..., Tuple[str, Optional[int]]], optional): A function to decorate. Defaults to None.
	roles (List[Role], optional): A List of roles returns 403 if the user has no role. Defaults to [].

Raises:
	Exception: If not used as a decorator

Returns:
	Callable[..., Tuple[str, Optional[int]]]: A function to call that returns an HTTP Status and Message

"""
```
