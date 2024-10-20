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

### Use via Dev Container

To use this repository via a Dev Container, be sure you have the Dev Containers extension installed, along with Docker Desktop and WSL 2 (Windows only). Clone the repository, open VS Code in the repository root, and click the button shown in the pop up in the bottom-right corner to open in the Dev Container.

If the popup doesn't show type `Cmd` / `Ctrl` + `Shift` + `P` &rarr; `Reopen in Container` (if the container is already built) or `Cmd` / `Ctrl` + `Shift` + `P` &rarr; `Build and Open in Container` if the container is not yet built.

### Local Installation

The dependencies required for local installation can be found in `.devcontainer/Dockerfile` and `.devcontainer/configure_environment.sh`.

For local installation, perform set up and install dependencies in the order they appear in the Dockerfile and the configuration script, starting with the Dockerfile.

Final setup commands can be found in `.devcontainer/post_attach.sh`.

Note that setup will be different depending on the local OS.

## Usage

To use this repository, explore and click through the Jupyter notebooks.

## License

This repository is provided with an MIT license. See the `LICENSE` file.

## Contributing

Please email Mauro Sanchirico at ms3978@camden.rutgers.edu (academic) or sanchirico.mauro@gmail.com (personal) with questions, comments, bug reports, or suggestions for improvement.

