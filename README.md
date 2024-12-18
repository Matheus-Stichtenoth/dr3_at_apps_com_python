# 'Central do Pós-Jogo!⚽'

## Requisitos Para Executar o Aplicativo

3️⃣◾1️⃣2️⃣◾5️⃣
```
Versão Python = 3.12.5
```

Outras versões podem funcionar também, mas o aplicativo foi construído sob esse versionamento.

🔧 Instalação
```
python -m pip install -r.\requirements.txt
```

Executar no powershell/cmd o código acima para fazer a instalação das bibliotecas necessárias para o funcionamento do código

⚙ Execução
```
streamlit run dashboard.py
```
Usar esse comando no powershell/cmd quando finalizar a configuração dos ambientes acima. Isso irá criar o streamlit local para você utilizar!

## 🌐 Utilização Web
### Streamlit

Página Narração da Partida:
    > Preencher o ID da partida (Recomendado = 22912 (Final da CL 2019, Tottenham x Liverpool)) <br/>
    > Selecionar o estilo da narração <br/>
    > Clicar em Analise <br/>
    💥 Bang! <br/>

Página Dúvidas Partida: <br/>
    > Digitar o ID da partida (Recomendado = 22912 (Final da CL 2019, Tottenham x Liverpool)) <br/>
    > Digitar sua pergunta <br/>
    > Clicar em "Perguntar ao Agente" <br/>
    Obs: Essa aplicação utiliza o agente para responder, porém não retorna a resposta. <br/>
    Se observar os logs (quando verbose = 1 no AgentExecutor), ele identifica a resposta mas não consegue retornar ela no Streamlit. Não consegui solucionar esse ponto, mas foi a única falha que essa aplicação teve. <br/>

Página Comparativo Jogadores: <br/>
    > Página focada em comparar dois jogadores, sendo eles Lionel Messi e Cristiano Ronaldo, que se enfrentaram na final da Champions League de 2009. <br/>
    > Não tem inputs do usuário para utilizar <br/>

Página Dashboard Campeonato/Partida: <br/>
    > ATENÇÃO, AGUARDE O CARD DE PASSES E DRIBLES FINALIZAR O CARREGAMENTO PARA UTILIZAR OS FILTROS NA PÁGINA <br/>
    > Selecione a competição desejada (Recomendo a Champions League) <br/>
    > Selecione a temporada desejada (Recomendo 2018-2019, final entre Tottenham e Liverpool) <br/>
    > Selecione a partida da competição <br/>
    > Ao final da página é possível fazer o download dos dados de dribles, passes e chutes na partida <br/>

### API

Método de utilização da API: POST

endpoints: 

```
/match_summary
/player_profile
```

```
uvicorn app.main:app --reload
```
O código acima é necessário para colocar a API em fucionamento

Para consumir os dados, acessar o Swagger da aplicação e preencher os IDs solicitados.

O retorno desses endpoints será um JSON

Ou, usar a biblioteca requests do Python para fazer a leitura dos dados

## ✨ LLM e Agent
Para a summarização dos eventos e geração do estilo de narração, foi utilizado Gemini 1.5 Flash.
Para criar sua API, acesse: https://aistudio.google.com/prompts/new_chat

Para a criação do agent, foi utilizado GPT 3.5 Turbo, pois o Gemini não atendeu a capicidade necessária para execução. Não usamos o GPT 4o por conta de ter um alto custo na aplicação (~ $0.3 por execução)