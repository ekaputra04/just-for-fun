import os
import subprocess

# Ganti dengan informasi repositori Anda
repository_url = "https://github.com/ekaputra04/commit-generator.git"
# commit_author = "Your Name <your.email@example.com>"
commit_message = "Fake commit message"

# Clone repositori
# os.system(f"git clone {repository_url}")
# os.chdir("commit-generator")

# Tambahkan perubahan ke file atau buat file baru
with open("note.txt", "w") as file:
    file.write("This is a fake file.")

# Lakukan commit
os.system("git add .")
os.system(f'git commit  -m "{commit_message}"')

# Push perubahan ke repositori
os.system("git push -u origin main")
