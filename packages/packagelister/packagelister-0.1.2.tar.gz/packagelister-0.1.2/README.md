# packageLister
Determine what 3rd-party packages and versions a project imports. <br>
Install with:
<pre>pip install packageLister</pre>

Only has one function: <pre>packageLister.scan()</pre><br>
It takes one optional argument and that is the directory or file to scan.<br>
If an argument isn't given, the current working directory will be scanned.

<br>
Usage:
<pre>
>>> from pathlib import Path
>>> import packageLister
>>> import json
>>> packages = packageLister.scan()
 [___________________________________________________]-100.00% Scanning packageLister.py
>>> print(json.dumps(packages, indent=2))
{
  "pathCrawler": {
    "files": [
      "src/packageLister/packageLister.py"
    ],
    "version": "0.1.0"
  },
  "printBuddies": {
    "files": [
      "src/packageLister/packageLister.py"
    ],
    "version": "0.4.1"
  }
}
</pre>
Can also be used as a cli tool:
<pre>
>packageLister packageLister -sf
 [___________________________________________________]-100.00% Scanning packageLister_cli.py
Packages used in packageLister:
pathCrawler==0.0.3     src\packageLister\packageLister.py
printBuddies==0.2.2    src\packageLister\packageLister.py
</pre>
Cli help:
<pre>
>packageLister -h
usage: packageLister [-h] [-p PROJECTPATH] [-sf] [-gr]

options:
  -h, --help            show this help message and exit
  -p PROJECTPATH, --projectPath PROJECTPATH
                        The project directory path to scan.
  -sf, --showFiles      Show which files imported each of the packages.
  -gr, --generateRequirements
                        Generate a requirements.txt file in --projectPath.
</pre>