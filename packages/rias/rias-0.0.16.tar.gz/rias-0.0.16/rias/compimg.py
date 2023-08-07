import os
import hashlib
import uuid


def compimgformat_image(folder_path=".") -> None:
    os.chdir(folder_path)
    for file in os.listdir():
        if ".py" not in file:
            if file[0:1:1] != ".":
                # print(file, f"\t-->\t{file[0:-3:1]}png")
                layer = file[0:-3:1].replace(".", "")
                os.rename(file, f"{layer}.png")


def compimgremove_duplicate_images(folder_path=".") -> None:
    # Zunächst werden alle Bilddateien im Ordner eingelesen
    image_files = [
        f
        for f in os.listdir(folder_path)
        if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".jpeg")
    ]
    delete = []
    # Für jedes Bild wird ein Hash-Wert berechnet
    image_hashes = {}
    for file in image_files:
        with open(os.path.join(folder_path, file), "rb") as f:
            hash = hashlib.sha256(f.read()).hexdigest()
            # Wenn es bereits ein Bild mit demselben Hash gibt, wird es gelöscht
            if hash in image_hashes:
                delete.append(file)  # --> Test new Thread
                # os.remove(os.path.join(folder_path, file))
            else:
                image_hashes[hash] = file

    for runner in delete:
        os.remove(os.path.join(folder_path, runner))


def compimgrename(pathx="."):
    # New Thread
    for runner in os.listdir(pathx):
        if not ".py" in runner:
            new_name = (
                f"{str(uuid.uuid4()).replace('-','').replace('.png','')[0:21:1]}.png"
            )
            os.replace(runner, new_name)


def compimg(content=".") -> None:
    print("\t Load Comp Image Module \n")
    print("\t Load Comp Image Format \n")
    compimgformat_image(content)
    print("\t Load Comp Image Duplicate \n ")
    compimgremove_duplicate_images(content)
    print("\t Load Comp Image Rename \n")
    compimgrename(content)
