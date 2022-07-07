import streamlit as st

st.title('Caracterização do município')
st.write("Clique nas características abaixo e veja quais ações estratégicas, possivelmente, há elegibilidade no seu município.")

agree = st.checkbox('Municípios com população vivendo em comunidades ribeirinhas')
agree = st.checkbox('Até duas equipes, sem profissionais adicionais (além da equipe mínima), sem especificidadese e sem cirurgião dentista.')
agree = st.checkbox('Duas ou mais equipes, com profissionais adicionais (além da equpe mínima), sem especificidades')
agree = st.checkbox('Duas ou mais equipes, com profissionais adicionais (além da equpe mínima), com especfificidades (sistema prisional adulto e jovem)')
agree = st.checkbox('Duas ou mais equipes, com profissionais adicionais (além da equpe mínima), com especfificidades (sistema prisional adulto e jovem) e com profissionais residentes nas equipes')
agree = st.checkbox('Duas ou mais equipes, com profissionais adicionais (além da equpe mínima), possibilidade de equipes com funcionamento de pelo menos 60h semanais, sem especificades')
agree = st.checkbox('Duas ou mais equipes, com profissionais adicionais (além da equpe mínima), possibilidade de equipes com funcionamento de pelo menos 60h semanais com especificades (sistema prisional adulto e jovem)')
agree = st.checkbox('Duas ou mais equipes, com profissionais adicionais (além da equpe mínima), possibilidade de equipes com funcionamento de pelo menos 60h semanais com especificades e com profissionais residentes nas equipes')

st.button('Ver ações')