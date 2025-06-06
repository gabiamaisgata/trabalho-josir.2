import streamlit as st

import random

st.set_page_config(page_title="Recomendador de Looks", page_icon="👗")

st.title("👗 Recomendador de Looks Personalizado")

st.markdown("Responda algumas perguntas e receba uma sugestão de look com sua cara!")

# PERGUNTAS ✨

ocasião = st.selectbox("1️⃣ Qual a ocasião?", [

    "Faculdade", "Escola", "Shopping", "Date", "Praia",

    "Festa / Balada", "Piquenique", "Museu", "Brunch",

    "Churrasco", "Cinema", "Teatro"

])

estilo = st.selectbox("2️⃣ Qual estilo você prefere?", [

    "Básico", "Fashionista", "Esportivo", "Romântico", "Despojado"

])

clima = st.selectbox("3️⃣ Como está o clima hoje?", [

    "Calor", "Frio", "Ameno", "Chuvoso"

])

humor = st.selectbox("4️⃣ Como você está se sentindo hoje?", [

    "Confiante", "Na dúvida", "Preguiçosa", "Quieta e estilosa", "Pronta pra brilhar"

])

tempo_fora = st.radio("5️⃣ Vai passar quanto tempo fora de casa?", [

    "O dia inteiro", "Só algumas horinhas", "Não sei ainda"

])

locomocao = st.selectbox("6️⃣ Vai como?", [

    "A pé", "Transporte público", "De carro", "Moto"

])

calçado = st.radio("7️⃣ Tem preferência de calçado?", [

    "Tênis", "Sandália", "Salto", "Bota", "Tanto faz"

])

vibe_cor = st.radio("8️⃣ Prefere algo mais colorido ou neutro?", [

    "Coloridão", "Tons pastéis", "Neutro e elegante", "Preto sempre"

])

acessorios = st.radio("9️⃣ Curte usar acessórios?", [

    "Sim, amo!", "Apenas alguns", "Prefiro evitar"

])

# SUGESTÕES DE ACESSÓRIOS 🎀

acessorios_por_estilo = {

    "Básico": ["argolas pequenas", "relógio simples", "bolsa transversal"],

    "Fashionista": ["óculos escuros estilosos", "brincos grandes", "cinto marcante"],

    "Esportivo": ["boné", "mochilinha", "meia alta estilizada"],

    "Romântico": ["tiara ou presilha", "colar delicado", "bolsa de palha"],

    "Despojado": ["pulseira de miçanga", "anel colorido", "bucket hat"]

}

# PALETA DE CORES 🌈

paletas = {

    "Calor": "https://i.pinimg.com/564x/67/ff/4a/67ff4a35439c31ea2ab53d5eb7e5a0ae.jpg",

    "Frio": "https://i.pinimg.com/564x/94/49/ba/9449ba7bcb305108de7bde1e43ff635e.jpg",

    "Ameno": "https://i.pinimg.com/564x/cf/99/41/cf99411b1e4f1b8a456cbbed3dbdc7c7.jpg",

    "Chuvoso": "https://i.pinimg.com/564x/79/23/95/792395b59bc25295a2798029e14f2cb1.jpg"

}

# LOOKS 🎽

looks = {

    "Faculdade": ["Calça jeans + camiseta básica + tênis", "Vestido confortável + jaqueta jeans"],

    "Escola": ["Calça de moletom + blusa larga + tênis", "Short + camiseta + mochila"],

    "Shopping": ["Saia jeans + blusa estilosa + sandália", "Calça cargo + cropped + tênis estiloso"],

    "Date": ["Vestido midi + salto baixo", "Calça de alfaiataria + top + jaqueta de couro"],

    "Praia": ["Saída de praia + biquíni + chinelo", "Short leve + regata + chapéu"],

    "Festa / Balada": ["Vestido colado + salto alto", "Top de brilho + saia + bota"],

    "Piquenique": ["Vestido floral + tênis", "Jardineira + blusa leve"],

    "Museu": ["Calça pantalona + regata + sandália", "Saia midi + camisa"],

    "Brunch": ["Blusa romântica + saia rodada + sapatilha", "Macacão + sandália confortável"],

    "Churrasco": ["Short jeans + cropped + rasteirinha", "Vestido soltinho + tênis"],

    "Cinema": ["Calça jeans + blusa quentinha + tênis", "Moletom + legging + tênis"],

    "Teatro": ["Blazer + vestido + sapato fechado", "Macacão + salto"]

}
