Este código simula una tabla de Galton, que es un dispositivo que demuestra la ley de los grandes números y la distribución normal.

El código consta de dos partes principales: la función galton y la función histogram.

La función galton simula el movimiento de las bolas a través de la tabla de Galton. Cada bola comienza en la parte superior de la tabla y se 
mueve hacia la izquierda o la derecha en cada paso, de manera aleatoria. El número de pasos que toma cada bola es igual a num_steps. 
La posición final de cada bola se ajusta si se sale de los límites de la tabla. La posición final de cada bola se almacena en la lista order y 
también se utiliza para actualizar el recuento en la lista slots, que lleva un registro de cuántas bolas han terminado en cada posición.

La función histogram crea un histograma que muestra la distribución de las bolas en la tabla de Galton. Utiliza la lista order generada por la 
función galton para definir los intervalos del histograma y para determinar el número de bolas en cada intervalo.

Finalmente, si el script se ejecuta como el programa principal, se ejecuta la simulación de la tabla de Galton con 12 bolas y 3000 pasos, y 
luego se muestra el histograma de la distribución de las bolas.

CONCLUSION:

Este proyecto representó un desafío significativo para mí, ya que inicialmente me encontré algo perdido respecto a cómo empezar y con qué 
elementos abordarlo. Gracias a la orientación proporcionada por el docente, pude superar esta fase inicial y avanzar en la realización del 
proyecto. En términos generales, me complace haber llevado a cabo esta iniciativa. Resultó ser tanto entretenido como desafiante, con complicaciones 
que logre resolver mediante investigación y mejora de nuestra lógica para abordar diversos problemas que surgieron durante el proceso. 
Personalmente, considero que el bootcamp está resultando sumamente beneficioso, ya que nos expone a desafíos que nos instan a investigar, 
lo cual es un aspecto fundamental en este ámbito.
