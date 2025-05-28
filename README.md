
### Integrantes do projeto
| R.A   | Nome |
| -------- | ------- |
| 24.00003-5  | Rafael Alvarez de Carvalho Ruthes    |
| 23.01178-5 | Matheus da Cunha Castilho     |
| 21.01576-7    | Gabriel Borges Silva    |

# Implementação real
O projeto do PI (back-end), está nessa mesma organização e seu código e estrutura podem ser vistos por lá. O repositório possui o nome de "chatbot".

# Arquivo conftest.py
Professora, este arquivo está auqi pois os imports do python deveriam ser diferentes ao rodar o pytest, e ao rodar o 
arquivo diretamente, então acabamos por utilizar esse código que está nesse arquivo. Sem ele, o pytest não vai funcionar.

# Projeto de Testes Automatizados - TDD

Este projeto implementa testes automatizados para funcionalidades de cadastro e login de usuários seguindo os princípios de Test-Driven Development (TDD). O desenvolvimento seguiu o ciclo Red-Green-Refactor, onde primeiro foram escritos os testes e depois implementadas as funcionalidades para que os testes passassem.

## Estrutura do Projeto

O projeto está organizado em uma estrutura de camadas, separando claramente as responsabilidades:

- `src/`: Contém o código fonte da aplicação
  - `modules/users/`: Módulos específicos para usuários
    - `users_repository.py`: Implementação do repositório de usuários
    - `users_usecase.py`: Implementação dos casos de uso de usuários
    - `users_viewmodel.py`: Modelo de visualização para usuários
  - `shared/entities/`: Entidades compartilhadas
    - `user.py`: Definição da entidade User

- `tests/`: Contém os testes automatizados
  - `modules/users/`: Testes para os módulos de usuários
    - `test_users_usecase.py`: Testes para os casos de uso de usuários

## Requisitos Implementados

Os testes automatizados cobrem os seguintes requisitos:

- Verificação de cadastro de usuário com dados válidos
- Verificação de impedimento de cadastro com e-mail já existente
- Garantia de login com credenciais válidas
- Garantia de falha no login com e-mail ou senha inválidos
- Verificação de validação de campos obrigatórios

## Como Executar os Testes

Para executar os testes, siga os passos abaixo:

### Instalação das Dependências

Execute o comando abaixo para instalar as dependências necessárias:

```
pip install pytest bcrypt pyjwt pydantic
```

### Executando os Testes

Na raiz do projeto, execute:

```
pytest
```

## Implementação

A implementação possui uma separação clara entre entidades, casos de uso e repositórios. O repositório utilizado nos testes é um mock que simula o comportamento de um banco de dados real.

O caso de uso de usuários implementa as funcionalidades de cadastro e login, com validação de campos obrigatórios e tratamento adequado de erros. A senha é armazenada de forma segura utilizando bcrypt para hash, e o login gera um token JWT para autenticação.

Os testes verificam todos os cenários especificados nos requisitos, garantindo que o sistema se comporta conforme esperado tanto em casos de sucesso quanto de falha.
