echo %CD%
dir
dir app
python -c "import sys; print(sys.path)"
uvicorn app.main:app --reload