# 🛡️ Proyecto BI – Counterfeit Product Detection

Este proyecto fue desarrollado por un grupo de tres integrantes con el propósito de aplicar un flujo de **Inteligencia de Negocios** empleando PostgreSQL, Python (pandas, SQLAlchemy) y Jupyter Notebooks.  

La fuente de información utilizada proviene del dataset https://www.kaggle.com/datasets/aimlveera/counterfeit-product-detection-dataset , el cual fue organizado en **DataFrames**, cada uno enfocado en un área clave para el análisis.

---

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

---

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

---

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

---

## ✅ Conclusiones

- **Transacciones** → se identifican operaciones sospechosas por fraude, alto valor o devoluciones frecuentes.  
- **Clientes** → se segmentan en perfiles estratégicos como VIP, frecuentes y de alto riesgo.  
- **Logística** → se evalúa la eficiencia de entregas, costos y el cumplimiento de SLA.  

La construcción de estos DataFrames, junto con sus respectivos filtros, permite establecer un flujo de **Inteligencia de Negocios** aplicable a la detección de fraude, la gestión de clientes clave y la optimización de procesos logísticos.

---

