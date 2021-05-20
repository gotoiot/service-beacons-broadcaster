<a href="https://www.gotoiot.com/">
    <img src="_doc/gotoiot-logo.png" alt="logo" title="Goto IoT" align="right" width="60" height="60" />
</a>

Service Beacons Broadcaster
===========================

*Ayudaría mucho si apoyaras este proyecto con una ⭐ en Github!*

`Bluetooth` es un protocolo que sirve para crear redes personales de manera inalámbrica en la banda de 2.4 Ghz. `BLE` es la version low energy del protocolo Bluetooth orientada a dispositivos de bajo consumo. Las comunicaciones dentro de BLE pueden realizarse bajo el esquema `central-peripheral` o bien `broadcaster-observer`.

Dentro del tipo broadcaster-observer existe un subtipo de dispositivos que se comunican a través de paquetes `beacons`, emitiendo información periódica que otros dispositivos pueden capturar y reaccionar en consecuencia (observers). Dentro de los beacons existen distintos protocolos de comunicación. Los protocolos `iBeacon` desarrollado por Apple y `Eddystone` desarrollado por Google, son los más dominantes.

Este proyecto es un broadcaster de distintas tramas beacons que funciona sobre sistemas Linux que posean una placa con BLE. Está desarrollado en `Python` y se ejecuta sobre un contenedor de `Docker`. 

> Para que este servicio funcione deberías contar con un host que tenga Bluetooth LE 4.0+.

> El soporte actual es únicamente para tramas iBeacon.

## Instalar las dependencias 🔩

Para correr este proyecto es necesario que instales `Docker` y `Docker Compose`. 

<details><summary><b>Mira cómo instalar las dependencias</b></summary><br>

En [este artículo](https://www.gotoiot.com/pages/articles/docker_installation_linux/) publicado en nuestra web están los detalles para instalar Docker y Docker Compose en una máquina Linux. Si querés instalar ambas herramientas en una Raspberry Pi podés seguir [este artículo](https://www.gotoiot.com/pages/articles/rpi_docker_installation) de nuestra web que te muestra todos los pasos necesarios.

En caso que quieras instalar las herramientas en otra plataforma o tengas algún incoveniente, podes leer la documentación oficial de [Docker](https://docs.docker.com/get-docker/) y también la de [Docker Compose](https://docs.docker.com/compose/install/).

Continua con la descarga del código cuando tengas las dependencias instaladas y funcionando.

</details>

## Descargar el código 💾

Para descargar el código, lo más conveniente es que realices un `fork` de este proyecto a tu cuenta personal haciendo click en [este link](https://github.com/gotoiot/service-beacons-broadcaster/fork). Una vez que ya tengas el fork a tu cuenta, descargalo con este comando (acordate de poner tu usuario en el link):

```
git clone https://github.com/USER/service-beacons-broadcaster.git
```

> En caso que no tengas una cuenta en Github podes clonar directamente este repo.

## Ejecutar la aplicación 🚀

Cuando tengas el código descargado, desde una terminal en la raíz del proyecto ejecuta el comando `docker-compose build beacons-broadcaster` que se va encargar de compilar la imagen del broadcaster de beacons en tu máquina (este proceso puede durar unos minutos dependiento tu conexión a internet). 

Una vez que haya compilado activa el Bluetooth en el sistema y ejecutá el comando `docker-compose up` para acceder a todas las herramientas que tiene el servicio. En la terminal deberías ver una salida similar a la siguiente:

```
      /$$$$$$            /$$                    /$$$$$$      /$$$$$$$$
     /$$__  $$          | $$                   |_  $$_/     |__  $$__/
    | $$  \__/ /$$$$$$ /$$$$$$   /$$$$$$         | $$   /$$$$$$| $$   
    | $$ /$$$$/$$__  $|_  $$_/  /$$__  $$        | $$  /$$__  $| $$   
    | $$|_  $| $$  \ $$ | $$   | $$  \ $$        | $$ | $$  \ $| $$   
    | $$  \ $| $$  | $$ | $$ /$| $$  | $$        | $$ | $$  | $| $$   
    |  $$$$$$|  $$$$$$/ |  $$$$|  $$$$$$/       /$$$$$|  $$$$$$| $$   
     \______/ \______/   \___/  \______/       |______/\______/|__/   

                SERVICE BEACONS BROADCASTER
                ---------------------------

* Run iBeacon broadcaster:
    docker-compose run beacons-broadcaster \
        python bin/run_ibeacon_broadcaster.py \
            --device hci0 --major 20 --minor 10 --power 200

* Stop iBeacon broadcaster 
    docker-compose run beacons-broadcaster \
        python bin/stop_ibeacon_broadcaster.py --device hci0
```

Si ves esta salida significa que el servicio se encuentra corriendo adecuadamente. Ejecutá cualquiera de las utilidades que posee el servicio con los comandos que aparecen en la salida. Podés leer la información útil para tener un mejor entendimiento de la aplicación.

## Información útil 🔍

En esta sección vas a encontrar información que te va a servir para tener un mayor contexto.

<details><summary><b>Mira todos los detalles</b></summary>

### Comandos de los servicios

Cada uno de los servicios toman distintas configuraciones por defecto y si al momento de correr, en el comando de ejecución le pasas algunos flags, estos sobreescriben la configuración por defecto.

Este comando te muestra cómo ejecutar el broadcaster de iBeacons con todos los posibles flags.

```
docker-compose run beacons-broadcaster \
python bin/run_ibeacon_broadcaster.py \
--device hci0 \
--uuid ffffffff-bbbb-cccc-dddd-eeeeeeeeeeee \
--major 20 \
--minor 10 \
--power 200
```

Este comando te muestra cómo detener el broadcaster de iBeacons con todos los posibles flags.

```
docker-compose run beacons-broadcaster \
python bin/stop_ibeacon_broadcaster.py \
--device hci0
```

</details>

## Tecnologías utilizadas 🛠️

<details><summary><b>Mira la lista de tecnologías usadas en el proyecto</b></summary><br>

* [Docker](https://www.docker.com/) - Ecosistema que permite la ejecución de contenedores de software.
* [Docker Compose](https://docs.docker.com/compose/) - Herramienta que permite administrar múltiples contenedores de Docker.
* [Python](https://www.python.org/) - Lenguaje en el que están realizados los servicios.

</details>

## Contribuir 🖇️

Si estás interesado en el proyecto y te gustaría sumar fuerzas para que siga creciendo y mejorando, podés abrir un hilo de discusión para charlar tus propuestas en [este link](https://github.com/gotoiot/service-beacons-broadcaster/issues/new). Así mismo podés leer el archivo [Contribuir.md](https://github.com/gotoiot/gotoiot-doc/wiki/Contribuir) de nuestra Wiki donde están bien explicados los pasos para que puedas enviarnos pull requests.

## Sobre Goto IoT 📖

Goto IoT es una plataforma que publica material y proyectos de código abierto bien documentados junto a una comunidad libre que colabora y promueve el conocimiento sobre IoT entre sus miembros. Acá podés ver los links más importantes:

* **[Sitio web](https://www.gotoiot.com/):** Donde se publican los artículos y proyectos sobre IoT. 
* **[Github de Goto IoT:](https://github.com/gotoiot)** Donde están alojados los proyectos para descargar y utilizar. 
* **[Comunidad de Goto IoT:](https://groups.google.com/g/gotoiot)** Donde los miembros de la comunidad intercambian información e ideas, realizan consultas, solucionan problemas y comparten novedades.
* **[Twitter de Goto IoT:](https://twitter.com/gotoiot)** Donde se publican las novedades del sitio y temas relacionados con IoT.
* **[Wiki de Goto IoT:](https://github.com/gotoiot/doc/wiki)** Donde hay información de desarrollo complementaria para ampliar el contexto.

## Muestas de agradecimiento 🎁

Si te gustó este proyecto y quisieras apoyarlo, cualquiera de estas acciones estaría más que bien para nosotros:

* Apoyar este proyecto con una ⭐ en Github para llegar a más personas.
* Sumarte a [nuestra comunidad](https://groups.google.com/g/gotoiot) abierta y dejar un feedback sobre qué te pareció el proyecto.
* [Seguirnos en twitter](https://github.com/gotoiot/doc/wiki) y dejar algún comentario o like.
* Compartir este proyecto con otras personas.

## Autores 👥

Las colaboraciones principales fueron realizadas por:

* **[Agustin Bassi](https://github.com/agustinBassi)**: Ideación, puesta en marcha y mantenimiento del proyecto.

También podés mirar todas las personas que han participado en la [lista completa de contribuyentes](https://github.com/gotoiot/service-beacons-broadcaster/contributors).

## Licencia 📄

Este proyecto está bajo Licencia ([MIT](https://choosealicense.com/licenses/mit/)). Podés ver el archivo [LICENSE.md](LICENSE.md) para más detalles sobre el uso de este material.

---

**Copyright © Goto IoT 2021** - [**Website**](https://www.gotoiot.com) - [**Group**](https://groups.google.com/g/gotoiot) - [**Github**](https://www.github.com/gotoiot) - [**Twitter**](https://www.twitter.com/gotoiot) - [**Wiki**](https://github.com/gotoiot/doc/wiki)
