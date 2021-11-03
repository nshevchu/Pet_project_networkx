set PYTHON=C:\Python38
set PYTHON_SCRIPTS=%PYTHON%\Scripts

set CURR_DIR=%CD%
set VENV=%CURR_DIR%\venv
set ACTIVATE=%VENV%\Scripts\activate.bat

cd %PYTHON%
cd %PYTHON_SCRIPTS%
pip install virtualenv
virtualenv %VENV%
cd %CURR_DIR%

%ACTIVATE%

install

