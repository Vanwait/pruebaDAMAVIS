# Resolución de la prueba técnica de DAMAVIS

## Aspectos de Diseño
Con este código he resulto con todos los resultados de los Test la prueba técnica de DAMAVIS.

Primero, el diagrama UML del código es el que aparece en la siguiente imagen.

![UMLDamavis drawio](https://github.com/Vanwait/pruebaDAMAVIS/assets/70864359/c1209054-695c-4725-8f13-365b964a09e0)

La resolución de este prueba la he hecho mediante un algoritmo basado en el diseño de Fuerza Bruta. Para ello, he utilizado como estructura de datos principal un árbol. 
Dado que no se permite el uso de librerías externas, lo he creado a mano, teniendo un orden máximo de 5, ya que son los posibles movimientos que puede tener el rectángulo.

En primera instancia, había pensado la utilización de un Árbol MiniMax ya que el problema se puede ver dentro de la toería de Juegos. Sin embargo, me costaba encontrar 
una métrica para evaluar qué tan buena era una jugada. Lo más simple sería la distancia entre el punto central del rectángulo y la esquina derecha del laberinto, que es la
casilla de vistoria. El problema son principalmente dos:
* La distancia no sería del todo buena dado que hay paredes intermedias, por lo que, aunque parezca una juegada prometedora porque está cerca de la victoria, a causa
  de las paredes, no es una buena jugada.
* La casilla central no es la que llegará a la casilla de la victoria, sino una de los extremos.

A causa de esto, decidí no implementar ninguna optimización y simplemente hacerlo por fuerza bruta. 


## Explicación de la ejecución

Primero, a partir del tablero se crea un objeto de tipo Game, el cual almacena el tablero y tiene funciones para evaluar si el movimiento del rectángulo es o no un movimiento
posible o ganador. 

Después empezamos con la creación del árbol. Cabe destacar que limpitamos la profundidad máxima dado que puede que hayan jugadas que tengan una profundidad excesiva y no sean
útiles. 

Primero creamos el nodo raíz, el cual contiene la posición del rectángulo, los hijos que tiene, la profundidad a la que se encuentra, el movimiento que hizo el padre para
llegar hasta esa posición, si está horizontal o vertical. El hecho de pasarle el tablero era solo para ver el desarrollo, pero no es necesario.

Una vez que tenemos el nodo Raíz, vamos al método recursivo de creación. Este coge el nodo padre, y mira un posible movimiento, en el caso de que este movimiento del rectángulo
no sea posible (chocarse con una pared '#' o salir fuera de los límites del laberinto), se descarta. También se descartan los movimiento inútiles, estos son aquellos que te 
devuelven a una posición anterior. Por ejemplo, si el nodo padre se ha movido hacia la izquierda, no es útil un movimiento hacia la derecha, ya que te dfevolvería a un estado anterior.


A la vez que se va creando el árbol, también se almacena la profundidad de un nodo hoja cuando este tiene un estado de victoria. Así, nos ahorramos luego hacer una búsqueda en
profundidad para hallar la resupuesta. 

Una vez que se ha creado un hijo con un movimiento válido, se hace una llamada recursiva a la función para hallar los hijos de este nuevo nodo creado.

Cabe destacar que, en el caso de que la juegada sea ganadora, no se crean hijos de esta.


