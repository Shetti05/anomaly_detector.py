import os
import hashlib
import shutil

SOURCE_DIR = "data"
DUPLICATE_DIR = "duplicates"

os.makedirs(DUPLICATE_DIR, exist_ok=True)

def get_file_hash(path):
    hasher = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

hash_map = {}

for root, _, files in os.walk(SOURCE_DIR):
    for file in files:
        path = os.path.join(root, file)
        file_hash = get_file_hash(path)

        if file_hash in hash_map:
            shutil.move(path, os.path.join(DUPLICATE_DIR, file))
            print(f"Duplicate moved: {file}")
        else:
            hash_map[file_hash] = path

print("✅ Deduplication complete")
