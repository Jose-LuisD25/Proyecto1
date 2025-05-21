import streamlit as st
import random

st.set_page_config(page_title="Aprende Python - While, For, If", page_icon="🐍")

st.title("🐍 Aprende Python: Bucles y Condicionales")

st.markdown("""
En esta página aprenderás sobre tres bloques fundamentales de programación en Python:

### 🔁 Bucle `while`
Ejecuta un bloque de código mientras una condición sea verdadera.

```python
i = 0
while i < 5:
    print(i)
    i += 1
    for i in range(5):
    print(i)
x = 10
if x > 5:
    print("Mayor que 5")
elif x == 5:
    print("Es 5")
else:
    print("Menor que 5")
