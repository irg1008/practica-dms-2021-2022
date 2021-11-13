- [Despliegue](#despliegue)
  * [Prerrequisitos:](#prerrequisitos)
    + [GNU/Linux](#gnulinux)
      - [Ubuntu](#ubuntu)
    + [Microsoft Windows](#microsoft-windows)
      - [Instalación WSL](#instalación-wsl)
      - [Actualizar la distribución a WSL2](#actualizar-la-distribución-a-wsl2)
      - [Instalación de DOCKER](#instalación-de-docker)
      - [Configuración de DOCKER](#configuración-de-docker)
  * [Ejecución de la Práctica](#ejecución-de-la-práctica)
    + [Obtención del Repositorio](#obtención-del-repositorio)
  * [Posibles Problemas](#posibles-problemas)
    + [Port Forwarding](#port-forwarding)
    + [Problema con los saltos de línea](#problema-con-los-saltos-de-línea)
# Despliegue
Este apartado de documentación se centra en la instalación y configuración del entorno para poder desplegar los distintos servicios que se utilizarán para la práctica.
## Prerrequisitos:
El repositorio está pensado para poder convertir cada uno de los servicios en una única imagen Docker que pueda ser desplegada en cualquier entorno, por lo que necesitamos tener instalado Docker.

### GNU/Linux
La instalación para GNU/Linux es independiente para cada distribución, por lo que es recomendable [consultar la documentació](https://docs.docker.com/engine/install/ubuntu/)n para conocer los distintos pasos.
En nuestro caso vamos a utilizar Ubuntu, por lo que vamos a seguir los pasos con esta distribución.

#### Ubuntu
Vamos a utilizar el script oficial de instalación:

```console
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh
```

Hecho esto, tendremos Docker instlado en nuestro equipo, pero es recomendable añadir a los usuarios que vayan a usar este servicio a el grupo **docker** para poder usarlo sin necesidad de permisos de superusuario.

Para añadir al usuario actual:

```console
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
```
Hecho esto es recomendable reiniciar el equipo para que el proceso se complete de forma satisfactoria. 
Podemos probar que todo está correctamente instalado usando el siguiente comando:

```console
 $ docker run hello-world
```
Si utilizamos el comando `$ docker ps` podemos comprobar si el contenedor está en ejecución.


### Microsoft Windows
La instalación de Docker en Windows es algo más complicada ya que requiere de un servicio de virtualización.

#### Instalación WSL
El primer requisito que necesitamos es instalar el Subsistema de Linux para Windows (Windows Subsystem for Linux)
Es recomendable seguir la [guía de instalación actualizada](https://docs.microsoft.com/en-us/windows/wsl/install) para este proceso, ya que ha cambiado mucho a lo largo de los últimos años.

Suponiendo que tengamos una versión relativamente actualizada de Window 10 o Windows 11, deberíamos poder ejecutar el siguiente comando con permisos de administrador para la instalación:
```Powershell
wsl --install
```
 
Hecho esto buscamos la distribución que más nos guste en la tienda de aplicaciones de Windows (En las últimas versiones WSL se puede instalar directamente desde esta tienda).
 En nuestro caso vamos a escoger [Ubuntu 20.04 LTS](https://www.microsoft.com/store/productId/9N6SVWS3RX71)
 ![Ubuntu 20.04 LTS](https://i.imgur.com/in73tug.png)
  
Se nos habrá instalado como una aplicación más que podemos encontrar en el menú de inicio, en el PATH ( `ubuntu2004.exe`), etc. 
Podemos abrir la distribución que tengamos por defecto con los comandos

    wsl

o

    bash
Como únicamente tenemos una distribución instalada, podemos abrir Ubuntu directamente con este proceso. 
Hecho esto abrimos la distribución y la configuramos como cualquier otro sistema operativo.

#### Actualizar la distribución a WSL2
Para poder utilizar la distribución con Docker, debemos utilizar la versión 2 de WSL que virtualiza el Kernel de Linux. 
Este paso es tan sencillo como utilizar el siguiente comando:

```Powershell
wsl --set-version <Distro> 2
```
Podemos obtener `<Distro>` a partir del siguiente comando:
```Powershell
wsl --list
```
En nuestro caso tenemos las distribuciones que va a instalar Docker ya instaladas, pero podemos ver el nombre exacto de nuestra distribución Ubuntu.
![Out](https://i.imgur.com/6Q39tVG.png)

Hecho esto ya podemos instalar Docker.

#### Instalación de DOCKER
Podemos seguir la siguiente [guía oficial](https://docs.docker.com/desktop/windows/install/) o usar Winget, en nuestro caso vamos a usar el gestor de paquetes.
```Powershell
winget install -e --id Docker.DockerDesktop
```

#### Configuración de DOCKER
Si queremos acceder a los comandos de docker desde Ubuntu, debemos indicar a Docker que pueda utilizar Ubuntu como una interfaz más. 
Para ello podemos utilizar la interfaz gráfica de Docker Desktop.
![Configuración Docker](https://i.imgur.com/QgyYna0.png)

## Ejecución de la Práctica
**Es recomendable realizar todo el proceso desde un entorno Linux, como por el ejemplo Ubuntu WSL**
### Obtención del Repositorio
Si tenemos GIT instalado (recomendable usar Linux para evitar un problema específico), podemos utilizar el siguiente comando:

    $ git clone https://github.com/irg1008/practica-dms-2021-2022.git
Hecho esto ya deberíamos tener la carpeta `practica-dms-2021-202` en el directorio de trabajo

Accedemos a ella

    cd practica-dms-2021-202
Y ejecutamos los siguientes scripts:

    $ sudo bash bootstrap.sh
    $ bash run.sh
Podemos comprobar que todo funciona correctamente con `$ docker ps`
![enter image description here](https://i.imgur.com/wvuMPyR.png)
## Posibles Problemas
### Port Forwarding
El funcionamiento de Docker en Windows aísla a los contenedores del sistema en una red local propia, si queremos acceder a esta red desde nuestro equipo (localhost) es necesario configurar los contenedores para redireccionar su puerto a un puerto libre del host. 
El proyecto ya está configurado para usar un puerto específico para acceder al frontend, pero si queremos replicarlo podemos hacerlo de la siguiente manera desde el fichero de configuración de la imagen:

    services:
      auth:
      ...
    
      backend:
       ...
    
      frontend:
        build:
          ...
        image: ...
        container_name: dms2122frontend
        volumes:...
        networks:...
        ports:
          - "8080:8080"
        environment:...
      ...
Hemos añadido el siguiente fragmento:

    ports:
      - "8080:8080"
Que nos indica que el puerto del contenedor 8080 será asociado al puerto `localhost:8080`(o a la dirección IP de la máquina)
### Problema con los saltos de línea
Al trabajar desde Windows es posible que alguno de los ficheros cambie su salto de línea al del sistema *(al usar git pull, git clone, etc),* esto no debería ser ningún inconveniente excepto si tenemos en cuenta que BASH no admite los saltos de línea de windows, por lo que Docker no podrá construir los contenedores. 

Para evitar problemas hemos hecho el script run.sh que ejecuta el contenedor después de convertir los ficheros `.sh` a ficheros con salto de línea LF, se requiere una dependencia extra que se instala con `bootstrap.sh`. 


