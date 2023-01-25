## Scaffold

1. Create a Python Virtual Environment (Python is a scripting language, this avoids running into som issues)

`python3 -m venv ~/.venv` then active it `source ~/.venv/bin/activate`

2. Create empty files: `Makefile`, `requirements.tct`, `main.py`, `Dockerfile`, `mtlib/__init__.py`

3. Populate `Makefile`
4. Setup Continuous Integration i.e. check code for issues like lint errors

![lint-failure](https://user-images.githubusercontent.com/10374083/214616546-fefeea2f-400c-4bd8-9ffa-fed53757c2de.png)

5. Build cli using Python Fire library ` ./cli-fire.py --help` to test logic
