from pathlib import Path

REPO = Path(__file__).resolve().parent.parent / "testdata"

for path in REPO.glob("**/*"):
    if " " in str(path):
        print(path)
        path.rename(Path(str(path).replace(" ", "_")))
