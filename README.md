# 🛡️ Proyecto BI – Inteligencia de Negocios

Este proyecto integra **tres fuentes de datos distintas**, cada una cargada en **PostgreSQL** y analizada con **Python (pandas, SQLAlchemy, Jupyter)**.  
El objetivo es construir **DataFrames principales** para exploración, aplicar filtros representativos y generar valor de negocio a partir de los datos.

---

## 📂 1. Counterfeit Product Detection Dataset

**Fuente:** Kaggle – [Counterfeit Product Detection](https://www.kaggle.com/datasets/aimlveera/counterfeit-product-detection-dataset)  
**Tabla en PostgreSQL:** `counterfeit_transactions`

### DataFrames principales
- **Transacciones (`df_transacciones`)**  
  Variables: `transaction_id`, `transaction_date`, `customer_id`, `quantity`, `unit_price`, `total_amount`, `payment_method`, `shipping_speed`, `discount_applied`, `refund_requested`, `velocity_flag`, `geolocation_mismatch`.  
  - Filtros:
    1. Transacciones de alto valor (top 10%).  
    2. Transacciones con banderas de riesgo.  
    3. Transacciones con descuentos elevados.

- **Clientes (`df_clientes`)**  
  Variables agregadas: `total_pedidos`, `monto_total`, `ticket_promedio`, `tasa_reembolso`, `flags_riesgo`, `customer_location_mas_comun`.  
  - Filtros:
    1. Clientes VIP (top 10% por monto).  
    2. Clientes riesgosos (alto reembolso o banderas de fraude).  
    3. Clientes frecuentes (≥ 5 pedidos).

- **Logística (`df_logistica`)**  
  Variables: `shipping_speed`, `delivery_time_days`, `shipping_cost`, `sla_dias`, `cumple_sla`.  
  - Filtros:
    1. Envíos fuera de SLA.  
    2. Envíos costosos (top 10%).  
    3. Envíos lentos (≥ 10 días).

---

## 📂 2. Olist Customers Dataset

**Fuente:** Kaggle – [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)  
**Tabla en PostgreSQL:** `olist_customers`

### DataFrames principales
- **Clientes (`df_clientes`)**  
  Variables: `customer_id`, `customer_unique_id`, `customer_zip_code_prefix`.  
  - Filtros:
    1. Clientes únicos por `customer_unique_id`.  
    2. Clientes con ZIP > 90000.  
    3. Clientes duplicados en `customer_id`.

- **Ubicaciones (`df_ubicaciones`)**  
  Variables: `customer_city`, `customer_state`.  
  - Filtros:
    1. Clientes de São Paulo (`SP`).  
    2. Clientes de las 10 ciudades más frecuentes.  
    3. Clientes fuera de SP y RJ.

- **Identificadores (`df_identificadores`)**  
  Variables: `customer_id`, `customer_unique_id`.  
  - Filtros:
    1. Conteo de IDs únicos.  
    2. Duplicados en `customer_unique_id`.  
    3. Top 10 IDs más repetidos.

---

## 📂 3. Customer_DF Dataset

**Fuente:** Dataset académico de fraude en clientes.  
**Tabla en PostgreSQL:** `customer_df`

### DataFrames principales
- **Contacto (`df_contacto`)**  
  Variables: `customerEmail`, `customerPhone`, `customerDevice`, `customerIPAddress`.  
  - Filtros:
    1. Emails con dominio `gmail.com`.  
    2. Dispositivos móviles.  
    3. IPs duplicadas.

- **Transacciones (`df_transacciones`)**  
  Variables: `No_Transactions`, `No_Orders`, `No_Payments`.  
  - Filtros:
    1. Clientes con > 5 transacciones.  
    2. Clientes con > 3 órdenes.  
    3. Clientes con 0 pagos.

- **Riesgo (`df_riesgo`)**  
  Variables: `customerBillingAddress`, `No_Transactions`, `Fraud`.  
  - Filtros:
    1. Clientes marcados como fraude.  
    2. Direcciones de facturación duplicadas.  
    3. Clientes con fraude y más de 2 transacciones.

---

## ✅ Conclusiones Generales

- **Counterfeit** → Permite detectar fraude en transacciones y optimizar logística.  
- **Olist** → Centrado en datos de clientes, útil para segmentación y geografía.  
- **Customer_DF** → Enfocado en fraude por contacto/dispositivo, muy útil en ciberseguridad.  

Este ecosistema de bases de datos brinda un **pipeline completo de BI**, cubriendo **transacciones, clientes y riesgo** desde múltiples fuentes.

---

## 🚀 Tecnologías utilizadas
- **PostgreSQL + Docker** → Almacenamiento relacional.  
- **Python (pandas, SQLAlchemy)** → Procesamiento de datos.  
- **Jupyter / DataSpell** → Exploración y documentación.  
- **Kaggle + datasets académicos** → Fuentes de datos abiertas.
