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

Página Narração:
    > Preencher o ID da partida (Recomendado = 22912 (Final da CL 2019, Tottenham x Liverpool))
    > Selecionar o estilo da narração
    > Clicar em Analise
    💥 Bang!

### API

✨ LLM
Para a summarização dos eventos e geração do estilo de narração, foi utilizado Gemini 1.5 Flash.
Para criar sua API, acesse: https://aistudio.google.com/prompts/new_chat

Para a criação do agent, foi utilizado GPT 3.5 Turbo, pois o Gemini não atendeu a capicidade necessária para execução. Não usamos o GPT 4o por conta de ter um alto custo na aplicação (~ $0.3 por execução)