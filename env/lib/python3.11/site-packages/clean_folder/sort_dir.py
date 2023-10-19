"""main"""
import sys
from pathlib import Path
from .process_directory import process_directory

def main():
    """ Основна функція для обробки папки """
    if len(sys.argv) != 2:
        print("Usage: python sort_dir.py <folder_path>")
        return

    folder_path = Path(sys.argv[1])
    sorted_folder_path = folder_path

    # Викликаємо функцію для обробки папки
    process_directory(folder_path, sorted_folder_path)

    print("Script is done !!!")

if __name__ == "__main__":
    main()

# python3 sort_dir.py ~/Desktop/мотлох
