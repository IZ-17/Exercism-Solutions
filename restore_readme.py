import os
import subprocess

# Скрипт ищет папки задач внутри 'solutions/python'
TRACK_PATH = "./solutions/python" 

def restore_docs():
    if not os.path.exists(TRACK_PATH):
        print(f"❌ Папка {TRACK_PATH} не найдена! Проверьте путь.")
        return

    # Находим все папки задач (armstrong-numbers, black-jack и т.д.)
    exercises = [d for d in os.listdir(TRACK_PATH) if os.path.isdir(os.path.join(TRACK_PATH, d))]
    print(f"Найдено {len(exercises)} задач. Начинаем загрузку README.md...")

    for exercise in exercises:
        exercise_dir = os.path.join(TRACK_PATH, exercise)
        readme_path = os.path.join(exercise_dir, "README.md")
        
        # Если README уже скачан, пропускаем задачу
        if os.path.exists(readme_path):
            continue
            
        print(f"📥 Скачиваем описание для: {exercise}...")
        
        # Передаем утилите команду скачать файлы прямо в вашу текущую папку бэкапа
        cmd = f'exercism download --track=python --exercise={exercise} --workspace="{os.path.abspath(TRACK_PATH)}/../.."'
        
        try:
            subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception as e:
            print(f"❌ Ошибка при скачивании {exercise}: {e}")

    print("\n✨ Все README.md успешно добавлены к вашим решениям!")

if __name__ == "__main__":
    restore_docs()
