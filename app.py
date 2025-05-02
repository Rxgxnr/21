import streamlit as st

# Inicializa el estado de las cartas
if 'cartas_jugador' not in st.session_state:
    st.session_state.cartas_jugador = []
if 'cartas_dealer' not in st.session_state:
    st.session_state.cartas_dealer = []

# Función para calcular el tipo de mano y total
def tipo_mano_y_total(cartas):
    valores = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}
    total = 0
    ases = 0
    for c in cartas:
        if c == 'A':
            ases += 1
        total += valores.get(c, 0)
    while total > 21 and ases > 0:
        total -= 10
        ases -= 1

    if len(cartas) == 2 and cartas[0] == cartas[1]:
        tipo = "par"
    elif 'A' in cartas and total < 21:
        tipo = "blanda"
    else:
        tipo = "dura"

    return tipo, total

# Estrategia para manos duras (simplificada)
def estrategia_dura(total, dealer_carta):
    dealer_valor = 11 if dealer_carta == 'A' else 10 if dealer_carta in ['K','Q','J'] else int(dealer_carta)

    if total <= 8:
        return "Pedir"
    elif total == 9:
        return "Doblar" if 3 <= dealer_valor <= 6 else "Pedir"
    elif total == 10:
        return "Doblar" if dealer_valor <= 9 else "Pedir"
    elif total == 11:
        return "Doblar"
    elif total == 12:
        return "Quedarse" if 4 <= dealer_valor <= 6 else "Pedir"
    elif 13 <= total <= 16:
        return "Quedarse" if 2 <= dealer_valor <= 6 else "Pedir"
    else:
        return "Quedarse"

# INTERFAZ
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

# Selectores de acción manual
st.subheader("⚙️ Acciones")
col3, col4 = st.columns(2)
with col3:
    accion_jugador = st.selectbox("Acción del Jugador", ["-", "Pedir", "Quedarse", "Doblar"])
with col4:
    accion_dealer = st.selectbox("Acción del Dealer", ["-", "Pedir", "Quedarse", "Doblar"])

# Recomendación automática
st.markdown("---")
accion = "-"
tipo, total = tipo_mano_y_total(st.session_state.cartas_jugador)
dealer_up = st.session_state.cartas_dealer[0] if st.session_state.cartas_dealer else None

if dealer_up:
    if tipo == "dura":
        accion = estrategia_dura(total, dealer_up)
    else:
        accion = "No implementado aún para manos " + tipo

st.markdown(f"🧠 **Tipo de mano:** {tipo.capitalize()} | **Total:** {total}")
st.markdown(f"🎯 **Carta visible del Dealer:** {dealer_up}")
st.markdown(f"📣 **Recomendación automática:** `{accion}`")

# Botón para reiniciar la partida
if st.button("🔄 Reiniciar"):
    st.session_state.cartas_jugador = []
    st.session_state.cartas_dealer = []
