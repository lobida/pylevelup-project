REM cd to repository directory
pushd "%~dp0"
cd ..

REM install the package
cd pyinit
python36 zzz_ezinstall.py

REM create doc tree
cd ..
cd batch
python36 create_doctree.py

REM build html doc
cd ..

make html

echo Complete!

pause