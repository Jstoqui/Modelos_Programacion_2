
# Introducción  al paradigma funcional!
Tradicionalmente  la  visión  de  la  programación  que  se  tiene  por  la  gran  mayoría de personas vinculadas como estudiante o  profesionales al desarrollo de software  solo  tiene  en cuenta  la secuencia  de  instrucciones que se  le  debe dar  al computador para que ejecute una tarea.

Una  visión  general  de  la  programación  debe  incluir  otros  aspectos  o modelos  de programar  una  computadora,  entonces,  se  debe definir  la  programación  como  el análisis  y la  solución  de  problemas  mediante  la  descripción  de  valores, propiedades y  métodos, el  diseño  de  algoritmos correctos  y  eficientes  y  de estructuras  de datos  que soporten dicha solución.

De  acuerdo  con  esta  visión  de  la  programación  la  visión  tradicional  solo  forma una  parte  pequeña  de una  visión global,  es  decir  que  la  programación imperativa, solo forma  parte  de  un  universo de posibilidades  para el  desarrollo  de  estas soluciones.

Un  **paradigma  de  programación**  es  un  modelo  básico  de  diseño  e implementación  de  programas,  un  modelo  que  permite desarrollar  programas conforme  a  ciertos  principios  o  fundamentos  específicos  que  se  aceptan como válidos.

Un  paradigma,  es  una  colección  de  modelos  conceptuales  que  juntos modelan  el proceso  de  diseño,  orientan  la  forma  de  pensar  y solucionar  los  problemas  y,  por lo tanto,  determinan la estructura final de un programa.

Los  paradigmas  de  programación  abarcan dos  ramas principales:  ***imperativa*** y ***declarativa***, estas ramas  abarcan los  diferentes  paradigmas de programación:

## Rama Imperativa (procedimentales)
En  esta  rama  están  los  paradigmas  que  indican  el  modo  de  construir  la  solución, detallando paso a paso  el mecanismo para la obtención de esta.

 - Paradigma  estructurado. 
 - Paradigma  orientado  a objetos.
## Rama Declarativa
En  esta  rama  se  describen  lasa  características  que  debe  tener  la  solución,  es decir que se debe obtener pero no como obtenerla.
 - Paradigma  funcional.
 - Paradigma  lógico.

Los  lenguajes de programación  ***imperativos*** evolucionaron desde los  lenguajes ensambladores,  por  esto  se  basan  en el  conocimiento  de  una  arquitectura física de  las máquinas para operar sobre dicha arquitectura.

Los  lenguajes ***imperativos***  dejan  de lado los  procesos  de pensamiento de los programadores.

Por  otro  lado,  los  lenguajes  de programación  ***funcionales*** tratan  el  problema  de  la programación desde un punto  de  vista matemático, utilizando  la  noción  de función como base para la construcción de los algoritmos y  estructuras de datos.

En los lenguajes  ***imperativos*** existen dos tipos de construcciones:  las instrucciones  de  control  y las  expresiones.  Las  instrucciones  de  control  permiten manejar  explícitamente  el  flujo  de  control,  y las  expresiones  son  utilizadas  para calcular valores.
Los  lenguajes ***imperativos*** poseen  la  característica  de  poder  realizar modificaciones  implícitas  a  la  memoria  de  la  computadora.  A  estas  modificaciones se  las  conocen como *"efectos  laterales"*,  ya que  no son claramente visibles en el código  del  programa,  y tienen  consecuencias  no  deseables  para  el  razonamiento de  propiedades.

A  modo de ejemplo de un programa en el paradigma ***imperativo***:
```haskell
Procedimiento factorial(x):
	n<-x;
	a<-1;
	mientras  (n>0) hacer 
		a<a*n;
		n<n-1; 
	fin mientras 
	retorne a;
fin procedimiento
}
```
En matemáticas  no existe  la  noción  de  **estado  implícito** que puede  ser modificado,  haciendo  innecesaria la  presencia  de  instrucciones. En  cambio existen valores  (inmutables)  que  pueden  ser  expresados  de  maneras  complejas mediante  expresiones;  el  conjunto  de  valores  conocidos  conforman de  esta manera un estado  explícito,  dando como resultado un lenguaje estático.

El cálculo de  dichos valores  se realiza mediante un  proceso de reemplazo de subexpresiones  que no tienen  un orden preestablecido,  dando como resultado un control implícito de operación.

Al no existir  **efectos laterales**,  dos expresiones  sintácticamente iguales darán el mismo  valor,  propiedad  conocida  como  **transparencia  referencial**;  esta propiedad  es  el  pilar  de  la  habilidad  de  razonamiento.  Por ello,  aumentar  el  nivel de  abstracción mantiene la coherencia con el modelo subyacente.

Ahora  veamos  el  ejemplo  anterior  expresado  respetando  un  modelado  dentro  del paradigma  funcional:
```haskell
factorial::Int->Int
factorial 0 = 1
factorial n = n * factorial(n-1)
```
Vemos  una  forma de  implementar  una solución que  esta mas  cercana al razonamiento  del  programador  y no  una  secuencia  de  instrucciones  orientadas más hacia la arquitectura  de una máquina que a un razonamiento matemático.


# Paradigma Funcional
Existen dos grandes  categorías  de lenguajes  funcionales:  los funcionales **puros** y los **híbridos**.

La  diferencia entre ambos estriba en que los lenguajes  funcionales  híbridos  son menos dogmáticos que los puros,  al admitir conceptos tomados de los lenguajes imperativos,  como las  secuencias de  instrucciones  o  la asignación de variables.

En contraste,  los lenguajes funcionales puros tienen una mayor potencia expresiva,  conservando  a  la  vez su transparencia  referencial,  algo  que  no se cumple siempre  con un lenguaje funcional híbrido.

En resumen podemos decir que:

 - El paradigma de programación funcional trata la computación como la evaluación  de funciones  matemáticas  y  evita los  estados y  datos mutables.
 - El  paradigma  de  programación  funcional  hace  énfasis  en  la  aplicación  de funciones,  en  contraste  con  el  estilo  de  programación  ***imperativo***  que  pone  el énfasis en los  cambios  de estado.
 - Los  cálculos  se  ven  como  una  función  matemática  que  hace  corresponder entradas y  salidas.
 - No hay noción de posición de memoria y por tanto, necesidad de una instrucción de asignación.
 - Los  bucles  se  modelan  a  través  de  la  recursividad  ya  que  no  hay  manera  de incrementar  o disminuir  el  valor  de una variable.
 - Un programa funcional es una expresión simple que es ejecutada por evaluación  de  la  expresión.  El  foco  se  centra  en  **QUÉ** va  a  ser  computado,  no en **CÓMO** va a hacerlo.

## Expresiones y  valores
La  noción  de expresiones  es  central en la programación funcional.  La característica  más  importante de  la  notación  matemática  es  que  una expresión  se usa  para  denotar  o  describir  un  valor.  En otras  palabras,  el  significado  de  una expresión es  su valor y  no existen efectos  laterales ocultos.

## Funciones
Una  función en  programación  funcional  tiene  dos  partes  importantes,  la declaración,  donde  se  indica  el  nombre  de  la  función, los  tipos  de  parámetros  que recibe  y el  tipo  de  retorno  de  la función (la  declaración  puede  ser  implícita)  y la definición o  definiciones  de la función.

Por  ejemplo  veamos  en  el  lenguaje   [Haskell](https://www.haskell.org/) como  queda  definida la  función factorial de los ejemplos anteriores.
```haskell
factorial::Int->Int
factorial 0 = 1
factorial n = n * factorial(n-1)
```
En  donde  en  negrillas  se  hace  la  declaración  de  la  función  factorial  y  el  resto  son las definiciones  de la función.

Estas  funciones  se  guardan  en  un  archivo  de  texto  plano  que  define  un  script  que será cargado por  Haskell.
>En estos scripts  se pueden definir  módulos de funciones.
## Reducción de expresiones
El computador  evalúa una expresión reduciéndola a su forma equivalente más simple  e imprimiendo  su  resultado.  Vamos  a  ve  un  ejemplo para  describir  este proceso.
Vamos a reducir la siguiente expresión:
```haskell
cuadrado (3 + 4)
```
Pero  antes recordemos  como estaría definida la  función cuadrado:

```haskell
cuadrado::Int->Int
cuadrado x = x * x
```
Una forma sería:
```haskell
cuadrado (3+4)
	cuadrado 7	(+)
	7 * 7		(cuadrado)
	49		(*)
```
Esta forma  de  evaluar  una  función  recibe  el  nombre  de  evaluación por  valor, evaluación  ansiosa  o  impaciente  y consiste  en  reducir  primero  las  expresiones que manejan valores  para luego  pasarlas por  valor  a las funciones.

`[TOC]`
