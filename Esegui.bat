@echo off
for /r %%f in (main.py) do (
    python "%%f"
    goto end
)
:end