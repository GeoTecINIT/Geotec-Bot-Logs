#!/usr/local/bin/python
# coding: utf-8
data = [[914, '10009', '10009', '¿Por qué no me explicas un chiste?', 140, 'tel-263536194', 1, '2016-07-13 11:06:40'],
[915, 'Chiste??? No soy muy buena en chistes', 'CHISTE NO SOY MUY BUENA EN CHISTES', '¿Me cuentas algo divertido?', 140, 'tel-263536194', 1, '2016-07-13 11:07:01'],
[916, 'Si seguro', 'SI SEGURO', 'Puede que estés en lo cierto.', 140, 'tel-263536194', 1, '2016-07-13 11:07:18'],
[917, 'Ahhhh', 'AHHHH', '¿Cómo estás de ansioso para la próxima película de Star Wars?', 140, 'tel-263536194', 1, '2016-07-13 11:08:05'],
[918, 'No estoy ansiosa, pues nunca he visto una', 'NO ESTOY ANSIOSA PUES NUNCA HE VISTO UNA', '¿Qué has hecho para estar ANSIOSA PUES NUNCA HE VISTO UNA?', 140, 'tel-263536194', 1, '2016-07-13 11:08:28'],
[919, 'No me llama la atención la historia', 'NO ME LLAMA LA ATENCIÓN LA HISTORIA', '¿Qué harías si en el futuro no existieran más los libros?', 140, 'tel-263536194', 1, '2016-07-13 11:08:51'],
[920, 'Pues los buscaría en internet', 'PUES LOS BUSCARÍA EN INTERNET', 'Internet es la mejor forma para perder el tiempo.', 140, 'tel-263536194', 1, '2016-07-13 11:09:12'],
[921, 'Pero siempre existirán', 'PERO SIEMPRE EXISTIRÁN', '¿Cómo se utiliza una bicicleta para moverse en la ciudad?', 140, 'tel-263536194', 1, '2016-07-13 11:09:19'],
[922, 'Pues puedes desplazarte de un lado a otro con mayor facilidad', 'PUES PUEDES DESPLAZARTE DE UN LADO A OTRO CON MAYOR FACILIDAD', '¿Cuál es tu película favorita?', 140, 'tel-263536194', 1, '2016-07-13 11:09:43'],
[923, 'Los juegos del hambre', 'LOS JUEGOS DEL HAMBRE', '¿A qué te gustaría jugar?', 140, 'tel-263536194', 1, '2016-07-13 11:09:56'],
[924, 'Baloncesto', 'BALONCESTO', 'Está todo el mundo por aquí comportandose como sí mismos?', 140, 'tel-263536194', 1, '2016-07-13 11:10:16'],
[925, 'Pues eso creo', 'PUES ESO CREO', '¿Por qué crees eso?', 140, 'tel-263536194', 1, '2016-07-13 11:10:58'],
[926, 'Si claro, cada quien con sus cosas', 'SI CLARO CADA QUIEN CON SUS COSAS', 'Perfecto.', 140, 'tel-263536194', 1, '2016-07-13 11:10:59'],
[927, 'Y puede que a veces se muestren como no son', 'Y PUEDE QUE A VECES SE MUESTREN COMO NO SON', '¿Has visto muchos gnomos por aquí?', 140, 'tel-263536194', 1, '2016-07-13 11:11:28'],
[928, 'Esta bien', 'ESTA BIEN', 'Bien, ¿y tú?', 140, 'tel-263536194', 1, '2016-07-13 11:11:34'],
[929, 'No', 'NO', 'Vale, si tú lo dices.', 140, 'tel-263536194', 1, '2016-07-13 11:11:36'],
[930, 'Y tu a qué te dedicas?', 'Y TU A QUÉ TE DEDICAS', 'Acabé los estudios de Turismo hace dos años.', 140, 'tel-263536194', 1, '2016-07-13 11:11:59'],
[931, 'Que bien', 'QUE BIEN', 'Bien.', 140, 'tel-263536194', 1, '2016-07-13 11:12:07'],
[932, 'Y trabajas?', 'Y TRABAJAS', 'Trabajo las 24 horas del día para ofrecerte el mejor servicio posible.', 140, 'tel-263536194', 1, '2016-07-13 11:12:10'],
[933, 'Claro', 'CLARO', 'Excelente.', 140, 'tel-263536194', 1, '2016-07-13 11:12:25'],
[934, 'Y específicamente tu trabajo es?', 'Y ESPECÍFICAMENTE TU TRABAJO ES', 'Soy el fruto de un largo trabajo de investigación en el campo de la Inteligencia Artificial.', 140, 'tel-263536194', 1, '2016-07-13 11:12:54'],
[935, 'Ah ok que bien', 'AH OK QUE BIEN', 'Bien.', 140, 'tel-263536194', 1, '2016-07-13 11:13:05'],
[936, 'Y qué es la inteligencia artificial?', 'Y QUÉ ES LA INTELIGENCIA ARTIFICIAL', 'La Inteligencia Artificial será en el futuro una tecnología puntera.', 140, 'tel-263536194', 1, '2016-07-13 11:13:19'],
[937, 'Vas a reemplazar lo que hace un humano?', 'VAS A REEMPLAZAR LO QUE HACE UN HUMANO', 'Puedes oler algo?', 140, 'tel-263536194', 1, '2016-07-13 11:13:39'],
[938, 'Si, dulce, por las galletas que están acá', 'SI DULCE POR LAS GALLETAS QUE ESTÁN ACÁ', 'Si los animales pudieran hablar nuestro idioma, ¿sería bonito?', 140, 'tel-263536194', 1, '2016-07-13 11:14:07'],
[939, '', '', '¿Alguna vez has pensado que podríamos hablar solo con emoticones?', 140, 'tel-263536194', 1, '2016-07-13 11:14:12'],
[940, 'No, los animales tienen otra forma de comunicarse', 'NO LOS ANIMALES TIENEN OTRA FORMA DE COMUNICARSE', '¿Prefieres los perros o los gatos?', 140, 'tel-263536194', 1, '2016-07-13 11:14:42'],
[941, 'Los gatos', 'LOS GATOS', '¿Crees que las computadoras serán más inteligentes que los humanos? Si sucede ¿Que crees que pasaría?', 140, 'tel-263536194', 1, '2016-07-13 11:14:47'],
[942, 'Me encantan', 'ME ENCANTAN', '¿En serio?', 140, 'tel-263536194', 1, '2016-07-13 11:14:50'],
[943, 'Si me encantan los gatos, son hermosos', 'SI ME ENCANTAN LOS GATOS SON HERMOSOS', 'Supongamos que la clonación es posible y accesible, ¿cuantos clones querrías?', 140, 'tel-263536194', 1, '2016-07-13 11:15:32'],
[944, 'Ninguno', 'NINGUNO', '¿Nada de nada?', 140, 'tel-263536194', 1, '2016-07-13 11:15:43'],
[945, 'No nada', 'NO NADA', '¿Nada de nada?', 140, 'tel-263536194', 1, '2016-07-13 11:15:49'],
[946, 'No le veo la necesidad', 'NO LE VEO LA NECESIDAD', 'Algunos me han dicho que han visto palomas decir palabras, ¿me crees?', 140, 'tel-263536194', 1, '2016-07-13 11:15:57'],
[947, 'No', 'NO', 'Vale, si tú lo dices.', 140, 'tel-263536194', 1, '2016-07-13 11:16:03']]