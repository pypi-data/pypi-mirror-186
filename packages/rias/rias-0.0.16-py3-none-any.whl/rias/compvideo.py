import os
import hashlib
import sys
import uuid


def compvideo_remove(folder_path="."):
    # Zunächst werden alle Bilddateien im Ordner eingelesen
    image_files = [
        f
        for f in os.listdir(folder_path)
        if f.endswith(".mp4") or f.endswith(".MP4") or f.endswith("mp4")
    ]

    # Für jedes Bild wird ein Hash-Wert berechnet
    image_hashes = {}
    for file in image_files:
        with open(os.path.join(folder_path, file), "rb") as f:
            hash = hashlib.sha256(f.read()).hexdigest()
            # Wenn es bereits ein Bild mit demselben Hash gibt, wird es gelöscht
            if hash in image_hashes:
                os.remove(os.path.join(folder_path, file))
            else:
                image_hashes[hash] = file


def compvideo_rename(folder_path="."):
    # New Thread
    image_files = [
        f
        for f in os.listdir(folder_path)
        if f.endswith(".mp4") or f.endswith(".MP4") or f.endswith("mp4")
    ]
    for file in image_files:
        uuidx = str(uuid.uuid4().hex).replace("-", "")[0:21:1]
        os.rename(file, f"{uuidx}.mp4")


def compvideo(content=".") -> None:
    print("Load Comp Video")
    print("\t Load Comp Video Remove")
    compvideo_remove(content)
    print("\t Load Comp Video Rename")
    compvideo_rename(content)
