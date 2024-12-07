import os
import time
import sys
from humanize import naturalsize

def get_oldest_files(directory, count=5):
    """
    Return the 'count' oldest files in a directory, including subdirectories.
    """
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            try:
                atime = os.path.getatime(filepath)  # Last access time
                size = os.path.getsize(filepath)
                files.append((filepath, atime, size))
            except (FileNotFoundError, PermissionError):
                continue
    
    # Sort files by access time (oldest first)
    files.sort(key=lambda x: x[1])
    return files[:count]

def display_files(files):
    """
    Display file information in a user-friendly format.
    """
    print("\nCele mai vechi fișiere accesate:")
    for i, (path, atime, size) in enumerate(files):
        print(f"{i+1}. {path}")
        print(f"   Ultimul acces: {time.ctime(atime)}")
        print(f"   Mărime: {naturalsize(size)}")
    print()

def delete_files(files):
    """
    Ask user which files to delete.
    """
    while True:
        try:
            choice = input("Introduceți numerele fișierelor de șters (separate prin virgulă) sau 'q' pentru a ieși: ").strip()
            if choice.lower() == 'q':
                print("Ieșire fără a șterge fișiere.")
                break
            indices = list(map(int, choice.split(',')))
            for index in indices:
                if 1 <= index <= len(files):
                    os.remove(files[index - 1][0])
                    print(f"Fișier șters: {files[index - 1][0]}")
                else:
                    print(f"Număr invalid: {index}")
        except ValueError:
            print("Intrare invalidă. Asigurați-vă că introduceți numere valide.")
        except FileNotFoundError:
            print("Fișierul nu mai există deja.")
        else:
            break

def main():
    if len(sys.argv) != 2:
        print("Utilizare: python script.py <cale_director>")
        return
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Director invalid: {directory}")
        return
    
    try:
        oldest_files = get_oldest_files(directory)
        if not oldest_files:
            print("Nu s-au găsit fișiere.")
            return

        display_files(oldest_files)
        delete_files(oldest_files)
    except Exception as e:
        print(f"Eroare: {e}")

if __name__ == "__main__":
    main()