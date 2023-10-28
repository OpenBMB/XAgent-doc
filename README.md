# This is doc of XAgent website.
> Develop in win11 by Arno

1. Create virtual environment
```python
python -m venv .venv
```

2. Activate virtual environment

| Platform | Shell      | Command to activate virtual environment           |
|----------|------------|---------------------------------------------------|
| POSIX    | bash/zsh   | `source .venv/bin/activate`                    |
|          | fish       | `source .venv/bin/activate.fish`               |
|          | csh/tcsh   | `source .venv/bin/activate.csh`                |
|          | PowerShell | `.venv/bin/Activate.ps1`                       |
| Windows  | cmd.exe    | `.venv\Scripts\activate.bat`                |
|          | PowerShell | `.venv\\Scripts\Activate.ps1`             |

3. Install `poetry` and use it to install dependencies

```python
pip install poetry
poetry install
```

4. Build html 

```bash
.\docs\make html
```