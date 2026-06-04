<<<<<<< HEAD
# 🌱 Proyecto: Sistema Inteligente de Monitoreo de Humedad del Suelo en un Cultivo de Fresa

## 📌 Título

**Tecnología al servicio del campo: Sistema inteligente de monitoreo de humedad del suelo para optimizar el riego en un cultivo de fresa en la Vereda Mancilla, Facatativá – Cundinamarca**

---

# 1. Introducción

La agricultura moderna enfrenta el reto de utilizar eficientemente los recursos hídricos debido al aumento de la demanda de alimentos y a las variaciones climáticas. En cultivos de fresa (*Fragaria × ananassa*), el control de la humedad del suelo es un factor determinante para garantizar un adecuado crecimiento, desarrollo radicular y producción de frutos.

El uso de tecnologías basadas en sensores y microcontroladores permite monitorear en tiempo real las condiciones del suelo, facilitando la toma de decisiones relacionadas con el riego y reduciendo el desperdicio de agua.

Por esta razón, se desarrolló un sistema de monitoreo utilizando Arduino UNO, un sensor de humedad FC-28 y un módulo RTC DS3231 para registrar mediciones periódicas de humedad en un cultivo de fresa ubicado en la Vereda Mancilla, municipio de Facatativá.

---

# 2. Planteamiento del problema

Los agricultores frecuentemente realizan el riego de forma empírica, basándose en observaciones visuales o experiencia previa.

Esta práctica puede generar:

* Exceso de agua.
* Déficit hídrico.
* Pérdida de nutrientes por lixiviación.
* Disminución de productividad.
* Incremento de costos de producción.

Por ello se requiere una herramienta tecnológica que permita conocer el estado real de humedad del suelo para optimizar el manejo del cultivo.

---

# 3. Justificación

La implementación de sistemas electrónicos de monitoreo permite mejorar la eficiencia en el uso del agua y favorecer una agricultura sostenible.

Los beneficios incluyen:

* Reducción del desperdicio de agua.
* Mayor precisión en las decisiones de riego.
* Disminución de estrés hídrico en las plantas.
* Mejor desarrollo vegetativo y productivo.
* Generación de información histórica para análisis posteriores.

---

# 4. Objetivo general

Diseñar e implementar un sistema de monitoreo de humedad del suelo basado en Arduino para evaluar el comportamiento hídrico de un cultivo de fresa y apoyar la toma de decisiones relacionadas con el riego.

---

# 5. Objetivos específicos

### Objetivo específico 1

Implementar un sistema electrónico de adquisición de datos utilizando Arduino UNO y un sensor de humedad FC-28.

### Objetivo específico 2

Registrar periódicamente los valores de humedad del suelo mediante un módulo RTC DS3231.

### Objetivo específico 3

Analizar las variaciones de humedad en diferentes momentos del día.

### Objetivo específico 4

Interpretar los resultados obtenidos para optimizar el manejo del riego.

---

# 6. Marco teórico

## Humedad del suelo

La humedad del suelo corresponde a la cantidad de agua presente entre las partículas del suelo.

Esta variable influye directamente en:

* Germinación.
* Absorción de nutrientes.
* Actividad microbiana.
* Desarrollo radicular.
* Productividad agrícola.

---

## Cultivo de fresa

La fresa requiere niveles adecuados de humedad debido a que posee un sistema radicular relativamente superficial.

Valores muy bajos generan:

* Marchitez.
* Reducción del crecimiento.
* Menor producción.

Valores excesivos generan:

* Asfixia radicular.
* Aparición de hongos.
* Pudrición de raíces.

---

## Agricultura de precisión

La agricultura de precisión consiste en utilizar tecnologías digitales para monitorear variables agrícolas y optimizar el manejo de cultivos.

Entre las tecnologías más utilizadas se encuentran:

* Sensores.
* Internet de las cosas (IoT).
* Sistemas de información geográfica.
* Automatización de riego.

---

# 7. Componentes del sistema

## Arduino UNO

Microcontrolador encargado de procesar la información proveniente del sensor.

Funciones:

* Leer datos analógicos.
* Procesar señales.
* Almacenar información temporalmente.
* Enviar resultados al computador.

---

## Sensor FC-28

Sensor encargado de medir la humedad del suelo mediante conductividad eléctrica.

Características:

* Alimentación: 3.3 – 5 V.
* Salida digital y analógica.
* Fácil integración con Arduino.

---

## RTC DS3231

Módulo de reloj en tiempo real.

Funciones:

* Registrar fecha.
* Registrar hora.
* Mantener precisión incluso sin energía principal.

---

# 8. Metodología

## Fase 1. Implementación

Montaje físico del sistema.

### Actividades

* Instalación de Arduino.
* Conexión del sensor FC-28.
* Conexión del RTC DS3231.
* Verificación del funcionamiento.

---

## Fase 2. Adquisición de datos

Se realizaron mediciones tres veces al día:

* Mañana.
* Tarde.
* Noche.

Durante varios días consecutivos.

---

## Fase 3. Procesamiento

Los datos obtenidos fueron organizados en tablas y posteriormente analizados mediante herramientas informáticas.

---

## Fase 4. Interpretación

Se compararon los cambios observados con eventos ambientales como:

* Riego.
* Lluvia.
* Evaporación.

---

# 9. Datos experimentales

Según los registros obtenidos:

| Día       | Mañana | Tarde | Noche |
| --------- | ------ | ----- | ----- |
| Lunes     | 208    | 209   | 210   |
| Martes    | 211    | 212   | 213   |
| Miércoles | 205    | 204   | 205   |
| Jueves    | 206    | 208   | 209   |
| Viernes   | 203    | 202   | 204   |
| Sábado    | 205    | 207   | 209   |
| Domingo   | 204    | 203   | 204   |

---

# 10. Análisis de resultados

Los datos muestran que la humedad presentó variaciones moderadas durante la semana.

### Martes

Se observaron los valores más altos de humedad:

* Mañana: 211
* Tarde: 212
* Noche: 213

Esto indica una adecuada disponibilidad de agua en el suelo.

---

### Viernes

Se registraron los valores más bajos:

* Mañana: 203
* Tarde: 202
* Noche: 204

Lo anterior puede asociarse a una mayor evaporación o consumo hídrico por parte de las plantas.

---

### Influencia del riego

Los incrementos observados después de eventos de riego demuestran la sensibilidad del sistema para detectar cambios en la humedad.

---

# 11. Modelo matemático

La dinámica de humedad puede representarse mediante:

[
\frac{dH}{dt}=rH\left(1-\frac{H}{H_{max}}\right)+\alpha R+\beta L-\gamma E
]

Donde:

* H = humedad del suelo.
* t = tiempo.
* r = tasa de crecimiento natural.
* Hmax = capacidad máxima de retención.
* R = aporte por riego.
* L = pérdidas por lixiviación.
* E = evaporación.
* α, β, γ = coeficientes de ajuste.

---

# 12. Impacto ambiental

La implementación del sistema contribuye a:

✅ Uso eficiente del agua.

✅ Reducción de desperdicios.

✅ Agricultura sostenible.

✅ Menor impacto ambiental.

✅ Optimización de recursos agrícolas.

---

# 13. Conclusiones

1. El sistema basado en Arduino UNO, sensor FC-28 y módulo RTC DS3231 permitió monitorear de manera efectiva la humedad del suelo en un cultivo de fresa.

2. Se identificaron variaciones de humedad asociadas a eventos de riego, lluvia y condiciones ambientales.

3. Los valores registrados mostraron un comportamiento relativamente estable, indicando condiciones favorables para el cultivo.

4. La automatización del monitoreo facilita la toma de decisiones relacionadas con el manejo del agua.

5. La implementación de tecnologías de bajo costo representa una alternativa viable para pequeños productores agrícolas.

---

# 14. Recomendaciones

* Incorporar sensores de temperatura y humedad ambiental.
* Implementar transmisión de datos vía WiFi.
* Desarrollar un sistema de riego automático.
* Aumentar el tiempo de monitoreo para obtener series históricas más robustas.
* Integrar análisis de datos mediante Python y Pandas.

---

# 15. Bibliografía

* FAO. Manejo eficiente del agua en agricultura.
* Arduino. Documentación técnica Arduino UNO.
* Principles of Soil Physics.
* Agricultura de Precisión.

=======
# 🌱 Proyecto: Sistema Inteligente de Monitoreo de Humedad del Suelo en un Cultivo de Fresa

## 📌 Título

**Tecnología al servicio del campo: Sistema inteligente de monitoreo de humedad del suelo para optimizar el riego en un cultivo de fresa en la Vereda Mancilla, Facatativá – Cundinamarca**

---

# 1. Introducción

La agricultura moderna enfrenta el reto de utilizar eficientemente los recursos hídricos debido al aumento de la demanda de alimentos y a las variaciones climáticas. En cultivos de fresa (*Fragaria × ananassa*), el control de la humedad del suelo es un factor determinante para garantizar un adecuado crecimiento, desarrollo radicular y producción de frutos.

El uso de tecnologías basadas en sensores y microcontroladores permite monitorear en tiempo real las condiciones del suelo, facilitando la toma de decisiones relacionadas con el riego y reduciendo el desperdicio de agua.

Por esta razón, se desarrolló un sistema de monitoreo utilizando Arduino UNO, un sensor de humedad FC-28 y un módulo RTC DS3231 para registrar mediciones periódicas de humedad en un cultivo de fresa ubicado en la Vereda Mancilla, municipio de Facatativá.

---

# 2. Planteamiento del problema

Los agricultores frecuentemente realizan el riego de forma empírica, basándose en observaciones visuales o experiencia previa.

Esta práctica puede generar:

* Exceso de agua.
* Déficit hídrico.
* Pérdida de nutrientes por lixiviación.
* Disminución de productividad.
* Incremento de costos de producción.

Por ello se requiere una herramienta tecnológica que permita conocer el estado real de humedad del suelo para optimizar el manejo del cultivo.

---

# 3. Justificación

La implementación de sistemas electrónicos de monitoreo permite mejorar la eficiencia en el uso del agua y favorecer una agricultura sostenible.

Los beneficios incluyen:

* Reducción del desperdicio de agua.
* Mayor precisión en las decisiones de riego.
* Disminución de estrés hídrico en las plantas.
* Mejor desarrollo vegetativo y productivo.
* Generación de información histórica para análisis posteriores.

---

# 4. Objetivo general

Diseñar e implementar un sistema de monitoreo de humedad del suelo basado en Arduino para evaluar el comportamiento hídrico de un cultivo de fresa y apoyar la toma de decisiones relacionadas con el riego.

---

# 5. Objetivos específicos

### Objetivo específico 1

Implementar un sistema electrónico de adquisición de datos utilizando Arduino UNO y un sensor de humedad FC-28.

### Objetivo específico 2

Registrar periódicamente los valores de humedad del suelo mediante un módulo RTC DS3231.

### Objetivo específico 3

Analizar las variaciones de humedad en diferentes momentos del día.

### Objetivo específico 4

Interpretar los resultados obtenidos para optimizar el manejo del riego.

---

# 6. Marco teórico

## Humedad del suelo

La humedad del suelo corresponde a la cantidad de agua presente entre las partículas del suelo.

Esta variable influye directamente en:

* Germinación.
* Absorción de nutrientes.
* Actividad microbiana.
* Desarrollo radicular.
* Productividad agrícola.

---

## Cultivo de fresa

La fresa requiere niveles adecuados de humedad debido a que posee un sistema radicular relativamente superficial.

Valores muy bajos generan:

* Marchitez.
* Reducción del crecimiento.
* Menor producción.

Valores excesivos generan:

* Asfixia radicular.
* Aparición de hongos.
* Pudrición de raíces.

---

## Agricultura de precisión

La agricultura de precisión consiste en utilizar tecnologías digitales para monitorear variables agrícolas y optimizar el manejo de cultivos.

Entre las tecnologías más utilizadas se encuentran:

* Sensores.
* Internet de las cosas (IoT).
* Sistemas de información geográfica.
* Automatización de riego.

---

# 7. Componentes del sistema

## Arduino UNO

Microcontrolador encargado de procesar la información proveniente del sensor.

Funciones:

* Leer datos analógicos.
* Procesar señales.
* Almacenar información temporalmente.
* Enviar resultados al computador.

---

## Sensor FC-28

Sensor encargado de medir la humedad del suelo mediante conductividad eléctrica.

Características:

* Alimentación: 3.3 – 5 V.
* Salida digital y analógica.
* Fácil integración con Arduino.

---

## RTC DS3231

Módulo de reloj en tiempo real.

Funciones:

* Registrar fecha.
* Registrar hora.
* Mantener precisión incluso sin energía principal.

---

# 8. Metodología

## Fase 1. Implementación

Montaje físico del sistema.

### Actividades

* Instalación de Arduino.
* Conexión del sensor FC-28.
* Conexión del RTC DS3231.
* Verificación del funcionamiento.

---

## Fase 2. Adquisición de datos

Se realizaron mediciones tres veces al día:

* Mañana.
* Tarde.
* Noche.

Durante varios días consecutivos.

---

## Fase 3. Procesamiento

Los datos obtenidos fueron organizados en tablas y posteriormente analizados mediante herramientas informáticas.

---

## Fase 4. Interpretación

Se compararon los cambios observados con eventos ambientales como:

* Riego.
* Lluvia.
* Evaporación.

---

# 9. Datos experimentales

Según los registros obtenidos:

| Día       | Mañana | Tarde | Noche |
| --------- | ------ | ----- | ----- |
| Lunes     | 208    | 209   | 210   |
| Martes    | 211    | 212   | 213   |
| Miércoles | 205    | 204   | 205   |
| Jueves    | 206    | 208   | 209   |
| Viernes   | 203    | 202   | 204   |
| Sábado    | 205    | 207   | 209   |
| Domingo   | 204    | 203   | 204   |

---

# 10. Análisis de resultados

Los datos muestran que la humedad presentó variaciones moderadas durante la semana.

### Martes

Se observaron los valores más altos de humedad:

* Mañana: 211
* Tarde: 212
* Noche: 213

Esto indica una adecuada disponibilidad de agua en el suelo.

---

### Viernes

Se registraron los valores más bajos:

* Mañana: 203
* Tarde: 202
* Noche: 204

Lo anterior puede asociarse a una mayor evaporación o consumo hídrico por parte de las plantas.

---

### Influencia del riego

Los incrementos observados después de eventos de riego demuestran la sensibilidad del sistema para detectar cambios en la humedad.

---

# 11. Modelo matemático

La dinámica de humedad puede representarse mediante:

[
\frac{dH}{dt}=rH\left(1-\frac{H}{H_{max}}\right)+\alpha R+\beta L-\gamma E
]

Donde:

* H = humedad del suelo.
* t = tiempo.
* r = tasa de crecimiento natural.
* Hmax = capacidad máxima de retención.
* R = aporte por riego.
* L = pérdidas por lixiviación.
* E = evaporación.
* α, β, γ = coeficientes de ajuste.

---

# 12. Impacto ambiental

La implementación del sistema contribuye a:

✅ Uso eficiente del agua.

✅ Reducción de desperdicios.

✅ Agricultura sostenible.

✅ Menor impacto ambiental.

✅ Optimización de recursos agrícolas.

---

# 13. Conclusiones

1. El sistema basado en Arduino UNO, sensor FC-28 y módulo RTC DS3231 permitió monitorear de manera efectiva la humedad del suelo en un cultivo de fresa.

2. Se identificaron variaciones de humedad asociadas a eventos de riego, lluvia y condiciones ambientales.

3. Los valores registrados mostraron un comportamiento relativamente estable, indicando condiciones favorables para el cultivo.

4. La automatización del monitoreo facilita la toma de decisiones relacionadas con el manejo del agua.

5. La implementación de tecnologías de bajo costo representa una alternativa viable para pequeños productores agrícolas.

El sistema permite monitorear variables ambientales relevantes para el cultivo de fresa.
---

# 14. Recomendaciones

* Incorporar sensores de temperatura y humedad ambiental.
* Implementar transmisión de datos vía WiFi.
* Desarrollar un sistema de riego automático.
* Aumentar el tiempo de monitoreo para obtener series históricas más robustas.
* Integrar análisis de datos mediante Python y Pandas.

---

# 15. Bibliografía

* FAO. Manejo eficiente del agua en agricultura.
* Arduino. Documentación técnica Arduino UNO.
* Principles of Soil Physics.
* Agricultura de Precisión.
>>>>>>> d535fbfc602d01b68cc88d3d79591340f69c0783
