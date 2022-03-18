from pathlib import Path

REPO = Path.cwd().parent / "testdata"

for path in REPO.glob("**/*"):
    if " " in str(path):
        print(path)
        path.rename(Path(str(path).replace(" ", "_")))
