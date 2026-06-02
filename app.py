import streamlit as st
import random

st.title("Simulation du paradoxe de Monty Hall")

st.write("""
Simuler le problème de Monty Hall et comparer :
- stratégie sans changer de porte
- stratégie en changeant de porte
""")

n = st.slider("Nombre de simulations", 100, 100000, 10000, step=100)

def simulation_monty_hall(n):
    gains_sans_changer = 0
    gains_en_changeant = 0

    for _ in range(n):
        porte_gagnante = random.randint(0, 2)
        choix_joueur = random.randint(0, 2)

        if choix_joueur == porte_gagnante:
            gains_sans_changer += 1
        else:
            gains_en_changeant += 1

    return gains_sans_changer, gains_en_changeant


if st.button("Lancer la simulation"):
    sans, change = simulation_monty_hall(n)

    st.subheader("Résultats")

    st.write(f"Sans changer : {sans/n:.3f}")
    st.write(f"En changeant : {change/n:.3f}")

    st.bar_chart({
        "Sans changer": [sans/n],
        "En changeant": [change/n]
    })
