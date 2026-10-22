import os
import shutil

def copy_static_to_public():
    """
    Copia ricorsivamente tutti i file dalla directory 'static' alla directory 'public',
    dopo aver eliminato il contenuto esistente di 'public'.
    """
    # Definisci le directory sorgente e destinazione
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_dir = os.path.join(project_root, "static")
    public_dir = os.path.join(project_root, "public")

    # Elimina il contenuto della directory 'public' se esiste
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
        print(f"Eliminata la directory esistente: {public_dir}")

    # Ricrea la directory 'public'
    os.mkdir(public_dir)
    print(f"Creato la directory: {public_dir}")

    # Copia ricorsivamente tutti i file da 'static' a 'public'
    copy_files_recursive(static_dir, public_dir)

def copy_files_recursive(source_dir, dest_dir):
    """
    Copia ricorsivamente tutti i file da source_dir a dest_dir.

    Args:
        source_dir (str): Directory sorgente.
        dest_dir (str): Directory di destinazione.
    """
    # Itera su tutti gli elementi nella directory sorgente
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)

        # Se è una directory, copia ricorsivamente
        if os.path.isdir(source_path):
            os.mkdir(dest_path)
            print(f"Creato directory: {dest_path}")
            copy_files_recursive(source_path, dest_path)
        # Se è un file, copia
        else:
            shutil.copy(source_path, dest_path)
            print(f"Copiato file: {source_path} -> {dest_path}")
