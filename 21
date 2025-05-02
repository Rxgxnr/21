import streamlit as st

# Mantener el estado entre ejecuciones
if 'cartas_jugador' not in st.session_state:
    st.session_state.cartas_jugador = []

if 'cartas_dealer' not in st.session_state:
    st.session_state.cartas_dealer = []

st.title("🤖 Asistente Blackjack en Tiempo Real")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🃏 Cartas Dealer")
    carta_dealer = st.text_input("Agregar carta al Dealer (ej: A, 10, J)", key="input_dealer")
    if st.button("➕ Agregar Carta Dealer"):
        if carta_dealer:
            st.session_state.cartas_dealer.append(carta_dealer.upper())
    st.write("Cartas:", st.session_state.cartas_dealer)

with col2:
    st.subheader("🎴 Cartas Jugador")
    carta_jugador = st.text_input("Agregar carta al Jugador (ej: A, 10, 7)", key="input_jugador")
    if st.button("➕ Agregar Carta Jugador"):
        if carta_jugador:
            st.session_state.cartas_jugador.append(carta_jugador.upper())
    st.write("Cartas:", st.session_state.cartas_jugador)

# Selectores de acción
st.subheader("⚙️ Acciones")
col3, col4 = st.columns(2)
with col3:
    accion_jugador = st.selectbox("Acción del Jugador", ["-", "Pedir", "Quedarse", "Doblar"])
with col4:
    accion_dealer = st.selectbox("Acción del Dealer", ["-", "Pedir", "Quedarse", "Doblar"])

st.markdown("---")
st.markdown(f"🧠 Acción jugador: **{accion_jugador}**")
st.markdown(f"🧠 Acción dealer: **{accion_dealer}**")
