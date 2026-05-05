import os
import tkinter as tk
from tkinter import filedialog, messagebox

files = [
    "test1.txt", "test2.txt",
    "image1.jpg", "image2.png",
    "music1.mp3",
    "video1.mp4",
    "doc1.pdf",
    "data1.csv",
    "script.py",
    "note.md"
]

def create_files():
    folder_path = filedialog.askdirectory()
    
    if not folder_path:
        return
    
    os.makedirs(folder_path, exist_ok=True)

    for file in files:
        path = os.path.join(folder_path, file)
        with open(path, "w") as f:
            pass

    messagebox.showinfo("完了", "ファイル作成しました")

# GUI
root = tk.Tk()
root.title("テストファイル作成ツール")

btn = tk.Button(root, text="フォルダ選択して作成", command=create_files)
btn.pack(padx=20, pady=20)

root.mainloop()