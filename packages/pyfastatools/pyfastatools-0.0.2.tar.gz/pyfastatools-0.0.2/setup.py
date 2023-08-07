from setuptools import setup

setup(
    # scripts=["src/cli.py"],
    # script_name="fastatools",
    name="pyfastatools",
    packages=["pyfastatools"],
    package_dir={"pyfastatools": "fastatools"},
    entry_points={
        "console_scripts": [
            "fastatools=cli.py"
        ]
    }
)