from pathlib import Path

REPO = Path.cwd().parent / "testdata"

def write_index(path):
    idx = ""
    for p in path.iterdir():
        if p.is_dir():
            write_index(p)  # recursive

        if idx not in [".DS_Store", "__index__"]: # exclusion
            idx += f"{p.name}\n"

    # save index
    index = path / "__index__"
    index.write_text(idx)

write_index(REPO)
