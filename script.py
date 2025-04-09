import os
from datetime import datetime

repo_path = os.path.dirname(os.path.abspath(__file__))
counter_file = os.path.join(repo_path, 'counter.txt')

# Read current count
if os.path.exists(counter_file):
    with open(counter_file, 'r') as file:
        try:
            count = int(file.read())
        except ValueError:
            count = 0
else:
    count = 0

# Increment and write back
count += 1
with open(counter_file, 'w') as file:
    file.write(str(count))

# Git commit and push
os.chdir(repo_path)
os.system('git add counter.txt')
os.system(f'git commit -m "Auto update: count = {count} ({datetime.now()})"')
os.system('git push origin main')
