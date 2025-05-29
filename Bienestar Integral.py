import streamlit as st

st.set_page_config(page_title="Agente de Autocuidado", page_icon="💖")

st.title("💆 Evaluación de Autocuidado")
st.write("Responde con sinceridad para conocer tu estado actual en diferentes aspectos de tu vida:")

estado_fisico = st.selectbox("¿Cómo te sientes físicamente?", ["Con mucha energía", "Normal", "Cansado/a", "Agotado/a"])
estado_mental = st.selectbox("¿Cómo está tu salud mental?", ["Positiva", "Estable", "Inestable", "Desmotivada"])
nivel_estres = st.slider("¿Qué tanto estrés has sentido últimamente? (1 = nada, 10 = muchísimo)", 1, 10, 5)
relaciones_sociales = st.selectbox("¿Cómo te llevas con las personas que te rodean?", ["Muy bien", "Bien", "Regular", "Mal"])
proyecto_vida = st.radio("¿Tienes claro tu propósito o rumbo de vida?", ["Sí, muy claro", "Más o menos", "No mucho", "Para nada"])
autocuidado = st.selectbox("¿Qué tanto te cuidas a ti mismo/a?", ["Muy bien", "Bien", "Poco", "Nada"])

if st.button("Ver mi evaluación"):
    st.subheader("📝 Tu resultado:")

    score = 0
    if estado_fisico == "Con mucha energía": score += 2
    elif estado_fisico == "Normal": score += 1

    if estado_mental == "Positiva": score += 2
    elif estado_mental == "Estable": score += 1

    if nivel_estres <= 3: score += 2
    elif nivel_estres <= 6: score += 1

    if relaciones_sociales == "Muy bien": score += 2
    elif relaciones_sociales == "Bien": score += 1

    if proyecto_vida == "Sí, muy claro": score += 2
    elif proyecto_vida == "Más o menos": score += 1

    if autocuidado == "Muy bien": score += 2
    elif autocuidado == "Bien": score += 1

    st.write("🔢 Puntos totales:", score, "/ 12")

    if score >= 10:
        st.success("¡Estás cuidándote muy bien! Sigue así, reina 💖")
    elif score >= 6:
        st.warning("Estás bien, pero podrías mejorar tu autocuidado 🧘‍♀️")
    else:
        st.error("Ojo 👀, necesitas darte más amor y tiempo. Busca ayuda si lo necesitas 💬")