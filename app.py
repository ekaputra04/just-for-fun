import os
import random
import subprocess

# Ganti dengan informasi repositori Anda
repository_url = "https://github.com/ekaputra04/commit-generator.git"
# commit_author = "Your Name <your.email@example.com>"
commit_message = "Fake commit message"

# Clone repositori
# os.system(f"git clone {repository_url}")
# os.chdir("commit-generator")

jumlah_perulangan = random.randint(1, 5)

for _ in range(jumlah_perulangan):
# Tambahkan perubahan ke file atau buat file baru
  with open("note.txt", "a+") as file:
      file.write("This is a fake file.\n")

  # Lakukan commit
  os.system("git add .")
  os.system(f'git commit  -m "{commit_message}"')

# Push perubahan ke repositori
os.system("git push -u origin main")
