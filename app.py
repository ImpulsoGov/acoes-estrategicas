import streamlit as st
import pandas as pd
import numpy as np

st.title('Caracterização do município')
st.write("Clique nas características abaixo e veja quais ações estratégicas, possivelmente, há elegibilidade no seu município.")

acoes = []

if st.checkbox('Municípios com população vivendo em comunidades ribeirinhas'):
    acoes.extend(['Informatiza APS','Programa Saúde na Escola (PSE)','Agente Comunitário de Saúde','Unidade Básica de Saúde Fluvial (UBSF)','Equipes de Saúde da Família Ribeirinha (eSFR)','Micropista']) 
if st.checkbox('Até duas equipes, sem profissionais adicionais (além da equipe mínima), sem especificidadese e sem cirurgião dentista.'):
    acoes.extend(['Informatiza APS','Programa Saúde na Escola (PSE)','Agente Comunitário de Saúde']) 
if st.checkbox('Duas ou mais equipes, com profissionais adicionais (além da equpe mínima), sem especificidades'):
    acoes.extend(['Informatiza APS','Programa Saúde na Escola (PSE)','Agente Comunitário de Saúde','Equipes de Saúde Bucal','Unidade Odontológica Móvel','Laboratório Regional de Prótese Dentária (LRPD)','Programa Academia da Saúde','Equipes de Consultório na Rua'])
if st.checkbox('Duas ou mais equipes, com profissionais adicionais (além da equpe mínima), com especfificidades (sistema prisional adulto e jovem)'):
    acoes.extend(['Informatiza APS','Programa Saúde na Escola (PSE)','Agente Comunitário de Saúde','Equipes de Saúde Bucal','Unidade Odontológica Móvel','Laboratório Regional de Prótese Dentária (LRPD)','Programa Academia da Saúde','Equipes de Consultório na Rua', 'Centro de Especialidades Odontológicas'])
if st.checkbox('Duas ou mais equipes, com profissionais adicionais (além da equpe mínima), com especfificidades (sistema prisional adulto e jovem) e com profissionais residentes nas equipes'):
    acoes.extend(['Formação Profissional','Informatiza APS','Programa Saúde na Escola (PSE)','Agente Comunitário de Saúde','Equipes de Saúde Bucal','Unidade Odontológica Móvel','Laboratório Regional de Prótese Dentária (LRPD)','Programa Academia da Saúde','Equipes de Consultório na Rua', 'Centro de Especialidades Odontológicas', 'Equipe de Atenção Básica Prisional (eABP)'])
if st.checkbox('Duas ou mais equipes, com profissionais adicionais (além da equpe mínima), possibilidade de equipes com funcionamento de pelo menos 60h semanais, sem especificades'):
    acoes.extend(['Informatiza APS','Programa Saúde na Hora','Programa Saúde na Escola (PSE)','Agente Comunitário de Saúde','Equipes de Saúde Bucal','Unidade Odontológica Móvel','Laboratório Regional de Prótese Dentária (LRPD)','Programa Academia da Saúde','Equipes de Consultório na Rua', 'Centro de Especialidades Odontológicas'])
if st.checkbox('Duas ou mais equipes, com profissionais adicionais (além da equpe mínima), possibilidade de equipes com funcionamento de pelo menos 60h semanais com especificades (sistema prisional adulto e jovem)'):
    acoes.extend(['Informatiza APS','Programa Saúde na Hora','Programa Saúde na Escola (PSE)','Agente Comunitário de Saúde','Equipes de Saúde Bucal','Unidade Odontológica Móvel','Laboratório Regional de Prótese Dentária (LRPD)','Programa Academia da Saúde','Equipes de Consultório na Rua', 'Centro de Especialidades Odontológicas', 'Equipe de Atenção Básica Prisional (eABP)'])
if st.checkbox('Duas ou mais equipes, com profissionais adicionais (além da equpe mínima), possibilidade de equipes com funcionamento de pelo menos 60h semanais com especificades e com profissionais residentes nas equipes'):
    acoes.extend(['Formação Profissional','Programa Saúde na Hora','Informatiza APS','Residência Profissional','Equipes de Saúde Bucal','Unidade Odontológica Móvel','Centro de Especialidades Odontológicas','Laboratório Regional de Prótese Dentária (LRPD)','Programa Saúde na Escola (PSE)','Programa Academia da Saúde','Equipes de Consultório na Rua','Equipe de Atenção Básica Prisional (eABP)','Agente Comunitário de Saúde','Atenção Integral à Saúde dos Adolescentes em Situação de Privação de Liberdade'])

tabela_acoes = pd.read_csv("acoes.csv")

if st.button('Ver ações'):
    tabela_acoes = tabela_acoes[tabela_acoes['Ação Estratégica'].isin(np.unique(acoes))]
    df = pd.DataFrame(tabela_acoes)
    st.dataframe(df)