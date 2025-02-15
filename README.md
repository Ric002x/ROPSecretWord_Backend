# ROPWebChat - Backend

## 📋Sobre

Este projeto é um **BACKEND** para um jogo de palavras inspirado no Wordle. O objetivo do jogo é adivinhar uma palavra de 5 letras em até 6 tentativas.

A API tem duas funções principais:
✅ Definir diariamente a palavra que os jogadores devem adivinhar.
✅ Verificar e validar as tentativas dos jogadores, fornecendo feedback sobre acertos e posições das letras.


## 🖥️Tecnologias

- **Python**: Linguagem de programação utilizada no backend.
- **Django**: Framework web para desenvolvimento rápido e seguro.
- **Django Rest Framework**: Ferramenta para criação de APIs RESTful robustas e escaláveis.
- **APScheduler**: Biblioteca para agendar e gerenciar a execução automática de tarefas em horários ou intervalos específicos.


## 📌Endpoints

### 🔍Palavra do Dia
**URL**: [GET] /api/v1/words/
Respostas:

🟩 200 OK – Retorna a palavra do dia (deverá ser oculta para o jogador).
```json
{
    "id": "id_da_palavra",
    "word": "palavra",
    "date": "data"
}
```

### 🎯Tentativas do Jogador
**URL**: [GET] /api/v1/words/validate/<word>
Respostas:

🟥 400 Bad Request - O jogador enviou uma palavra inválida ou inexistente
```json
{"detail": "palavra inválida ou inexistente"}
```

🟩 200 OK - Retorna o resultado da tentativa.
```json
{
    "resultado": ["0", "1", "1", "2", "1"]
}
```

> Cada número representa o status de cada letra da palavra enviada pelo jogador em comparação com a palavra do dia:
> 
> 2 → A letra está correta e na posição certa.
>
> 1 → A letra está presente na palavra, mas na posição errada.
>
> 0 → A letra não existe na palavra.


## 🔧Instalação


1. Clone o repositório:

   ```bash
   git clone https://github.com/Ric002x/...
   ```

2. Acesse o diretório do projeto:

   ```bash
   cd ...
   ```

3. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv

   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

4. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```


## 📝Inicialização

1. Execute as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

2. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

3. A API estará disponível em:  
   [http://localhost:8000](http://localhost:8000)


## Licença
Este projeto é licenciado sob a licença **MIT**. Consulte o arquivo `LICENSE` para mais informações.
