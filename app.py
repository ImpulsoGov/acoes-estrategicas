import streamlit as st
import pandas as pd
import numpy as np

st.title('Caracterização do município')
st.write("Clique nas características abaixo e veja quais ações estratégicas, possivelmente, há elegibilidade no seu município.")

acoes = []

if st.checkbox('Municípios com população vivendo em comunidades ribeirinhas'):
    acoes.extend(['Informatiza APS','Programa Saúde na Escola (PSE)','Estratégia de Agentes Comunitários de Saúde (ACS)','Unidade Básica de Saúde Fluvial (UBSF)','Equipes de Saúde da Família Ribeirinha (eSFR)','Micropista']) 
if st.checkbox('Até duas equipes, sem profissionais adicionais (além da equipe mínima), sem especificidadese e sem cirurgião dentista.'):
    acoes.extend(['Informatiza APS','Programa Saúde na Escola (PSE)','Estratégia de Agentes Comunitários de Saúde (ACS)']) 
if st.checkbox('Duas ou mais equipes, com profissionais adicionais (além da equpe mínima), sem especificidades'):
    acoes.extend(['Informatiza APS','Programa Saúde na Escola (PSE)','Estratégia de Agentes Comunitários de Saúde (ACS)','Equipes de Saúde Bucal','Unidade Odontológica Móvel (UOM)','Laboratório Regional de Prótese Dentária (LRPD)','Programa Academia da Saúde','Equipe de Consultório na Rua (eCR)'])
if st.checkbox('Duas ou mais equipes, com profissionais adicionais (além da equpe mínima), com especfificidades (sistema prisional adulto e jovem)'):
    acoes.extend(['Informatiza APS','Programa Saúde na Escola (PSE)','Estratégia de Agentes Comunitários de Saúde (ACS)','Equipes de Saúde Bucal','Unidade Odontológica Móvel (UOM)','Laboratório Regional de Prótese Dentária (LRPD)','Programa Academia da Saúde','Equipe de Consultório na Rua (eCR)', 'Centro de Especialidades Odontológicas (CEO)'])
if st.checkbox('Duas ou mais equipes, com profissionais adicionais (além da equpe mínima), com especfificidades (sistema prisional adulto e jovem) e com profissionais residentes nas equipes'):
    acoes.extend(['Formação Profissional','Informatiza APS','Programa Saúde na Escola (PSE)','Estratégia de Agentes Comunitários de Saúde (ACS)','Equipes de Saúde Bucal','Unidade Odontológica Móvel (UOM)','Laboratório Regional de Prótese Dentária (LRPD)','Programa Academia da Saúde','Equipe de Consultório na Rua (eCR)', 'Centro de Especialidades Odontológicas (CEO)', 'Equipe de Atenção Básica Prisional (eABP)'])
if st.checkbox('Duas ou mais equipes, com profissionais adicionais (além da equpe mínima), possibilidade de equipes com funcionamento de pelo menos 60h semanais, sem especificades'):
    acoes.extend(['Informatiza APS','Programa Saúde na Hora','Programa Saúde na Escola (PSE)','Estratégia de Agentes Comunitários de Saúde (ACS)','Equipes de Saúde Bucal','Unidade Odontológica Móvel (UOM)','Laboratório Regional de Prótese Dentária (LRPD)','Programa Academia da Saúde','Equipe de Consultório na Rua (eCR)', 'Centro de Especialidades Odontológicas (CEO)'])
if st.checkbox('Duas ou mais equipes, com profissionais adicionais (além da equpe mínima), possibilidade de equipes com funcionamento de pelo menos 60h semanais com especificades (sistema prisional adulto e jovem)'):
    acoes.extend(['Informatiza APS','Programa Saúde na Hora','Programa Saúde na Escola (PSE)','Estratégia de Agentes Comunitários de Saúde (ACS)','Equipes de Saúde Bucal','Unidade Odontológica Móvel (UOM)','Laboratório Regional de Prótese Dentária (LRPD)','Programa Academia da Saúde','Equipe de Consultório na Rua (eCR)', 'Centro de Especialidades Odontológicas (CEO)', 'Equipe de Atenção Básica Prisional (eABP)'])
if st.checkbox('Duas ou mais equipes, com profissionais adicionais (além da equpe mínima), possibilidade de equipes com funcionamento de pelo menos 60h semanais com especificades e com profissionais residentes nas equipes'):
    acoes.extend(['Formação Profissional','Programa Saúde na Hora','Informatiza APS','Residência Profissional','Equipes de Saúde Bucal','Unidade Odontológica Móvel (UOM)','Centro de Especialidades Odontológicas (CEO)','Laboratório Regional de Prótese Dentária (LRPD)','Programa Saúde na Escola (PSE)','Programa Academia da Saúde','Equipe de Consultório na Rua (eCR)','Equipe de Atenção Básica Prisional (eABP)','Estratégia de Agentes Comunitários de Saúde (ACS)','Atenção Integral à Saúde dos Adolescentes em Situação de Privação de Liberdade'])

tabela_acoes = pd.read_csv("acoes.csv")




if st.button('Ver ações'):
    tabela_acoes = tabela_acoes[tabela_acoes['Ação Estratégica'].isin(np.unique(acoes))]
    # st.dataframe(tabela_acoes)

    col = tabela_acoes.columns
    st.markdown("""<table>
        <tr>
            <th style="width:12px">{}</th>
            <th style="width:123px">{}</th>
            <th style="width:90px">{}</th>
            <th style="width:185px">{}</th>
            <th style="width:185px">{}</th>
        </tr>""".format(col[0], col[1], col[2], col[3], col[4]), unsafe_allow_html=True)
    for i in tabela_acoes.index:
        linha = tabela_acoes.loc[i]
        st.markdown("""
                <tr>
                    <td style="height:200px; width:125px">{}</td>
                    <td style="height:200px; width:125px">{}</td>
                    <td style="height:200px; width:90px">{}</td>
                    <td style="height:200px; width:185px">{}</td>
                    <td style="height:200px; width:185px">{}</td>
                </tr>""".format(linha[0], linha[1], linha[2], linha[3], linha[4]), unsafe_allow_html=True)
    st.markdown("""</table>""", unsafe_allow_html=True)
