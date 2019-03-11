# Programación Lógica 
La programación lógica, junto con la funcional, forma parte de  lo que se conoce como programación declarativa.
El paradigma lógico se fundamenta en las teorías de la lógica  proposicional  (Cláusulas  de  Horn),  manejando  lógica  de  predicados  con  una  sola  conclusión  en  cada  cláusula  y  un  conjunto de premisas de cuyo valor de verdad se deduce el  valor de verdad de la conclusión:
> **Nota:** una conclusión es cierta si lo son simultáneamente todas  sus premisas. 

En  los  lenguajes  tradicionales,  la  programación  consiste  en  indicar cómo resolver un problema mediante sentencias; en la  programación  lógica  al  ser  un  paradigma  de  la  rama  declarativa, un programa no tiene un algoritmo que indique  los pasos que detallen la manera de llegar a un resultado, sino  que  es  el  sistema  internamente  el  que  proporciona  la  secuencia  de  control,  se  trabaja  de  una  forma  descriptiva,  estableciendo relaciones entre entidades, indicando no cómo,  sino qué hacer.

La ecuación de Robert Kowalski (Universidad de Edimburgo)  establece la idea esencial de la programación lógica:
$$  
algoritmos = lógica + control 
$$
Es decir, un algoritmo se construye especificando conocimiento  en un lenguaje formal (lógica de primer orden), y el problema  se resuelve mediante un mecanismo de inferencia (control) que  actúa sobre aquél.

En el paradigma lógico no existe el concepto de asignación de  variables, sino el de unificación. No hay un “estado” de las  variables que se vaya modificando por sucesivas asignaciones,  generalmente asociadas a posiciones de memoria, sino que las  variables asumen valores al unificarse o “ligarse” con valores  particulares temporalmente y se van sustituyendo durante la  ejecución del programa.

Un programa lógico contiene una base de conocimiento sobre  la  que  se  hacen  consultas.  La  base  de  conocimiento  está  formada  por  hechos,  que  representan  la  información  del  sistema expresada como relaciones entre datos, y por reglas  lógicas  que  permiten  deducir  consecuencias  a  partir  de  combinaciones entre los hechos y, en general, otras reglas. 

Un programa lógico se construye especificando la información  del problema real en una base de conocimiento en un lenguaje  formal y el problema se resuelve mediante un mecanismo de  inferencia que actúa sobre ella. 
Una  clave  de  la  programación  lógica  es  poder  expresar  apropiadamente  todos  los  hechos  y  reglas  necesarios  que  definen el dominio de un problema. 

En  otros  paradigmas,  las  salidas  son  funcionalmente  dependientes de las entradas, por lo que el programa puede  verse  abstractamente  como  la  implementación  de  una  transformación  de  entradas  en  salidas.  En  cambio,  la  programación  lógica  está  basada  en  la  noción  de  que  el  programa  implementa  una  relación,  en  vez  de  una  transformación. 

Los predicados son relaciones, que al no tener predefinido una  “dirección”  entre  sus  componentes,  permiten  que  sus  argumentos  actúen  indistintamente  como  argumentos  de  entrada  y  salida.  Esta  característica  se  denomina  inversibilidad. 

A diferencia de las funciones donde está la restricción de la  unicidad  de  la  imagen  para  un  elemento  determinado  del  dominio, una relación permite vincular a cada elemento con  muchos otros elementos, permitiendo soluciones alternativas. 

Dado  que  las  relaciones  son  más  generales  que  las  transformaciones, la programación lógica es potencialmente de  más alto nivel que la de otros paradigmas.

Internamente,  existe  un  mecanismo,  un  “motor”,  que  actúa  como  control  de  secuencia.  Durante  la  ejecución  de  un  programa va evaluando y combinando las reglas lógicas de la  base de conocimiento para lograr los resultados esperados. 

Se  debe  garantizar  que  se  agoten  todas  las  combinaciones  lógicas  posibles  para  ofrecer  el  conjunto  completo  de  respuestas alternativas posibles a cada consulta efectuada. 

Dos  características  típicas  de  los  programas  lógicos  son  la  recursividad como estrategia lógica para encontrar soluciones  y la utilización de listas para representar conjuntos de valores.

Los  lenguajes  del  paradigma  lógico,  en  general  incluyen  herramientas para realizar soluciones polimórficas y manejar  el concepto de orden superior, entendido como la capacidad de  un  lenguaje  para  manejar  su  propio  código  como  una  estructura de datos más. 
 

El lenguaje Prolog, principal representante del paradigma, se  basa en un subconjunto de la lógica de primer orden. Philippe  Roussel y Alain Colmerauer (Universidad de Aix­Marseille) lo  crearon en 1972.

En PROLOG declaramos conocimiento de la siguiente manera:

```
mortal(X):­humano(X).  Regla
humano(socrates).  Hecho
```
Que  podemos  hacer  con  PROLOG  y  las  declaraciones  de  conocimiento siguientes: 
```
mortal(X):­humano(X).  Regla
humano(socrates).  Hecho

Sócrates, ¿es mortal? 		?- ­ mortal(socrates).
				    Yes
Maradona, ¿es mortal? 		?­- mortal(maradona).
				    No
¿Qué mortales conoce? 		?­-mortal(X). X = socrates
				    Yes

¿Hay algún mortal en la sala? 	?­-mortal(_).
			          Yes
```
## Esquema de una aplicación en programación lógica
![Esquema de una aplicación en programación lógica ](https://i.ibb.co/QXG6rYN/PROLOG.png) 
## Variable anonima
La traducción para la consulta lógica:
```
¿Hay algún mortal en la sala?  		?­-mortal(_).
					  Yes

```
existe x tal que p de x se cumple, donde p(x) significa que x es  mortal
## Principio de Universo cerrado
Cuando preguntamos:
 ```
¿Hay algún mortal en la sala?  		?­-mortal(maradona).
						  No

```
Bueno, eso es lo que se llama Principio de Universo Cerrado o  Negación por falla (Closed World assumption): todo lo que no  está en la base de conocimientos no se puede inferir si es cierto  o no, por lo tanto se asume falso.
## Ejemplo
```
padrede('juan','maria'). 
padrede('pablo','juan'). 
padrede('pablo','marcela'). 
padrede('carlos','debora').

hijode(A,B) :­ padre(B,A).
abuelode(A,B) :­ padrede(A,C), padrede(C,B).
hermanode(A,B) :­ padrede(C,A), padrede(C,B), A \== B.
familiarde(A,B) :­ padrede(A,B). 
familiarde(A,B) :­ abuelode(A,B). 
familiarde(A,B) :­ hermanode(A,B).
```
# Prolog
## Operadores
### Aritméticos
- "+, ­ , * , /"
-  // : cociente de la división (división entera) mod : resto de la división (módulo) 
-  ^ : potencia (primer operando elevado a segundo operando)
## #Relacionales
- ">, <, >=, <="
### Igualdad 
- = :unificación. Es verdadero si ambos operandos unifican, en  cuyo caso se realiza la unificación
> **Nota:** Dados 2 términos cualesquiera, T1 y T2,  para que se unifiquen en PROLOG uno de  ellos debe ser una variable no instanciada  y al final acabara tomando el valor del  otro.

- \= :no unificación. Es verdadero si ambos operandos NO  unifican, en cuyo caso NO se realiza la unificación.
- is :evaluador. Se utiliza para evaluar las expresiones  aritméticas y funciones. Evalúa la parte de la derecha y unifica  a la parte izquierda. Si no se usa el is, las expresiones se  mantienen en su forma original ( X=3+3 en lugar de X=6 ).
- = = :significa “es exactamente igual que”. Compara términos sin  evaluar expresiones.(no unifica). Ambos términos tienen que  estar instanciados.
- \= = :es falso cuando dos términos son exactamente iguales. (no  unifica).
- =:= :mismo valor. Evalúa los dos operandos, a derecha y a  izquierda, y es verdadero si los valores obtenidos son iguales.  (no unifica).

### Ejemplos

```
?­ X is 3+4.  
  X=7 
  Yes

?­ X+Y = 3+5.
  X=3, Y=5
 Yes
 
?­ X = 3+5.
  X=3+5
  Yes 
  
?­ X is 8,
  X = 3+5.
  No 
?­ X is 8, X is 3+5.
 X=8
 Yes
 
3 = = 1+2.
 No
 
3*3 =:= 9.
 Yes.
 
?­ X*Y = 9*a.
  X=9,Y=a
  Yes
```

```
precio(boligrafo, 0.5).
precio(folios, 2.5).
precio(portatil, 700).
precio(carro, 5000). precio(tomate, 2).

%% ¿Qué puedo comprar con 100 pesos? 
?­ precio( X,Y ), Y < 100.  
X=boligrafo, Y=0,5;
X=folios, Y=2,5;
X=tomates, Y=1;
No.

```

```
ganados( juan, 7 ).				?­ porcentaje(X,Y).
ganados( susana, 6 ).				X = juan, 
ganados( pedro, 2 ). 				Y = 53.84615384615385 ;
ganados( rosa, 5 ). 				X = susana,
jugados( rosa, 10 ). 				Y = 85.71428571428571 ;
jugados( juan, 13 ). 				X = pedro,
jugados( pedro, 3 ). 				Y = 66.66666666666666 ;
jugados( susana, 7 ).				X = rosa,	
						Y = 50.0.

porcentaje( X,Y ):­ ganados( X,Z ),jugados( X,Q ),Y is ( Z/Q )*100.
```
## Instanciación de variables con operadores
- Una variable está instanciada cuando Prolog le ha  asignado un valor.
- Los operadores aritméticos y relacionales necesitan que  todas las variables implicadas en la expresión  correspondiente estén instanciadas en el momento en que  se realiza la evaluación. En otro caso, Prolog nos avisará de  que las variables no están debidamente instanciadas. El  operador =:= se incluye en este grupo.
- ?-­5 =:= X + 4 – ¡Error! X no está instanciada y no se puede  realizar la suma.
- El operador is requiere que estén instanciadas las  variables del operando a la derecha.
- ?­-5 is X + 4 – ¡Error! X no está instanciada y no se puede  realizar la suma
- ?­-Y is 1 + 4 – Correcto: Y = 5
- Los operadores de unificación (=, \=) no requieren que las  variables estén instanciadas
- ?­- X = Y – Correcto: X=_G210, Y=_G210 (Las variables se  unifican a una misma)
Aunque en lógica no es importante el orden, sí que lo es en  Prolog:
- ?-­ 5 = X + 4, X = 1. – ¡Error! X no está aún instanciada y no  se puede realizar la suma
- ?­- X =1, 5 = X + 4. – Correcto: X = 1
- El predicado between/3 de Prolog sirve para instanciar  variables dentro de intervalos de enteros:
- ?-­ 5 is X –  ¡Error! X no está instanciada
- ?­-between(1,10,X), 5 is X. – Correcto: X = 5. (se instancia X  con valores de 1 a 10)


Con esto se evita el problema de buscar dentro de un  espacio infinito, ya que X puede tomar en principio  cualquier valor.

calcular la raíz cuadrada de 16 usando la operación de potencia  de 2 (inversa de funciones)
```
?­-between(1,10,X), 16 is X^2. – Correcto: X = 4.
```
## Funciones
Prolog implementa algunas funciones matemáticas:
- abs/1 : valor absoluto 
- cos/1 : coseno 
- sin/1 : seno 
- tan/1 : tangente 
- exp/1 : exponencial (ex) 
- log/1 : logaritmo en base e 
- sqrt/1 : raíz cuadrada 
- round/1 : redondeo 
- random/1 : número aleatorio


Las variables que aparecen en el argumento de las funciones  deben estar adecuadamente instanciadas.
```
?­ X is sqrt(6). –  Correcto: X=2.449
```
## Tipos de datos
Prolog no es un lenguaje con asignación de tipos fuerte.
- La lógica se preocupa más de las relaciones entre objetos  que del tipo de éstos, dando a todos ellos un tratamiento  similar.

Prolog incluye predicados que permiten clasificar términos:
- var/1 : verdadero si el término es una variable no  instanciada. 
- nonvar/1 : verdadero si el término no es una variable  instanciada. 
- atom/1 : verdadero si el término es un átomo de Prolog. 
- atomic/1 : verdadero si el término es átomo o número. 
- integer/1 : verdadero si el término es un entero. 
- float/1 : verdadero si el término es un real. 
- number/1 : verdadero si el término es un número
## Estructuras
La forma de introducir datos estructurados en Prolog es  sencilla. Por ejemplo:

![Estructura de personas](https://i.ibb.co/njF1Xsv/personas.png)
```
persona( nombre(‘Pedro’), apellido(‘López’), cc( 123456789 ) ).
persona( nombre(‘Ana’), apellido(‘Macías’), cc( 987654321 ) ).

%% Recuperar nombres y apellidos:
 ?­-persona( nombre(X), apellido(Y), _ ).
 X=‘Pedro’, Y=‘López’;
 X=‘Ana’, Y=‘Macías’;
 No.
```
De igual modo, podemos construir registros compuestos. Por  ejemplo:
![Registro compuesto ](https://i.ibb.co/q5xQ3sm/masp-ersonas.png)
```
partido( local( nombre( ‘America’ ), ciudad(‘Cali’) ),
visitante( nombre(‘Tolima’), ciudad(‘Tolima’) ), glocal(10), gvisit(0) ).
partido( local( nombre( ‘Nacional’ ), ciudad(‘Medellin’) ),
visitante( nombre(‘Equidad’), ciudad(‘Bogotá’) ), glocal(1), gvisit(2) ).
```
Predicado que nos dice si un equipo gana en su casa y el tanteo:
```
ganacasa(X,Y,Z,V):­partido(local(nombre(X),ciudad(Y)),_,tlocal(Z),tvisit(V)),  Z>V.
```
Consultar todos los equipos de Cali  que ganan en casa y los  tanteos

```
?­-ganacasa(X,’Cali’,Y,Z). X=‘America’, Y=10, Z=0; No
```
Consultar todos los equipos de Cali que ganan en casa por más  de 5 tantos:
```
?­-ganacasa(X,’Cali’,Y,Z), Y > Z+5. X=‘America’, Y=10, Z=0; No
```
## Árboles
En Prolog, los predicados pueden interpretarse como árboles: 
```
oracion( sujeto( ‘Pedro’ ), predicado( verbo( ‘come’ ),  objetodirecto( ‘bocadillo’ ) ) )
```
![arbol](https://i.ibb.co/BnpP8Bv/oracion.png)

Y, del mismo modo, pueden representarse árboles en forma de  predicados: 
```
arbol( a, arbol( c, arbol( 1, 2, 3 ) ),
```
![ejemplo árbol](https://i.ibb.co/KbzZbQ6/arbolito.png)
### Ejemplo
Escribir el recorrido en inorden de un árbol de expresión  aritmética 

![Arbol expresión aritmética](https://i.ibb.co/rZmv1zq/arbol.png)
```
% Utilizaremos el predicado % 
a( operador, hijo_izquierda, hijo_derecha ) 

% el árbol de la figura es: %
a( +, a( *, 3, 9 ), a( /, a( ­, 1, a( *,4,8 ) ), a(^,7,2) ) ) 

%Y deseamos obtener el recorrido en inorden:%
( (3*9) + ( ( 1 ­ (4*8) ) / (7^2) ) )

%Solución en Prolog
inord( a(OP,HI,HD) ):-  
write(‘(‘),inord(HI),write(OP),inord(HD),write(‘)’). inord(X):­write(X).

```
## Listas
Prolog implementa un tipo de dato especial: la lista. Una lista es  una serie de términos separados por comas entre corchetes:
```
[] 
[a,b,c]
[1,p(X),b,’Casa’]
```
Las listas también son términos, luego se permite el  anidamiento:
```
[ [], [ 1,2 ], a, [ [ 1 ], [ s, 1.4, 5 ] ] ]
```
Una secuencia de caracteres entre comillas es una cadena de  caracteres y Prolog la trata internamente como una lista de  enteros que se corresponden con los valores ASCII de los  caracteres en la cadena.
```
?­-X = “Pedro”. 
X = [ 80, 101, 100, 114, 111 ]
```
### Unificación de listas:
Dos listas unifican si sus componentes unifican una a una:
```
[X, Y, Z] = [a, b, c]  –  unifica 
[X, Y, Z] = [a, b, c, d] –  no unifica
```
Existe una sintaxis especial para la utilización de listas: la  sintaxis de barra. [ Cabeza | Cola ]
Donde Cabeza puede ser uno o varios términos separados por , y  Cola es una lista (que puede ser vacía) que representa a los  demás términos de la lista con la que se realiza la unificación.
Para la unificación con esta sintaxis, los términos de Cabeza  deben unificar uno a uno y Cola unifica con una lista que  contiene los términos restantes sin incluir aquellos que  unificaron con Cabeza.
### Ejemplos
Longitud de una lista: 
```
% Si queremos hallar la longitud de una lista. 
% La longitud de una lista vacia es 0. 
% La longitud de cualquier lista es la longitud de la cola + 1.

longitud([],0). 
longitud([_|T],N):-longitud(T,N0), N is N0 + 1.
?- longitud([a,b,c],L).   
	L = 3 
?- longitud([a,b,c],4).   
	No
```
Búsqueda de un elemento
```
% Si queremos determinar si un elemento pertenece a una lista. 
% El elemento pertenece a la lista si coincide con la cabeza de la lista. 
% El elemento pertenece a la lista si se encuentra en la cola de la lista.

pertenece(X,[X|_]) :- !.
 pertenece(X,[_|R]):- pertenece(X,R). 
 
?- pertenece(b,[a,b,c]).   
	Yes 
?- pertenece(b,[a,[b,c]]).   
	No 
?- pertenece([b,c],[a,[b,c]]).   
	Yes
```
Eliminar elemento de una lista
```
% Si queremos eliminar un elemento de la lista. 
% Si X es la cabeza de la lista, la cola T es la lista sin X 
% Si X no es la cabeza de la lista, conservamos la cabeza de la lista 
% como parte de la respuesta y continuamos eliminando X de la cola T.

elimina(X,[X|T],T). 
elimina(X,[H|T],[H|T1]):- elimina(X,T,T1).
 
?- elimina(1,[1,2,3,4],R).   
	R = [2,3,4]

```
Concatenar listas

```
% Si queremos concatenar dos listas lista. 
% Concatenar una lista vacia con L es L. 
% Concatenar X|L1 con L2 es poner el primer 
% elemento de la primera lista (X) más la 
% concatenación del resto de la lista (L1) con L2

concatenar([],L,L). 
concatenar([X|L1],L2,[X|L3]):-concatenar(L1,L2,L3).
 
?- concatenar([1,2],[3,4],R). 
	R = [1, 2, 3, 4].

```
Comprobar si una lista es la inversa de otra

```
% Si queremos calcular la inversa de una lista.
% La inversa de una lista vacía es una lista vacía 
% La inversa de H|T es la inversa de T concatenada con H.
 
inversa([],[]). 
inversa([H|T],L):-  inversa(T,R),  concatenar(R,[H],L).
 
?- inversa([a,b,c,d],[d,c,b,a]).   
	Yes/Si

```
