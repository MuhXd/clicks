import os
import traceback
import shutil
import json
import time

jsonshit = {
    "everything": []
}
filecrap = json.reads(os.environ['ALL_FILES'])


def rename_files():
    folder_path = shutil.copytree("Update", "Output")
    shutil.rmtree("Update")
    for root, dirs, files in os.walk(folder_path):

        for i, file in enumerate(files, start=1):
            # do starting variables
            print(root)
            name = root.split("/")[2]
            memeUseful = root.split("/")[1]
            # split whole file name to just the start and the extension
            filename, file_extension = os.path.splitext(file)
            # check if click name exists in json
            if file == "pack.json":
                pack = {}
                with open(root + file, "r") as file:
                    lines = file.readlines()
                    pack = json.reads('\n'.join(lines))
                pack["click-files"] = filecrap[name]["c"]
                pack["release-files"] = filecrap[name]["v"]
                with open(root + file, "w") as file:
                    for line in [json.dumps(pack)]:
                        file.write(f'{line}\n')
                jsonshit["everything"].append(pack)

if __name__ == "__main__":
    if os.path.exists("Output"):
        shutil.rmtree("Output")
    os.mkdir("Update")
    shutil.copytree("../../Meme", "Update/Meme")
    shutil.copytree("../../Useful", "Update/Useful")

    rename_files()

    jsonshitall = jsonshit["everything"]

    with open("../../list.json", "w") as file:
        for line in [json.dumps(jsonshitall)]:
            file.write(f'{line}\n')
    
    shutil.rmtree("Output")
    shutil.rmtree("../../.github")
    print("Files renamed, converted, and original files removed successfully!")
