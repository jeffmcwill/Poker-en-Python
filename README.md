# Poker-Python
juego de póker escrito en Python (proyecto completo)

¡POKER EN PYTHON!

juego de poker de jugador con ia, escrito por mi en python3, con uso de libreria numpy.

* ¿Como jugar?

este codigo, es una version mas sencilla del juego, contando solo con 2 jugadores, maquina contra jugador o jugador contra maquina.
se debe apostar cierto dinero (el que queramos) y gana quien tenga la cantidad de cartas mas alta en la mesa, normalmente solo se
pueden elegir hasta 5 cartas en una mano para poder llegar a un numero alto, mas de eso no se podra, ademas que podremos apostar
lo que queramos, siempre y cuando tengamos el dinero suficiente, si no perderemos.

* CAPTURAS DEL JUEGO: 

1. Como primer paso, descargamos el juego y lo ejecutamos con doble click en el archivo .py

![pok1](https://user-images.githubusercontent.com/111131531/212674251-1bb4a0ad-5a0a-4e34-9cf8-71448beae755.png)

2. al ejecutarlo, aparecera la pantalla principal, con las dos opciones, iniciar juego y salir. 

![pok2](https://user-images.githubusercontent.com/111131531/212674434-1919086d-3544-4b3e-a341-41ea496afe9d.png)

3. al empezar, te aparecera un menu con bastante informacion.

![pok3](https://user-images.githubusercontent.com/111131531/212674994-119619e8-5371-41a3-a70a-96d5b152e9d0.png)

-en primero esta el "Dinero", que sera de 500.
-en segundo "Cartas", que te da la cantidad de cartas que poseen ambos jugadores, la pc y el jugador
-como tercero "Partida", que te dira la cantidad de partidas jugadas por el jugador.

despues esta la informacion de ambos jugadores.
CRUPIER: te muestra sus cartas (no el valor de sus cartas, por que eso seria trampa), pero si la cantidad
que posee en su mano.
JUGADOR: "las cartas" que tienes en tu mano y sus valores y el "total" que valen esas cartas

despues de todo eso, estan las opciones que el jugador puede tomar.

4. Opciones en cada funcion

si presionamos "1", nos dara una carta de la baraja (tomar en cuenta que el crupier tambien obtendra otra carta mas):

![pok4](https://user-images.githubusercontent.com/111131531/212676387-1f1df5da-f3ec-461c-8f9e-b41c09774bec.png)

![pok5](https://user-images.githubusercontent.com/111131531/212676348-4ff39a2b-41d5-4d15-92f8-25b08d000329.png)

esto tiene un limite de 5 cartas, que el jugador puede obtener de la baraja. mas haya de eso, no te dejara.

si presionamos "3", nos llevara al menu de apuesta.

![pok6](https://user-images.githubusercontent.com/111131531/212676813-31eb6fa4-8d85-4b7c-95f7-dd542c2478ac.png)

podremos apostar lo que queramos... Hasta todo el dinero que tengamos (aunque es muy peligroso ajaj)

![pok7](https://user-images.githubusercontent.com/111131531/212676829-709ff383-d906-4b66-9291-e2641a671d70.png)

![pok8](https://user-images.githubusercontent.com/111131531/212677184-480b076e-5b66-4811-ac57-3dbd84f86bfa.png)

![pok9](https://user-images.githubusercontent.com/111131531/212677218-76d5de79-0e8d-4588-9493-d3aad0552e84.png)

una vez apostado, nos volvera a la tabla de juego.

notaremos con la seccion "POZO" que se agregara la cantidad de dinero que nosotros pusimos mas lo que agregue el bot.
(la ia del juego, siempre apostara una cantidad similar a la que apuesta el jugador.)

![pok10](https://user-images.githubusercontent.com/111131531/212677574-28b8004b-91dd-458d-a3b5-c19511de1c69.png)

Ahora una vez tenido las cartas y la apuesta, debemos presionar 2 para "quedarnos"

![pok11](https://user-images.githubusercontent.com/111131531/212677594-9cbf45ee-f5ce-4a6c-bbd8-21ac1c821718.png)

y con suerte ganaremos...

![pok15](https://user-images.githubusercontent.com/111131531/212678114-3c6c5a3e-7bd4-4ff0-8134-a077b91faa86.png)

o perderemos.

![pok12](https://user-images.githubusercontent.com/111131531/212678168-80d6fd9f-ae58-4bfc-b2a8-67cd41e26ce7.png)

Ahora si presionamos 4, el juego cierra.

![pok13](https://user-images.githubusercontent.com/111131531/212678805-6bc1a4e9-b841-47ac-9462-b6f65c3aa1d5.png)

una vez que perdamos o ganemos, el dinero se modificara, obteniendo lo que apostamos mas lo que puso el contrincante o perdiendo ese dinero
que apostamos, ademas, en la seccion de partidas, aumentara a +1 cada vez que pase una partida.

si nosotros llegamos a quedarnos sin dinero en nuestras apuestas, perderemos el juego.

![pok14](https://user-images.githubusercontent.com/111131531/212679309-cb1092f2-cfa7-4910-9032-0308fdd46eb5.png)

pero si ganamos todas nuestras apuestas, la mesa se quedara sin dinero y GANAREMOS :3

![pok16](https://user-images.githubusercontent.com/111131531/212679945-08ceb035-48d5-481d-a8fd-81d26fac817c.png)

en ambos casos, te dira cuantas partidas ganaste y perdiste (es mas un dato estadistico).

Espero que te guste mi proyecto, me llevo una tarde aburrida de domingo, pero valio la pena, quedo bastante bien :).

Muchas gracias...

Jeff McWill 16/1/23
