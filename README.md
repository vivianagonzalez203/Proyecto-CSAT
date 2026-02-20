# 📊Modelo Predictivo de Satisfacción de Clientes (CSAT)

Proyecto de analítica de datos enfocado en la predicción de satisfacción de clientes mediante técnicas de Machine Learning y visualización interactiva.

El objetivo es transformar datos históricos en información accionable que apoye la toma de decisiones estratégicas.

## 🔗 Aplicación en producción:
👉 https://csat-proyecto-vivianagonzalez.streamlit.app/

## 🎯 Objetivo del Proyecto

- Desarrollar un modelo capaz de identificar clientes con riesgo de insatisfacción, permitiendo:
- Anticipar posibles abandonos o quejas
- Priorizar acciones correctivas
- Optimizar recursos
- Tomar decisiones basadas en datos
- El enfoque no se limita a maximizar métricas técnicas, sino a generar impacto en negocio.

## 🧠 Metodología

El proyecto sigue el flujo completo de un proceso de analítica:

- Exploración y limpieza de datos
- Análisis exploratorio (EDA)
- Feature Engineering
- Tratamiento de desbalance de clases mediante SMOTE

### Entrenamiento de modelo (Random Forest)

- Optimización de hiperparámetros
- Evaluación con métricas robustas
- Ajuste de umbral personalizado
- Despliegue en aplicación interactiva con Streamlit

## ⚖️ Tratamiento del Desbalance

Dado que el conjunto de datos presenta desbalance entre clientes satisfechos e insatisfechos:

- Se aplicó SMOTE para mejorar la representación de la clase minoritaria.
- Se priorizó la evaluación mediante Curva ROC y AUC.
- Se ajustó el umbral de decisión para optimizar sensibilidad según el objetivo de negocio.
- Esto permitió evaluar el modelo más allá del accuracy tradicional.

## 📈 Evaluación del Modelo

### La evaluación incluyó:

- Curva ROC
- AUC
- Matriz de confusión
- Análisis de sensibilidad y especificidad
- Ajuste de threshold (umbral personalizado)
- El objetivo fue maximizar la capacidad de discriminación del modelo y alinearlo con decisiones reales.

## 🖥️ Aplicación Interactiva

El modelo fue desplegado en una aplicación desarrollada con Streamlit que permite:

- Ingresar variables del cliente
- Obtener la probabilidad de insatisfacción
- Visualizar resultados de forma clara e intuitiva

## 🔗 Accede aquí:
https://csat-proyecto-vivianagonzalez.streamlit.app/

## 🛠️ Tecnologías Utilizadas

- Python
- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Matplotlib / Seaborn

### Streamlit

#### 📂 Estructura del Proyecto
├── data/
├── notebooks/
├── models/
├── app.py
├── requirements.txt
└── README.md

## 🚀 Cómo Ejecutarlo Localmente

### Clonar el repositorio:
git clone https://github.com/vivianagonzalez203/Proyecto-CSAT.git
cd Proyecto-CSAT

### Instalar dependencias:

pip install -r requirements.txt

### Ejecutar la aplicación:

streamlit run app.py

## 💡 Principales Aprendizajes

- Evaluar modelos en contextos desbalanceados requiere métricas adecuadas.
- Ajustar el umbral puede ser más estratégico que mejorar el accuracy.
- El despliegue a producción implica retos distintos al entrenamiento.
- La visualización facilita la interpretación y adopción del modelo.

## 👩‍💻 Autor:

Viviana Gonzalez
Proyecto desarrollado como parte de mi portafolio en analítica de datos y machine learning.
