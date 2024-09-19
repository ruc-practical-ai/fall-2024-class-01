# Fall 2024 Class 01 - Course Introduction

This repository holds lecture notes for Class 01 for RUC's Fall 2024 Practical AI class.

This class provides an introduction to the Practical AI course, covers some key motivations for the subject matter, and introduces some mathematical notation and background we will use throughout the semester.

## Installation

### Use via Github Codespaces (Recommended)

To use this repository via codespaces simply click on the `code` &rarr; `codespaces` &rarr; `create codespace on main` buttons.

Once the codespace is open in the browser, click the three bars in the top left corner and select `Open in VS Code Desktop`.

Widgets might work better when using VS Code Desktop vs. in the browser.

Note the codespace might take a long time to build. This is usually due to texlive dependencies. Use `Cmd` / `Ctrl` + `Shift` + `P` &rarr; `Codespaces: View Creation Logs` to check status.

If required, use `Cmd` / `Ctrl` + `Shift` + `P` &rarr; `Codespaces: Rebuild Container` to rebuild the container. Do not use `gh codespace rebuild`. This takes a long time since it re-downloads the entire image.

### Dependencies for Local Installation

This project is built on Python 3.12. Poetry is required for installation. To install Poetry, view the instructions [here](https://python-poetry.org/docs/).

In codespaces, Poetry installation is handled in the development container. The user does not need to install Poetry if working in codespaces.

This project also requires texlive to render math fonts. Texlive can be installed via the following commands.

```bash
sudo apt-get -y update
sudo apt-get -y install texlive
sudo apt-get -y install dvipng texlive-latex-extra texlive-fonts-recommended cm-super
```

In codespaces, texlive installation is also handled in the development container. The user does not need to install these packages if working in codespaces.

### Local Installation

To install locally, first install the required dependencies (Poetry and texlive), then clone the repository and navigate to its directory.

```bash
git clone https://github.com/ruc-practical-ai/fall-2024-class-01.git
cd fall-2024-class-01
```

Configure Poetry to install its virtual environment inside the repository directory.

```bash
poetry config virtualenvs.in-project true
```

Install the repository's Python dependencies.

```bash
poetry install --no-root
```

Check where Poetry built the virtual environment with the following command.

```bash
poetry env info --path
```

Open the command pallette with `Ctrl` + `Shift` + `P` and type `Python: Select Interpreter`.

Now specify that VSCode should use the that interpreter (the one in `./.venv/Scripts/python.exe`). Once you specify this, Jupyter notebooks should show the project's interpreter as an option when you click the `kernel` icon or the small icon showing the current version of python (e.g., `Python 3.12.1`) and then click `Select Another Kernel`, and finally click `Python Environments...`.

## Usage

To use this repository, explore and click through the Jupyter notebooks.

## License

This repository is provided with an MIT license. See the `LICENSE` file.

## Contributing

Please email Mauro Sanchirico at ms3978@camden.rutgers.edu (academic) or sanchirico.mauro@gmail.com (personal) with questions, comments, bug reports, or suggestions for improvement.

