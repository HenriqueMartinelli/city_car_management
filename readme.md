# City Car Management

Este é o projeto **City Car Management**, uma API que gerencia proprietários de carros e seus veículos. A API permite criar, listar e gerenciar proprietários e veículos associados.

## Funcionalidades

- **Adicionar proprietário**: Adiciona um novo proprietário de carros.
- **Adicionar carro**: Adiciona um carro associado a um proprietário, com a restrição de até 3 carros por proprietário.
- **Listar proprietários**: Lista todos os proprietários cadastrados.

## Tecnologias Utilizadas

- **Python 3.12**
- **Flask**
- **Flask-Migrate** (para gerenciamento de migrações de banco de dados)
- **PostgreSQL**
- **SQLAlchemy** (ORM)
- **Poetry** (para gerenciamento de dependências)
- **Docker** e **Docker Compose**

## Requisitos

- **Docker** e **Docker Compose** instalados
- **Python 3.12+** instalado

## Configuração do Projeto

### Passo a Passo para Executar o Projeto

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu_usuario/city-car-management.git
   cd city-car-management´´

2. **Execute o projeto usando Docker.**
    ```bash
    docker-compose up web
   
    O comando irá:Construir as imagens do Docker,
    Subir os containers do banco de dados PostgreSQL e da API Flask.
    O container do PostgreSQL será iniciado, e o script de espera (wait-for-it.sh) 
    será utilizado para garantir que o banco de dados esteja disponível antes de iniciar o Flask.

3.  **Execute o test**
    ```bash
    docker-compose up test


_________________________
## Rotas e Entradas da API

A API **City Car Management** possui algumas rotas principais que permitem gerenciar **proprietários** e **carros**. Abaixo estão as rotas, métodos HTTP suportados e os dados de entrada esperados:

### 1. `POST /owners`

- **Descrição**: Cria um novo proprietário de carros.
- **Método HTTP**: `POST`
- **Entrada**:
  - **Corpo da Requisição (JSON)**:
    ```json
    {
      "name": "Nome do Proprietário"
    }
    ```
  - O nome do proprietário é obrigatório.
- **Resposta**:
  - Código HTTP 201 (Created) se o proprietário for criado com sucesso.
  - Corpo da resposta (JSON):
    ```json
    {
      "message": "Owner added successfully"
    }
    ```
  - Código HTTP 400 (Bad Request) se houver erro na entrada.

### 2. `POST /owners/<int:owner_id>/cars`

- **Descrição**: Adiciona um carro para um proprietário específico, limitado a um máximo de 3 carros por proprietário.
- **Método HTTP**: `POST`
- **Entrada**:
  - **Parâmetro de URL**:
    - `owner_id`: O ID do proprietário que receberá o carro.
  - **Corpo da Requisição (JSON)**:
    ```json
    {
      "model": "Modelo do Carro",
      "color": "Cor do Carro"
    }
    ```
  - O `model` e a `color` do carro são obrigatórios.
- **Restrições**:
  - Um proprietário pode ter no máximo 3 carros.
- **Resposta**:
  - Código HTTP 201 (Created) se o carro for adicionado com sucesso.
  - Corpo da resposta (JSON):
    ```json
    {
      "message": "Car added successfully"
    }
    ```
  - Código HTTP 400 (Bad Request) se o proprietário já tiver 3 carros ou se houver erro na entrada.

    