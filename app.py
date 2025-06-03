import streamlit as st

st.title("⚡ Asistente Rápido de Blackjack Hola Camilo")

st.markdown("Ingresa el total de tu mano y la carta visible del dealer para obtener una recomendación automática.")

# Entrada rápida
total_jugador = st.number_input("🧮 Total de tu mano", min_value=4, max_value=21, step=1)
dealer_up = st.text_input("🃏 Carta del Dealer (ej: 2, 10, A)").upper()

# Estrategia básica para manos duras
def estrategia_dura(total, dealer_carta):
    try:
        dealer_valor = 11 if dealer_carta == 'A' else 10 if dealer_carta in ['K','Q','J'] else int(dealer_carta)
    except:
        return "⚠️ Carta del dealer no válida"

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

# Mostrar recomendación solo si ambos valores están presentes
if total_jugador and dealer_up:
    recomendacion = estrategia_dura(total_jugador, dealer_up)
    st.markdown("---")
    st.markdown(f"🧠 **Recomendación:** `{recomendacion}`")
