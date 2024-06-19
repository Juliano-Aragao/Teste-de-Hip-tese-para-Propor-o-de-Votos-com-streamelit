import streamlit as st
import numpy as np
import scipy.stats as stats

def main():
    st.title("Teste de Hipótese para Proporção de Votos")

    st.header("Insira os Dados da Amostra")
    n = st.number_input("Tamanho da amostra (n)", min_value=1, value=1000)
    x = st.number_input("Número de votos para o candidato (x)", min_value=0, value=540)

    if st.button("Calcular"):
        p_hat = x / n  # proporção observada na amostra
        p0 = 0.50  # proporção sob a hipótese nula

        # Estatística de teste (z)
        z = (p_hat - p0) / np.sqrt((p0 * (1 - p0)) / n)

        # Valor-p
        p_value = 2 * (1 - stats.norm.cdf(abs(z)))

        # Nível de significância
        alpha = 0.05

        st.subheader("Resultados")
        st.write(f"Estatística de teste (z): {z:.4f}")
        st.write(f"Valor-p: {p_value:.4f}")

        if p_value < alpha:
            st.write("Rejeitamos a hipótese nula (H0).")
            st.write("Há evidências suficientes para afirmar que a proporção de votos para o candidato é diferente de 50%.")
        else:
            st.write("Não rejeitamos a hipótese nula (H0).")
            st.write("Não há evidências suficientes para afirmar que a proporção de votos para o candidato é diferente de 50%.")

if __name__ == "__main__":
    main()
