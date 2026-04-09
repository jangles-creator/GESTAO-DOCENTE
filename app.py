import streamlit as st

st.set_page_config(layout="wide")

# Título
st.markdown("<h1 style='text-align: center;'>SENAI HUB</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>GESTÃO EDUCACIONAL</h2>", unsafe_allow_html=True)

# Layout em 3 colunas
col1, col2, col3 = st.columns(3)

# ===== COLUNA 1 =====
with col1:
    st.subheader("Gestão de Turmas")

    with st.expander("📁 APRENDIZAGEM", expanded=False):
        st.link_button("Programa de Edificações (2025-2026)", "#")
        st.link_button("Gestão Industrial 1 - Manhã", "#")
        st.link_button("Gestão Industrial 2 - Manhã", "#")
        st.link_button("Gestão Industrial 3 - Manhã", "#")
        st.link_button("Gestão Industrial 4 - Manhã", "#")
        st.link_button("Gestão Industrial 5 - Tarde", "#")
        st.link_button("Gestão Industrial 6 - Tarde", "#")

# ===== COLUNA 2 =====
with col2:
    st.subheader("Cronogramas")

    with st.expander("📁 TRILHAS NEM 2026", expanded=False):
        st.link_button("Logística A - Manhã (1º ANO)", "#")
        st.link_button("Logística B - Manhã (1º ANO)", "#")
        st.link_button("Logística C - Manhã (1º ANO)", "#")
        st.link_button("Logística D - Tarde (1º ANO)", "#")
        st.link_button("Logística E - Tarde (1º ANO)", "#")

# ===== COLUNA 3 =====
with col3:
    st.subheader("Coordenação Pedagógica")

    with st.expander("📁 TRILHAS NEM 2025-2026", expanded=False):
        st.link_button("Renováveis - Manhã (3º ANO)", "#")
        st.link_button("Logística 1 - Manhã (2º ANO)", "#")
        st.link_button("Logística 2 - Tarde (2º ANO)", "#")
        st.link_button("Logística 3 - Manhã (3º ANO)", "#")