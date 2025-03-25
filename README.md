# DTU CDIO ASIGNMENT



## PULLING AND PUSHING:

We are using GitHub Actions to strip the outputs of Jupyter notebooks when they are pushed to the repository.

Therefore, when pulling down a notebook, all the outputs will be cleared. It is important to clear the notebooks and commit it before pulling to avoid merge conflicts.

To make this process easier, you can use the Python library `nbstripout`:

```
pip install nbstripout
```

You can then clear the outputs of all notebooks in a directory using the following commands:

```powershell
Get-ChildItem -Recurse -Filter *.ipynb | ForEach-Object { nbstripout $_.FullName }
```

```bash
find . -name "*.ipynb" -exec nbstripout {} \;
```