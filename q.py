import os
import subprocess
from datetime import datetime, timedelta

# ==== НАСТРОЙКИ ====
REPO_URL = "https://github.com/Void-404X/draw.git"
REPO_DIR = "draw"  # папка, куда склонируется репозиторий
COMMITS_PER_DAY = 1
start_date = datetime(2026, 1, 1)
end_date = datetime(2030, 12, 31)
# =====================

# Проверяем, склонирован ли уже репозиторий
if not os.path.isdir(REPO_DIR):
    print("📥 Клонирую репозиторий...")
    subprocess.run(["git", "clone", REPO_URL, REPO_DIR], check=True)

# Переходим в папку репозитория
os.chdir(REPO_DIR)

# Проверяем текущую ветку и переключаемся на main
subprocess.run(["git", "checkout", "main"], check=True)

current_date = start_date

while current_date <= end_date:
    for i in range(COMMITS_PER_DAY):
        with open("log.txt", "a") as file:
            file.write(f"Commit {i+1} on {current_date.strftime('%Y-%m-%d')}\n")

        subprocess.run(["git", "add", "log.txt"], check=True)

        commit_message = f"Auto commit {i+1} on {current_date.strftime('%Y-%m-%d')}"
        env = os.environ.copy()
        date_str = current_date.strftime('%Y-%m-%d %H:%M:%S')
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str

        subprocess.run(
            ["git", "commit", "-m", commit_message],
            check=True,
            env=env
        )

    current_date += timedelta(days=1)

print("📤 Отправляю коммиты на GitHub...")
subprocess.run(["git", "push", "origin", "main"], check=True)
print("✅ Все коммиты с 2026 по 2030 год успешно созданы и отправлены!")
