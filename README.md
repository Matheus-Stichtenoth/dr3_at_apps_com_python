# REQUISITOS PARA EXECUTAR O APLICATIVO 'CENTRAL DO PÓS-JOGO'

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

## 🌐 Utilização Web
### Streamlit

Página Narração da Partida:
    > Preencher o ID da partida (Recomendado = 22912 (Final da CL 2019, Tottenham x Liverpool))
    > Selecionar o estilo da narração
    > Clicar em Analise
    💥 Bang!

Página Dúvidas Partida:
    > Digitar o ID da partida (Recomendado = 22912 (Final da CL 2019, Tottenham x Liverpool))
    > Digitar sua pergunta
    > Clicar em "Perguntar ao Agente"
    Obs: Essa aplicação utiliza o agente para responder, porém não retorna a resposta.
    Se observar os logs (quando verbose = 1 no AgentExecutor), ele identifica a resposta mas não consegue retornar ela no Streamlit. Não consegui solucionar esse ponto, mas foi a única falha que essa aplicação teve.

Página Comparativo Jogadores:
    > Página focada em comparar dois jogadores, sendo eles Lionel Messi e Cristiano Ronaldo, que se enfrentaram na final da Champions League de 2009.
    > Não tem inputs do usuário para utilizar

### API

✨ LLM
Para a summarização dos eventos e geração do estilo de narração, foi utilizado Gemini 1.5 Flash.
Para criar sua API, acesse: https://aistudio.google.com/prompts/new_chat

Para a criação do agent, foi utilizado GPT 3.5 Turbo, pois o Gemini não atendeu a capicidade necessária para execução. Não usamos o GPT 4o por conta de ter um alto custo na aplicação (~ $0.3 por execução)