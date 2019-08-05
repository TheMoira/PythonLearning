from pathlib import Path

# Path() - relates to (returns the path) the current directory

path = Path("ecommerce")
print(path.exists())

path = Path()
# path.glob('*.py')  -  searhing for all the .py files in current direcoty
path = Path("D:\docs")
for file in path.glob('*.docx'):
    print(file)

