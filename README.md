# automacao-clp
 Código para ser usado para leitura e escrita de registradores em um CLP compatível com Modbus TCP.

Disponibilizado um exemplo de um código em Python para controle e automação usando um CLP (Controlador Lógico Programável) via protocolo Modbus. Esse código pode ser usado para leitura e escrita de registradores em um CLP compatível com Modbus TCP.

Resumindo a criação desse código:

- Conexão com o CLP: O código se conecta ao CLP usando o protocolo Modbus TCP.
- Leitura de registradores: Ler a temperatura de um sensor conectado ao CLP.
- Tomada de decisão: Se a temperatura ultrapassar 30°C, aciona um atuador.
- Escrita de registradores: Atualizar o registrador para ligar ou desligar um dispositivo.

## Instalação das Dependências
Antes de rodar o script, instale as bibliotecas necessárias com:
```bash
pip install -r requirements.txt

(Dessa forma, qualquer pessoa que clonar o repositório pode instalar as dependências facilmente e evitar erros. )
