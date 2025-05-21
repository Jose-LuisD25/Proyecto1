import streamlit as st

st.set_page_config(page_title="Aprende Python", page_icon="🐍", layout="centered")

# Título principal
st.title("🐍 Aprende Python - Control de flujo")
st.markdown("---")

# Sección informativa
with st.expander("📘 ¿Cómo funcionan while, for e if en Python?"):
    st.markdown("""
    ### 🔁 Bucle `while`
    El bucle `while` repite un bloque de código **mientras** se cumpla una condición.
    
    ```python
    x = 0
    while x < 5:
        print(x)
        x += 1
    ```

    ### 🔁 Bucle `for`
    El bucle `for` itera sobre una secuencia (como una lista o rango).
    
    ```python
    for i in range(5):
        print(i)
    ```

    ### 🔀 Condicional `if`
    El condicional `if` ejecuta un bloque de código si se cumple una condición.
    
    ```python
    edad = 18
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
    ```
    """)

# Lista de preguntas
preguntas = [
    {
        "pregunta": "¿Cuál es la función principal de un bucle `while`?",
        "opciones": ["Ejecutar código una sola vez", "Ejecutar código mientras se cumpla una condición", "Detener el programa"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Qué hace este código?\n\n```python\nfor i in range(3):\n    print(i)\n```",
        "opciones": ["Imprime 0, 1, 2", "Imprime 1, 2, 3", "Imprime 0, 1, 2, 3"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué palabra clave se usa para tomar una decisión en Python?",
        "opciones": ["if", "do", "loop"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué hace `x += 1`?",
        "opciones": ["Resta 1 a x", "Suma 1 a x", "Multiplica x por 1"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Cuál es la salida de este código?\n\n```python\nx = 2\nif x > 3:\n    print('Alto')\nelse:\n    print('Bajo')\n```",
        "opciones": ["Alto", "Bajo", "Nada"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Cuál es el valor final de x?\n\n```python\nx = 0\nwhile x < 3:\n    x += 1\n```",
        "opciones": ["0", "3", "4"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Cuál es la función de `range(5)`?",
        "opciones": ["Generar 5 números aleatorios", "Crear una lista del 0 al 5", "Crear una secuencia de 0 a 4"],
        "respuesta_correcta": 2
    },
    {
        "pregunta": "¿Qué estructura usarías para repetir código 10 veces?",
        "opciones": ["if", "for", "break"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Cómo se detiene un bucle antes de que termine normalmente?",
        "opciones": ["continue", "stop", "break"],
        "respuesta_correcta": 2
    },
    {
        "pregunta": "¿Qué imprime esto?\n\n```python\nfor i in range(2):\n    print('Hola')\n```",
        "opciones": ["Nada", "Hola una vez", "Hola dos veces"],
        "respuesta_correcta": 2
    },
]

st.subheader("📝 Test de 10 preguntas")
respuestas_usuario = []

# Mostrar preguntas y alternativas
for i, pregunta in enumerate(preguntas):
    st.markdown(f"**{i+1}. {pregunta['pregunta']}**")
    opcion = st.radio(
        label="Selecciona una opción:",
        options=pregunta["opciones"],
        key=f"pregunta_{i}"
    )
    respuestas_usuario.append(opcion)

# Botón para verificar respuestas
if st.button("✅ Verificar puntaje"):
    puntaje = 0
    for i, pregunta in enumerate(preguntas):
        if respuestas_usuario[i] == pregunta["opciones"][pregunta["respuesta_correcta"]]:
            puntaje += 1

    st.markdown(f"### 🎯 Tu puntaje: **{puntaje} / {len(preguntas)}**")

    if puntaje == len(preguntas):
        st.balloons()
        st.success("¡Felicidades! Has respondido todo correctamente 🎉")
    elif puntaje >= 7:
        st.success("¡Muy bien! Tienes una buena comprensión.")
    else:
        st.warning("Puedes repasar los conceptos y volver a intentarlo.")
