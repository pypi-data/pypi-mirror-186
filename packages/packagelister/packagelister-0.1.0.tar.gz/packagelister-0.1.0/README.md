# packageLister
Determine what 3rd-party packages and versions a project imports. <br>
Install with:
<pre>pip install packageLister</pre>

Only has one function: packageLister.scan()

<br>
Usage:
<pre>
>>> from pathlib import Path
>>> import packageLister
>>> packageLister.scan(Path.cwd())
 [___________________________________________________]-100.00% Scanning packageLister.py
{'pathCrawler==0.0.3': ['src/packageLister/packageLister.py'], 'printBuddies==0.2.2': ['src/packageLister/packageLister.py']}
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
usage: packageLister [-h] [-sf] [-gr] projectPath

positional arguments:
  projectPath           The project directory path to scan.

options:
  -h, --help            show this help message and exit
  -sf, --showFiles      Show which files imported each of the packages.
  -gr, --generateRequirements
                        Generate a requirements.txt file in --projectPath.
</pre>