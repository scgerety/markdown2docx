
import glob
import pypandoc
import os

dir_path = os.path.realpath(os.path.dirname(__file__))
WORD_DIR = os.path.join(dir_path, "Word Docs")

def convert_md(markdown, stem_name):
    pypandoc.convert_file(markdown, "docx", outputfile=f"{stem_name}.docx")

def main(directory=dir_path):
    for filename in glob.glob(f"{directory}/*.md"):
        _, f_ext = os.path.split(filename)
        name, _ = os.path.splitext(f_ext)
        convert_md(filename, f"{os.path.join(WORD_DIR, name)}")

if __name__ == "__main__":
    if not os.path.exists(WORD_DIR):
        os.mkdir(WORD_DIR)
    main()
