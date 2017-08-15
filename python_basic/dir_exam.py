import os


for root, dirs, files in os.walk("./"):
    for name in files:
        if ".py" in name and ".pyc" not in name:
            print(os.path.join(root, name))
