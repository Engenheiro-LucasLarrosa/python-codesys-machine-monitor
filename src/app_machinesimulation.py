import time

from csv_logger import initialize_csv, save_machine_data
from modbus import read_modbus


IP_CODESYS = "192.168.1.100"

def main():
    initialize_csv()

    while True:
        try:
            data = read_modbus(IP_CODESYS)

            if data is None:
                print("Falha na leitura Modbus TCP.")

            else:
                machine_status = (
                    "Ligada"
                    if data["machine_running"]
                    else "Desligada"
                )

                alarm_status = (
                    "Ativo"
                    if data["alarm_active"]
                    else "Normal"
                )

                print("-" * 40)
                print(f"Máquina: {machine_status}")
                print(
                    f"Produção: "
                    f"{data['production_count']} peças"
                )
                print(
                    f"Temperatura: "
                    f"{data['temperature']:.1f} °C"
                )
                print(f"Alarme: {alarm_status}")

                save_machine_data(data)

            time.sleep(1)

        except KeyboardInterrupt:
            print("\nAplicação encerrada pelo usuário.")
            break

        except Exception as error:
            print(f"Erro inesperado: {error}")
            time.sleep(2)


if __name__ == "__main__":
    main()