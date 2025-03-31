from pyModbusTCP.client import ModbusClient
import time

# Configuração do cliente Modbus
PLC_IP = "192.168.1.100"  # IP do CLP
PLC_PORT = 502  # Aqui porta padrão Modbus
modbus_client = ModbusClient(host=PLC_IP, port=PLC_PORT, auto_open=True)

def ler_registrador(endereco):
    """Lê um registrador Modbus."""
    valor = modbus_client.read_holding_registers(endereco, 1)
    if valor:
        return valor[0]
    else:
        print(f"Erro ao ler registrador {endereco}")
        return None

def escrever_registrador(endereco, valor):
    """Escreve um valor em um registrador Modbus."""
    sucesso = modbus_client.write_single_register(endereco, valor)
    if sucesso:
        print(f"Registrador {endereco} atualizado para {valor}")
    else:
        print(f"Erro ao escrever no registrador {endereco}")

if __name__ == "__main__":
    while True:
        # Exemplo da leitura de um registrador
        temp_atual = ler_registrador(0)
        if temp_atual is not None:
            print(f"Temperatura Atual: {temp_atual}°C")

            # Se a temperatura ultrapassar um limite, aciona um atuador(notificar)
            if temp_atual > 30:
                escrever_registrador(1, 1)  # Liga o atuador
            else:
                escrever_registrador(1, 0)  # Desliga o atuador

        time.sleep(5)  # Aguarda 5 segundos antes da próxima leitura
