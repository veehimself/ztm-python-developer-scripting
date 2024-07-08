# ztm-python-developer-scripting

## Initial setup

[Install  uv](https://github.com/astral-sh/uv?tab=readme-ov-file#getting-started)


```sh
uv venv  # Create a virtual environment at .venv
```

#### following the standards virtual environment is named `.venv`

---

### To activate the virtual enivronment:

```sh
# On macOS and Linux.
source .venv/bin/activate

# On Windows.
.venv\Scripts\activate
```
---
### To install a package into the virtual environment:

```sh
uv pip install <package>            # Install <Package>.
uv pip install -r requirements.txt  # Install from a requirements.txt file.
```
---
### To run the project 
- create a virtual environment
- activate the virtual environment
- install packages from `requirements.txt` 