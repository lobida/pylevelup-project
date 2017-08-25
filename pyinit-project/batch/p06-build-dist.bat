REM cd to repository directory
pushd "%~dp0"
cd ..

REM source code distribute, usually a .tar.gz file
python36 setup.py sdist

REM
python36 setup.py bdist_wheel --universal

pause