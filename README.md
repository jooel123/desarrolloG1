# 🛡️ Proyecto BI – Counterfeit Product Detection

Este proyecto fue desarrollado por un grupo de tres integrantes con el propósito de aplicar un flujo de **Inteligencia de Negocios** empleando PostgreSQL, Python (pandas, SQLAlchemy) y Jupyter Notebooks.  

La fuente de información utilizada proviene del dataset https://www.kaggle.com/datasets/aimlveera/counterfeit-product-detection-dataset , el cual fue organizado en **DataFrames**, cada uno enfocado en un área clave para el análisis.


## 📊 1. DataFrame de Transacciones (`df_transacciones`)

### Descripción
En este DataFrame se registran todas las operaciones realizadas por los clientes. Se constituye como la base para los análisis financieros y de riesgo dentro del proyecto.

| Columna              | Descripción                                |
|----------------------|--------------------------------------------|
| transaction_id       | Identificador único de la transacción      |
| transaction_date     | Fecha de la operación                      |
| customer_id          | Cliente asociado                           |
| quantity, unit_price | Cantidad y precio unitario                 |
| total_amount         | Monto total                                |
| payment_method       | Forma de pago                              |
| shipping_speed       | Velocidad de envío                         |
| discount_applied     | Indicador de descuento aplicado            |
| refund_requested     | Solicitud de reembolso                     |
| velocity_flag        | Bandera de velocidad (fraude)              |
| geolocation_mismatch | Bandera de geolocalización                 |

### Filtros aplicados
1. Transacciones de alto valor (top 10% de `total_amount`).  
2. Operaciones con banderas de riesgo (`velocity_flag`, `geolocation_mismatch`, `refund_requested`).  
3. Compras con descuentos superiores al 30%.  


## 👤 2. DataFrame de Clientes (`df_clientes`)

### Descripción
Este conjunto de datos reúne métricas a nivel de cliente, con el fin de segmentar y analizar diferentes perfiles de usuarios.

| Columna                      | Descripción                                 |
|------------------------------|---------------------------------------------|
| customer_id                  | Identificador único del cliente             |
| total_pedidos                | Número de compras realizadas                |
| monto_total                  | Valor total acumulado                       |
| ticket_promedio              | Valor promedio de compra                    |
| tasa_reembolso               | Proporción de pedidos con devolución        |
| flags_riesgo                 | Número de alertas de fraude asociadas       |
| customer_location_mas_comun  | Ubicación más frecuente del cliente         |

### Filtros aplicados
1. Clientes VIP → top 10% en `monto_total`.  
2. Clientes riesgosos → `tasa_reembolso >= 30%` o `flags_riesgo > 0`.  
3. Clientes frecuentes → `total_pedidos >= 5`.  


## 🚚 3. DataFrame de Logística (`df_logistica`)

### Descripción
En este DataFrame se estudia el desempeño logístico, con especial atención en los tiempos de entrega y el cumplimiento de los SLA.

| Columna             | Descripción                              |
|---------------------|------------------------------------------|
| shipping_speed      | Modalidad de envío                       |
| delivery_time_days  | Tiempo real de entrega (días)            |
| shipping_cost       | Costo del envío                          |
| sla_dias            | SLA asignado según modalidad             |
| cumple_sla          | Indicador de cumplimiento del SLA        |

### Filtros aplicados
1. Envíos fuera de SLA (`cumple_sla = FALSE`).  
2. Envíos de alto costo (top 10% en `shipping_cost`).  
3. Envíos con demoras considerables (`delivery_time_days >= 10`).  


## ✅ Conclusiones

- **Transacciones** → se identifican operaciones sospechosas por fraude, alto valor o devoluciones frecuentes.  
- **Clientes** → se segmentan en perfiles estratégicos como VIP, frecuentes y de alto riesgo.  
- **Logística** → se evalúa la eficiencia de entregas, costos y el cumplimiento de SLA.  

La construcción de estos DataFrames, junto con sus respectivos filtros, permite establecer un flujo de **Inteligencia de Negocios** aplicable a la detección de fraude, la gestión de clientes clave y la optimización de procesos logísticos.
## 🚀 Tecnologías utilizadas
- **PostgreSQL + Docker** → base de datos principal.  
- **Python (pandas, SQLAlchemy)** → procesamiento y análisis de datos.  
- **Jupyter / DataSpell** → entorno de notebooks.  
- **Kaggle Dataset** → fuente de datos (CSV).

# 📘 ProyectoG1 – Componente Práctico S2

## 📌 Introducción
Este proyecto corresponde al **Componente Práctico S2** de la materia **Inteligencia de Negocios**.  
El objetivo principal fue **preparar y transformar datos de diferentes fuentes** para dejarlos listos para análisis, aplicando técnicas de **Exploración, Limpieza, Transformación y Expansión de DataFrames**.

En la práctica profesional, los datos rara vez llegan limpios: suelen contener errores, duplicados o formatos inconsistentes.  
Por eso, aplicamos un proceso **ETL (Extract, Transform, Load)**:

- **Extract (Extracción):** obtuvimos datos desde CSV y los cargamos en PostgreSQL.  
- **Transform (Transformación):** limpiamos, normalizamos y derivamos nuevas variables.  
- **Load (Carga):** guardamos las tablas listas en la base `maestria_bi`.  



## 🗂️ Fuentes de datos
Se trabajó con tres datasets principales:

1. **`counterfeit_transactions`**  
   - Contiene transacciones con información de fechas, montos, métodos de pago y banderas de fraude.  

2. **`customer_df`**  
   - Incluye información de clientes: correo, teléfono, IP, dirección de facturación y comportamiento histórico.  

3. **`olist_customers_dataset`**  
   - Proporciona identificadores de clientes junto con ubicación geográfica (código postal, ciudad, estado).  



## ⚙️ Desarrollo del Taller

### a. Exploración inicial
- Se identificaron columnas, registros y llaves candidatas (`transaction_id`, `customer_id`).  
- Descubrimos que `customer_df` no tenía `customer_id`, por lo que se generó un identificador artificial.

👉 **Utilidad:** reconocer cómo se relacionan los datasets y detectar problemas de calidad.



### b. Limpieza de datos
- Normalizamos nombres de columnas (`snake_case`).  
- Eliminamos duplicados.  
- Quitamos valores nulos en campos clave.  

👉 **Utilidad:** garantizar consistencia y evitar errores en análisis posteriores.


### c. Variables de entorno
Se creó un archivo **`.env`** con las credenciales de conexión a PostgreSQL.  

👉 **Utilidad:** proteger contraseñas y buenas prácticas de seguridad.



### d. Transformaciones
Aplicamos transformaciones relevantes:  
- **Transacciones:** derivamos `anio` y `mes` desde `transaction_date`.  
- **Clientes:** creamos `longitud_email` usando funciones `lambda`.  
- **Olist:** normalizamos `customer_city` y `customer_state`.  

👉 **Utilidad:** enriquecer los datos para análisis temporal, validación y segmentación.



### e. Expansión de DataFrames
Las nuevas variables fueron integradas en los DataFrames originales.  

👉 **Utilidad:** mantener datasets completos y listos para consultas.



### f. Índices numéricos
Se generaron IDs únicos y secuenciales:  
- `id_transaccion`  
- `id_cliente`  
- `id_olist`  

👉 **Utilidad:** asegurar integridad referencial y facilitar cruces en SQL.



## 📊 Visualización de resultados

Con los datos ya listos, construimos gráficas para extraer información:

1. **Distribución de montos de transacciones**  
   Permite detectar clientes con montos atípicamente altos o bajos.  

2. **Clientes por estado**  
   Muestra la concentración geográfica de clientes (útil en segmentación de mercado).  

3. **Transacciones por mes/año**  
   Identifica tendencias estacionales y patrones de compra.  



## 🚀 Utilidad del proyecto
- Integración de datos heterogéneos en una sola base relacional.  
- Aseguramiento de la calidad de los datos para análisis confiables.  
- Creación de indicadores clave (fraude, distribución geográfica, tendencias temporales).  
- Base preparada para **dashboards de BI** o **modelos predictivos**.  


## ✅ Conclusiones
- Los datos crudos no son útiles sin un proceso de limpieza y transformación.  
- La fase **Transformación (T en ETL)** es crucial para dar valor a la información.  
- Ahora contamos con una base de datos **integrada, normalizada y enriquecida**, lista para análisis estratégicos en Inteligencia de Negocios.  


## 👥 Autores
- Equipo G1 – Maestría en Ciberseguridad 
  * ORDOÑEZ VIVANCO MARIA FERNANDA
  * MUÑOZ SARMIENTO ANDERSON JOEL
  * ALAVA BOLAÑOS JENNY JULIZZA

- Universidad Internacional del Ecuador (UIDE)  
