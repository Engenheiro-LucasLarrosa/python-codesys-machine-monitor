import csv
from datetime import datetime
from pathlib import Path
from typing import Any


CSV_FILE = Path("data") / "machine_history.csv"


def initialize_csv() -> None:
    """Cria a pasta e o arquivo CSV com cabeçalho, caso ainda não existam."""

    CSV_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not CSV_FILE.exists():
        with CSV_FILE.open(
            mode="w",
            newline="",
            encoding="utf-8",
        ) as file:
            writer = csv.writer(file)

            writer.writerow(
                [
                    "timestamp",
                    "machine_running",
                    "production_count",
                    "temperature_c",
                    "alarm_active",
                ]
            )


def save_machine_data(data: dict[str, Any]) -> None:
    """Adiciona uma nova leitura ao arquivo CSV."""

    machine_status = (
        "Ligada" if data["machine_running"] else "Desligada"
    )

    alarm_status = (
        "Ativo" if data["alarm_active"] else "Normal"
    )

    with CSV_FILE.open(
        mode="a",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                machine_status,
                data["production_count"],
                f"{data['temperature']:.1f}",
                alarm_status,
            ]
        )