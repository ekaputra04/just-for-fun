import os
import random

repository_url = "https://github.com/ekaputra04/commit-generator.git"
commit_message = "just for fun"

jumlah_perulangan = random.randint(1, 5)

for _ in range(jumlah_perulangan):
  with open("note.txt", "a+") as file:
      file.write("Just for fun :).\n")

  os.system("git add .")
  os.system(f'git commit  -m "{commit_message}"')

os.system("git push -u origin main")
