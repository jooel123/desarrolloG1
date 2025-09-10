Proyecto BI – Counterfeit Product Detection


📊 1. DataFrame de Transacciones (df_transacciones)
Descripción
Contiene cada operación registrada en el dataset. Es la fuente base para análisis financiero y de riesgo.

Columna	Tipo de Dato	Descripción	Restricciones
transaction_id	VARCHAR(50)	Identificador único de la transacción	PRIMARY KEY
transaction_date	DATE	Fecha de la operación	NOT NULL
customer_id	VARCHAR(50)	Cliente asociado	NOT NULL
quantity	INTEGER	Cantidad comprada	CHECK (> 0)
unit_price	DECIMAL(10,2)	Precio unitario	CHECK (> 0)
total_amount	DECIMAL(12,2)	Monto total	CHECK (>= 0)
payment_method	VARCHAR(20)	Forma de pago	NOT NULL
shipping_speed	VARCHAR(15)	Velocidad de envío	NOT NULL
discount_applied	BOOLEAN	Indicador de descuento aplicado	DEFAULT FALSE
discount_percentage	DECIMAL(5,2)	Porcentaje de descuento	CHECK (>= 0 AND <= 100)
refund_requested	BOOLEAN	Solicitud de reembolso	DEFAULT FALSE
velocity_flag	BOOLEAN	Bandera de velocidad (fraude)	DEFAULT FALSE
geolocation_mismatch	BOOLEAN	Bandera de geolocalización	DEFAULT FALSE
Filtros aplicados

Transacciones de alto valor → top 10% de total_amount

Transacciones con banderas de riesgo → velocity_flag = TRUE OR geolocation_mismatch = TRUE OR refund_requested = TRUE

Transacciones con descuentos altos → discount_percentage >= 30%

👤 2. DataFrame de Clientes (df_clientes)
Descripción
Agrupa métricas a nivel de cliente para segmentación de usuarios.

Columna	Tipo de Dato	Descripción	Restricciones
customer_id	VARCHAR(50)	Identificador único del cliente	PRIMARY KEY
total_pedidos	INTEGER	Número de compras realizadas	DEFAULT 0
monto_total	DECIMAL(12,2)	Valor total acumulado	DEFAULT 0.00
ticket_promedio	DECIMAL(10,2)	Valor promedio de compra	DEFAULT 0.00
tasa_reembolso	DECIMAL(5,2)	Proporción de pedidos con devolución	DEFAULT 0.00
flags_riesgo	INTEGER	Número de alertas de fraude asociadas	DEFAULT 0
customer_location	VARCHAR(100)	Ubicación más frecuente del cliente	NOT NULL
customer_segment	VARCHAR(20)	Segmento del cliente	DEFAULT 'Standard'
Filtros aplicados

Clientes VIP → top 10% en monto_total

Clientes riesgosos → tasa_reembolso >= 30 OR flags_riesgo > 0

Clientes frecuentes → total_pedidos >= 5

🚚 3. DataFrame de Logística (df_logistica)
Descripción
Evalúa desempeño logístico y cumplimiento de SLA (tiempo objetivo de entrega).

Columna	Tipo de Dato	Descripción	Restricciones
shipping_id	SERIAL	ID único del envío	PRIMARY KEY
transaction_id	VARCHAR(50)	ID de la transacción asociada	FOREIGN KEY
shipping_speed	VARCHAR(15)	Modalidad de envío	NOT NULL
delivery_time_days	INTEGER	Tiempo real de entrega (días)	CHECK (> 0)
shipping_cost	DECIMAL(8,2)	Costo del envío	CHECK (>= 0)
sla_dias	INTEGER	SLA asignado según modalidad	CHECK (> 0)
cumple_sla	BOOLEAN	Indicador de cumplimiento del SLA	DEFAULT FALSE
region	VARCHAR(50)	Región de destino	NOT NULL
Filtros aplicados

Envíos fuera de SLA → cumple_sla = FALSE

Envíos costosos → top 10% en shipping_cost

Envíos lentos → delivery_time_days >= 10

✅ Conclusiones del Análisis
El equipo de estudiantes logró establecer que:

Transacciones: Permiten identificar operaciones sospechosas (fraude, alto valor, devoluciones)

Clientes: Se segmentan efectivamente en VIP, frecuentes y riesgosos

Logística: Se mide eficientemente la eficiencia, costos y cumplimiento de SLA

Este esquema de 3 DataFrames + filtros habilita un pipeline de Inteligencia de Negocios útil para detección de fraude, análisis de clientes estratégicos y optimización logística.

🚀 Tecnologías Utilizadas
Tecnología	Versión	Uso en el Proyecto
PostgreSQL	15+	Base de datos principal
Docker	20.10+	Contenerización de la BD
Python	3.10+	Procesamiento de datos
pandas	2.0+	Manipulación de datos
SQLAlchemy	2.0+	ORM para PostgreSQL
Jupyter Notebooks	6.5+	Entorno de análisis