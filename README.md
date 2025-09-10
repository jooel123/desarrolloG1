# 🛡️ Proyecto BI – Counterfeit Product Detection

Este proyecto implementa un flujo de **Inteligencia de Negocios** usando PostgreSQL, Python (pandas, SQLAlchemy) y Jupyter Notebooks.  
Se trabaja con el dataset de [Counterfeit Product Detection](https://www.kaggle.com/datasets/aimlveera/counterfeit-product-detection-dataset), estructurándolo en **tres DataFrames principales** para análisis.

---

## 📊 1. DataFrame de Transacciones (`df_transacciones`)

### Descripción
Contiene cada operación registrada en el dataset. Es la fuente base para análisis financiero y de riesgo.

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
1. **Transacciones de alto valor** → top 10% de `total_amount`.  
2. **Transacciones con banderas de riesgo** → `velocity_flag`, `geolocation_mismatch`, `refund_requested`.  
3. **Transacciones con descuentos altos** → `discount_percentage >= 30%`.

---

## 👤 2. DataFrame de Clientes (`df_clientes`)

### Descripción
Agrupa métricas a nivel de cliente para segmentación de usuarios.

| Columna                  | Descripción                                 |
|--------------------------|---------------------------------------------|
| customer_id              | Identificador único del cliente             |
| total_pedidos            | Número de compras realizadas                |
| monto_total              | Valor total acumulado                       |
| ticket_promedio          | Valor promedio de compra                    |
| tasa_reembolso           | Proporción de pedidos con devolución        |
| flags_riesgo             | Número de alertas de fraude asociadas       |
| customer_location_mas_comun | Ubicación más frecuente del cliente     |

### Filtros aplicados
1. **Clientes VIP** → top 10% en `monto_total`.  
2. **Clientes riesgosos** → `tasa_reembolso >= 30%` o `flags_riesgo > 0`.  
3. **Clientes frecuentes** → `total_pedidos >= 5`.

---

## 🚚 3. DataFrame de Logística (`df_logistica`)

### Descripción
Evalúa desempeño logístico y cumplimiento de SLA (tiempo objetivo de entrega).

| Columna             | Descripción                              |
|---------------------|------------------------------------------|
| shipping_speed      | Modalidad de envío                       |
| delivery_time_days  | Tiempo real de entrega (días)            |
| shipping_cost       | Costo del envío                          |
| sla_dias            | SLA asignado según modalidad             |
| cumple_sla          | Indicador de cumplimiento del SLA        |

### Filtros aplicados
1. **Envíos fuera de SLA** → `cumple_sla = FALSE`.  
2. **Envíos costosos** → top 10% en `shipping_cost`.  
3. **Envíos lentos** → `delivery_time_days >= 10`.

---

## ✅ Conclusiones

- **Transacciones** → permiten identificar operaciones sospechosas (fraude, alto valor, devoluciones).  
- **Clientes** → se segmentan en VIP, frecuentes y riesgosos.  
- **Logística** → se mide eficiencia, costos y cumplimiento de SLA.  

Este esquema de **3 DataFrames + filtros** habilita un pipeline de **Inteligencia de Negocios** útil para detección de fraude, análisis de clientes estratégicos y optimización logística.

---

## 🚀 Tecnologías utilizadas
- **PostgreSQL + Docker** → base de datos principal.  
- **Python (pandas, SQLAlchemy)** → procesamiento y análisis de datos.  
- **Jupyter / DataSpell** → entorno de notebooks.  
- **Kaggle Dataset** → fuente de datos (CSV).

---
