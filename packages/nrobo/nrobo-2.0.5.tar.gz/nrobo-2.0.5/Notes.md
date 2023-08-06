Packaging and uploading to TestPyPi or PyPi
-------------------------------------------

1. Update version number in version.yaml
2. Install build
   - On Unix/Linux/Mac
     - `pip3 install build` 
   - On Windows
     - `pip install build`
3. Install twine
   - On Unix/Linux/Mac
        - `pip3 install twine`
     - On Windows
       - `pip install twine`
4. Package and upload nRobo on target environment 
   - On Unix/Linux/Mac
     - `python3 package_and_upload_nrobo.py -t <test | prod>`
   - On Windows
     - `python package_and_upload_nrobo.py -t <test | prod>`

Allure Reporting Framework
--------------------------

* Allure Reports 
https://docs.qameta.io/allure-report/
* Allure Command Line Tools
https://docs.qameta.io/allure/#_commandline
$ brew tap qameta/allure
$ brew install allure

Generate and save allure report as html
---------------------------------------

`allure generate tests_advanced_reports --clean`

Packaging and Publishing to PyPi
--------------------------------

- `python3 -m pip install --upgrade build`
  - `python3 -m build`
- Check build
  - `twine check  dist/*`
- `python3 -m pip install --upgrade twine`
  - `python3 -m twine upload --repository testpypi dist/* --verbose`


Key Files
-----------

- `pyproject.toml`
- `nrobo/__init__.py`
- `nrobo/__main__.py`
- `speedboat.py`
- `requirements.py`
- `Notes.md`
- `README.md`
- `conftest.py`

[Configure Git Signature](https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key?platform=mac)
-------------------------

- ` git config --global gpg.format ssh`
- `git config --global user.signingkey /PATH/TO/.SSH/KEY.PUB`

[Singing Git Commits](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits)
---------------------
 
- `git commit -S -m "YOUR_COMMIT_MESSAGE"`  

