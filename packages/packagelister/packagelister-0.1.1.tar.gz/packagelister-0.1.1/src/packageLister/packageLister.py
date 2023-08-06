import importlib.metadata
import sys
from pathlib import Path

from pathCrawler import crawl
from printBuddies import ProgBar


def scan(projectDir: str) -> dict:
    """Returns a dictionary where the keys are 3rd-party package
    names and the values are lists of the files that import them
    and the version number of the package if there is one."""
    projectDir = Path(projectDir).absolute()
    files = [file for file in crawl(projectDir) if file.suffix == ".py"]
    bar = ProgBar(len(files) - 1, widthRatio=0.25)
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
                relPath = file.relative_to(projectDir)
                if (
                    package in packages
                    and str(relPath) not in packages[package]["files"]
                ):
                    packages[package]["files"].append(str(relPath))
                else:
                    try:
                        packageVersion = importlib.metadata.version(package)
                    except Exception as e:
                        packageVersion = None
                    packages[package] = {
                        "files": [str(relPath)],
                        "version": packageVersion,
                    }
    return packages
