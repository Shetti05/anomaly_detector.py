import shutil
import os

def backup_files(source, destination):
    os.makedirs(destination, exist_ok=True)

    for file in os.listdir(source):
        src_file = os.path.join(source, file)
        dst_file = os.path.join(destination, file)

        if os.path.isfile(src_file):
            shutil.copy(src_file, dst_file)

    print("Backup completed successfully")

if __name__ == "__main__":
    backup_files("data", "backup")
