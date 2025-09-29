# transmilenio-ai-routes
Sistema inteligente para el traslado de una locacion a otra a partir de reglas logicas
# 🚌 Sistema Inteligente de Rutas - TransMilenio Bogotá

## 📖 Descripción
Este proyecto implementa un **sistema inteligente basado en conocimiento** que utiliza:
- **Hechos**: estaciones y tiempos de viaje entre ellas.
- **Reglas**: penalización por transferencia de línea.
- **Motor de inferencia**: aplica reglas para calcular el costo real.
- **Búsqueda heurística (A*)**: encuentra la mejor ruta entre dos estaciones.

El caso de estudio se centra en la localidad **Madelena (Bogotá Sur)** y su conexión con diferentes puntos de la red de TransMilenio.

---

## ⚙️ Requisitos
- Python 3.8 o superior  
- Instalar dependencias:
```bash
pip install -r requirements.txt
