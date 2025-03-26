import os
import subprocess
from datetime import datetime, timedelta

# Количество коммитов в день
COMMITS_PER_DAY = 1

# Начальная дата (1 апреля 2024)
start_date = datetime(2017, 1, 1)

# Конечная дата (30 июня 2024) - исправлено
end_date = datetime(2017, 4, 5)

# Текущая дата для цикла
current_date = start_date

while current_date <= end_date:
    for i in range(COMMITS_PER_DAY):
        # Создаём/обновляем файл log.txt с фиктивными изменениями
        with open("log.txt", "a") as file:
            file.write(f"Commit {i+1} on {current_date.strftime('%Y-%m-%d')}\n")

        # Добавляем файл в Git
        subprocess.run(["git", "add", "log.txt"], check=True)

        # Делаем коммит с заданной датой
        commit_message = f"Auto commit {i+1} on {current_date.strftime('%Y-%m-%d')}"
        subprocess.run(
            ["git", "commit", "-m", commit_message, "--date", current_date.strftime('%Y-%m-%d %H:%M:%S')],
            check=True
        )

    # Переход на следующий день
    current_date += timedelta(days=1)

# Отправляем все коммиты на GitHub
subprocess.run(["git", "push", "origin", "main"], check=True)

print("✅ Все коммиты за 2024 год успешно созданы и отправлены!")