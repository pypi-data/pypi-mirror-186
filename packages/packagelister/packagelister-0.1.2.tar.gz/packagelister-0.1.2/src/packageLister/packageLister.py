import importlib.metadata
import sys
from pathlib import Path

from pathCrawler import crawl
from printBuddies import ProgBar


def scan(projectDir: Path | str = None) -> dict:
    """Recursively scans a directory for python files to determine
    what 3rd-party packages are in use, as well as the version number
    if applicable.

    Returns a dictionary where the keys are package
    names and the values are the version number of the package if there is one
    (None if there isn't) and a list of the files that import the package.

    :param projectDir: Can be an absolute or relative path
    to a directory or a single file (.py).
    If it is relative, it will be assumed to be relative to
    the current working directory.
    If an argument isn't given, the current working directory
    will be scanned.
    If the path doesn't exist, an empty dictionary is returned."""
    if not projectDir:
        projectDir = Path.cwd()
    elif type(projectDir) is str:
        projectDir = Path(projectDir)
    if not projectDir.is_absolute():
        projectDir = projectDir.absolute()

    # Return empty dict if projectDir doesn't exist
    if not projectDir.exists():
        return {}
    # You can scan a non python file one at a time if you reeeally want to.
    if projectDir.is_file():
        files = [projectDir]
    else:
        files = [file for file in crawl(projectDir) if file.suffix == ".py"]

    bar = ProgBar(len(files) - 1, widthRatio=0.33)
    # If scanning one file, the progress bar will show 0% complete if bar.counter == 0
    if len(files) == 1:
        bar.counter = 1
    packages = {}
    standardLib = list(sys.stdlib_module_names)
    for file in files:
        bar.display(suffix=f"Scanning {file.name}")
        contents = [
            line.split()[1]
            for line in file.read_text().splitlines()
            if line.startswith(("from", "import"))
        ]
        for package in contents:
            if package.startswith("."):
                package = package[1:]
            if "." in package:
                package = package[: package.find(".")]
            if "," in package:
                package = package[:-1]
            if file.with_stem(package) not in files and package not in standardLib:
                if package in packages and str(file) not in packages[package]["files"]:
                    packages[package]["files"].append(str(file))
                else:
                    try:
                        packageVersion = importlib.metadata.version(package)
                    except Exception as e:
                        packageVersion = None
                    packages[package] = {
                        "files": [str(file)],
                        "version": packageVersion,
                    }
    return packages
