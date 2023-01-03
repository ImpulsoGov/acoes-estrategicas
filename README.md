<!--
SPDX-FileCopyrightText: 2021, 2022 ImpulsoGov <contato@impulsogov.org>

SPDX-License-Identifier: MIT
-->
![Badge em Produção](https://img.shields.io/badge/status-em%20produ%C3%A7%C3%A3o-green)

# Ações Estratégicas
Aplicação em streamlit que serve de suporte ao projeto [Impulso Previne](https://github.com/ImpulsoGov/ImpulsoPrevine), permitindo gestores públicos de saúde simular a partir de quais caracteristicas quais ações estratégicas podem aderir.

*******
## :mag_right: Índice
1. [Rodando em produção](#rodando)
2. [Instruções para instalação e acesso ao projeto](#instalacao)
3. [Contribua](#contribua)
4. [Licença](#licenca)
*******

 <div id='rodando'/> 
 
## :gear: Rodando em produção

A nossa aplicação está hospedada no [heroku](https://acoesestrategicas.herokuapp.com/) e está embedada na nossa aplicação, [Impulso Previne](https://www.impulsoprevine.org/).


*******

<div id='instalacao'/> 

 ## 🛠️ Instruções para instalação e acesso ao projeto
 
 ```bash
 # Para criar uma env
pip install virtualenv
virtualenv nome_da_virtualenv
# Para ativar a env (Windows)
cd nome_da_virtualenv\Scripts\activate
# Para ativar a env (Linux)
source nome_da_virtualenv/bin/activate
```

```bash
# Instala requerimentos
pip install -r requirements.txt
```


```bash
# Roda a aplicação
streamlit run app.py
```

*******

<div id='contribua'/>  

## :left_speech_bubble: Contribua
Sinta-se à vontade para contribuir em nosso projeto! Abra uma issue ou envie PRs.

*******
<div id='licenca'/>  

## :registered: Licença
MIT (c) 2020, 2022 Impulso Gov <contato@impulsogov.org>
