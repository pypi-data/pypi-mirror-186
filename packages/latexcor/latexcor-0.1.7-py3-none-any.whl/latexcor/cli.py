import argparse
import chardet
import codecs
import sys
import os
import time
import subprocess
from datetime import datetime


clean_up = [
    ".bar",
    ".cor",
    ".lua",
    ".lub",
    ".tab",
    ".log",
    ".gz",
    ".aux",
    ".out",
    ".fdb_latexmk",
    ".fls",
    ".xdv",
    ".dvi",
]


def predict_encoding(file_path: str, n_lines: int = 20) -> str:
    """Predict a file's encoding using chardet

    Args:
        file_path (str): _description_
        n_lines (int, optional): _description_. Defaults to 20.

    Returns:
        str: _description_
    """

    # Open the file as binary data
    with open(file_path, "rb") as f:
        # Join binary lines for specified number of lines
        rawdata = b"".join([f.readline() for _ in range(n_lines)])

    return chardet.detect(rawdata)["encoding"]


def convert_utf8(path_to_watch: str) -> None:
    """_summary_

    Args:
        path_to_watch (str): _description_
    """
    # https://stackoverflow.com/questions/1728376/get-a-list-of-all-the-encodings-python-can-encode-to
    paths = initilisation(path_to_watch)
    files = get_files(paths)
    for file in files:
        encoding = predict_encoding(file["name"])

        if encoding != "utf-8":
            print(file["name"], encoding)
            if encoding == "Windows-1252":
                print("Windows-1252 -> cp1252 -> utf-8")

                with open(file["name"], "r", encoding="cp1252") as f:
                    contenu = f.read()
                # print(contenu)
                with open(file["name"], "w", encoding="utf_8") as f:
                    f.write(contenu)

            elif encoding == "ISO-8859-1":
                print("ISO-8859-1-> latin_1 -> utf-8")
                with open(file["name"], "r", encoding="latin_1") as f:
                    contenu = f.read()
                # print(contenu)
                with open(file["name"], "w", encoding="utf_8") as f:
                    f.write(contenu)

            elif encoding == "MacRoman":
                print("MacRoman: no need to convert")

            elif encoding == "ascii":
                print("ascii -> utf-8: don't work. Try manualy")

            # for _ in range(2):
            #     with open(file["name"], "r", encoding=encoding) as f:
            #         contenu = f.read()
            #     with open(file["name"], "w", encoding="utf-8") as f:
            #         f.write(contenu)
            # print(file["name"], "conversion utf-8 réussie")


def initilisation(path_to_watch: str) -> list:
    """Initialisation

    Args:
        path_to_watch (str): path to watch

    Returns:
        list: _description_
    """
    paths = [path_to_watch]
    for root, dirs, files in os.walk(path_to_watch):
        for dir in dirs:
            paths.append(os.path.join(path_to_watch, dir))
    return paths


def get_files(paths: list) -> list[dict]:
    """_summary_

    Args:
        paths (list): _description_

    Returns:
        list[dict]: _description_
    """
    files = []
    for path in paths:
        try:
            temp_list = [
                {
                    "name": os.path.join(path, file),
                    "time_modification": os.path.getmtime(os.path.join(path, file)),
                    "path": path,
                }
                for file in os.listdir(path)
                if ".tex" in file
            ]
            files = files + temp_list
        except:
            pass
    return files


def clean_aux(paths: list) -> None:
    """Remove aux files

    Args:
        paths (list): _description_
    """
    for path in paths:
        try:
            for file in os.listdir(path):
                ext = os.path.splitext((file))[1]
                if ext in clean_up:
                    os.remove(os.path.join(path, file))
        except:
            pass


def recompile_all(path_to_watch: str, latex_engine: str) -> None:
    """Recomplie all .tex files in path_to_watch folder with latex_engine

    Args:
        path_to_watch (str): _description_
        latex_engine (str): _description_
    """

    cmd = f"latexmk -interaction=nonstopmode -{latex_engine}"
    print(cmd)
    subprocess.call(cmd, shell=True)
    subprocess.call(cmd, shell=True)
    clean_aux([path_to_watch])


def watch(path_to_watch: str, latex_engine: str) -> None:
    """Watch path_to_watch folder

    Args:
        path_to_watch (str): _description_
        latex_engine (str): _description_
    """
    print("Démarrage de la surveillance.")
    print(f"Dossier: {path_to_watch}")
    paths = initilisation(path_to_watch)
    before = get_files(paths)
    while 1:
        time.sleep(10)
        after = get_files(paths)
        added = [f for f in after if not f in before]
        if added:
            print("Fichier ajouté ou modifié")
            for file in added:
                if " " in file["path"]:
                    output = paths[0]
                else:
                    output = file["path"]
                print(output)
                cmd = f"latexmk \"{file['name']}\" -interaction=nonstopmode -{latex_engine} -output-directory=\"{os.path.join(file['path'])}\""
                print(cmd)
                subprocess.call(cmd, shell=True)
            before = after
            clean_aux(paths)


def define_latex_engine(args: argparse) -> str:
    """Process latex engine argument

    Args:
        args (argparse): _description_

    Returns:
        str: _description_
    """
    if args.lualatex:
        print("lualatex")
        return "lualatex"
    else:
        print("xelatex")
        return "xelatex"


def main() -> None:
    path_to_watch = os.getcwd()
    parser = argparse.ArgumentParser(description="""Basic usage: latexcor""")
    parser.add_argument(
        "--clean",
        action="store_true",
        default=False,
        help="clean all aux files in current directory",
    )
    parser.add_argument(
        "--recompile",
        action="store_true",
        default=False,
        help="recompile all files in current directory",
    )
    parser.add_argument(
        "--xelatex", action="store_true", default=True, help="xelatex default True"
    )
    parser.add_argument(
        "--lualatex", action="store_true", default=False, help="lualatex default False"
    )
    parser.add_argument(
        "--utf8",
        action="store_true",
        default=False,
        help="convert .tex files to utf-8 encoding",
    )
    args = parser.parse_args()
    if args.clean:
        print(f"Nettoyage du dossier: {path_to_watch}")
        clean_aux([path_to_watch])
        print("Fait")
    elif args.recompile:
        latex_engine = define_latex_engine(args)
        print("Recompile tout")
        recompile_all(path_to_watch, latex_engine)
        print("Fait")
    elif args.utf8:
        print("Conversion utf-8")
        convert_utf8(path_to_watch)
    else:
        latex_engine = define_latex_engine(args)
        watch(path_to_watch, latex_engine)


if __name__ == "__main__":
    main()
