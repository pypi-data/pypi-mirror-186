import argparse
from pathlib import Path

from .packageLister import scan


def main():
    def getArgs() -> argparse.Namespace:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "projectPath", type=str, help=""" The project directory path to scan. """
        )
        parser.add_argument(
            "-sf",
            "--showFiles",
            action="store_true",
            help=""" Show which files imported each of the packages. """,
        )
        parser.add_argument(
            "-gr",
            "--generateRequirements",
            action="store_true",
            help=""" Generate a requirements.txt file in --projectPath. """,
        )

        args = parser.parse_args()
        if not Path(args.projectPath).is_absolute():
            args.projectPath = Path.cwd() / args.projectPath
        else:
            args.projectPath = Path(args.projectPath)

        return args

    args = getArgs()
    packages = scan(args.projectPath)
    if args.generateRequirements:
        reqPath = args.projectPath / "requirements.txt"
        reqPath.write_text(
            "\n".join(
                f"{package}=={packages[package]['version']}"
                if packages[package]["version"]
                else package
                for package in sorted(packages)
            )
        )
    packages = {
        f"{package}=={packages[package]['version']}": packages[package]["files"]
        for package in sorted(packages)
    }

    if args.showFiles:
        longestKey = max(len(package) for package in packages)
        packages = [
            f"{package}{' '*(longestKey-len(package)+4)}{', '.join(file for file in packages[package])}"
            for package in packages
        ]

    print(f"Packages used in {args.projectPath.stem}:")
    print(
        *packages,
        sep="\n",
    )
