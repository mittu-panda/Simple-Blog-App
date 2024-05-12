First, install Python and set the system environment path. If you're on Windows, ensure that the Python Scripts directory is added to your PATH environment variable.

Run this command to install virtualenv:
pip install virtualenv

Create a virtual environment by running this command:
virtualenv venv

To activate the virtual environment, use this command:
.\venv\Scripts\activate

Then, install FastAPI and uvicorn by running this command:
pip install fastapi uvicorn

To run the Simple Blog App, execute the following command:
uvicorn main:app --reload

