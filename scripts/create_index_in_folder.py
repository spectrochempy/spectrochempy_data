from pathlib import Path
import yaml

REPO = Path.cwd().parent / "testdata"

def write_index(path):
    files = []
    folders = []
    for p in path.iterdir():
        name = p.name
        if p.is_dir():
            folders.append(name)
            write_index(p)  # recursive
        elif name not in [".DS_Store", "__index__"]: # exclusion
            files.append(name)

    # save index
    idx = {"folders": folders, "files": files}
    index = path / "__index__"
    index.write_text(yaml.dump(idx))


write_index(REPO)
