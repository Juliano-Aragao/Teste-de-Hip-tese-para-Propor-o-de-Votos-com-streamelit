# Teste-de-Hip-tese-para-Propor-o-de-Votos-com-streamelit

# Teste de Hipótese para Proporção de Votos

Este projeto implementa um aplicativo interativo em Streamlit para realizar um teste de hipótese sobre a proporção de votos em uma eleição.

## Descrição

O aplicativo permite que os usuários insiram o tamanho da amostra e o número de votos para um candidato específico. Ele então calcula a estatística de teste \(z\) e o valor-p, e determina se a hipótese nula pode ser rejeitada ou não com base em um nível de significância de 0,05.

## Tecnologias Utilizadas

- Python
- Streamlit
- NumPy
- SciPy

## Instalação

1. Clone este repositório para sua máquina local:
    ```sh
    git clone https://github.com/Juliano-Aragao/Teste-de-Hip-tese-para-Propor-o-de-Votos-com-streamelit.git
2. Navegue até o diretório do projeto:
    ```sh
    cd teste-hipotese-proporcao-votos
    ```
3. Crie um ambiente virtual (opcional, mas recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate  # Para Windows
    ```
4. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Execute o aplicativo Streamlit:
    ```sh
    streamlit run app.py
    ```
2. Insira o tamanho da amostra e o número de votos para o candidato nos campos fornecidos.
3. Clique no botão "Calcular" para visualizar os resultados do teste de hipótese.

## Exemplo de Código

```python
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
