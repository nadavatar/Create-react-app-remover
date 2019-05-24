import os
import time

# start removing the unneeded files
os.remove('./public/favicon.ico')
os.remove('./src/App.css')
os.remove('./src/App.test.js')
os.remove('./src/logo.svg')
os.remove('./src/serviceWorker.js')

# start removing the unneeded line in index.html
with open('./public/index.html', 'r') as infile:
    lines = infile.readlines()

with open('./public/index.html', 'w') as outfile:
    for pos, line in enumerate(lines):
        if pos != 4:
            outfile.write(line)

# start removing the unneeded lines in app.js
with open('./src/App.js', 'r') as infile:
    lines = infile.readlines()

app_unneeded_lines = [1, 2]
app_unneeded_lines.extend(list(range(7, 21)))

with open('./src/App.js', 'w') as outfile:
    for pos, line in enumerate(lines):
        if pos not in app_unneeded_lines:
            outfile.write(line)

# start removing the unneeded lines in index.js
with open('./src/index.js', 'r') as infile:
    lines = infile.readlines()

index_unneeded_lines = [4, 8, 9, 10, 11]

with open('./src/index.js', 'w') as outfile:
    for pos, line in enumerate(lines):
        if pos not in index_unneeded_lines:
            outfile.write(line)

print('Your project is now clean and ready to go, \nEnjoy!')
time.sleep(3)
