# Coscine Python SDK
![Coscine] ![Python]  
[Coscine](https://coscine.de/), short for **Co**llaborative **Sc**ientific
**In**tegration **E**nvironment, is a platform for Research Data Management.  

[Coscine]: ./data/coscine_logo_rgb.png
[Python]: ./data/python-powered-w-200x80.png
[Coscine Landing Page]: https://www.coscine.de/

## About
The *Coscine Python SDK* is an open source python package providing
a pythonic interface to the *Coscine* REST API.
### Features:  
- **Project Management**
	- Create, modify or delete projects
	- Add/Invite members to projects and set their roles
	- Download projects and all their content
- **Resource Management**
	- Create, modify or delete resources
	- Download resources and all of their content
- **File and Metadata Management**
	- Upload, download and delete files
	- Interact with metadata in an intuitive pythonic manner
	- Fetch S3 access credentials

> **DISCLAIMER**  
> Please note that this python module is developed and maintained
> by the scientific community and even though Copyright remains with
> *RWTH Aachen*, it is not an official service that *RWTH Aachen*
> provides support for.  

## Example Code

**Uploading a file to a resource located in a subproject:**
```python
import coscine
from datetime import datetime

token: str = "My Coscine API Token"
client = coscine.Client(token)
project = client.project("My Project").subproject("My Subproject")
resource = project.resource("My Resource")
metadata = resource.metadata_form()
metadata["Author"] = "Dr. Akula"
metadata["Created"] = datetime.now()
metadata["Discipline"] = "Medicine"
metadata["DAP"] = 0.32
# ...
resource.upload("file.txt", "C:/databases/file.txt", metadata)
```

**Listing all files in all resources of a project:**
```python
import coscine

token: str = "My Coscine API Token"
client = coscine.Client(token)
for resource in client.project("My Project").resources():
	for file in resource.contents():
		if not file.is_folder:
			print(file.path)
```

More examples can be found in the online [documentation].

[documentation]: https://coscine.pages.rwth-aachen.de/community-features/coscine-python-sdk

## Installation
### via the Python Package Index (PyPi)
The *Coscine Python SDK* is hosted on the [*Python Package Index (PyPi)*].  
You can download and install the package with *pip*:  
```bash
py -m pip install coscine
```

[*Python Package Index (PyPi)*]: https://pypi.org/project/coscine/

### via Conda
The package version hosted on the *Python Package Index (PyPi)* is
automatically mirrored in the community driven packaging for *Conda*.
You can download and install the package with *conda*:  
```bash
conda install -c conda-forge coscine
```
### via Git
Manual installation:  
```bash
git clone https://git.rwth-aachen.de/coscine/community-features/coscine-python-sdk.git
cd ./coscine-python-sdk
py setup.py
```

## Documentation
The source code has been thorougly documented with *Python DOCstrings*.
Documentation can be generated via a variety of tools that take advantage
of these *DOCstrings*, such as [pydoc] or [pdoc].  
Use the following script to generate documentation with *pdoc*:  
```bash
cd ./coscine-python-sdk
py -m pip install pdoc
py -m pdoc --docformat numpy --template-dir src/docs/template -o ./public ./src/coscine
```  
The documentation inside of this repository is automatically deployed to
a [GitLab-Pages instance] for online access.  

[GitLab-Pages instance]:https://coscine.pages.rwth-aachen.de/community-features/coscine-python-sdk/coscine
[pydoc]:https://docs.python.org/3/library/pydoc.html
[pdoc]:https://pypi.org/project/pdoc/

## Contact
To report bugs, request features or resolve questions open an issue inside
of the current git repository.  
Contributions and any help on improving this package are appreciated. To
contribute source code you may fork the repository and open a merge request
or simply submit a short and relevant snippet or fix inside of an issue.
More information on contributing can be found in [CONTRIBUTING.md].

[CONTRIBUTING.md]: ./CONTRIBUTING.md

## License

This project is Open Source Software and licensed under the terms of
the [MIT License](./LICENSE.txt).

> **MIT License**
> 
> Copyright (**c**) 2018-2022 *RWTH Aachen University*
> 
> Permission is hereby granted, free of charge, to any person obtaining a copy  
> of this software and associated documentation files (the "Software"), to deal  
> in the Software without restriction, including without limitation the rights  
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
> copies of the Software, and to permit persons to whom the Software is  
> furnished to do so, subject to the following conditions:  
>   
> The above copyright notice and this permission notice shall be included in all  
> copies or substantial portions of the Software.  
>   
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
> SOFTWARE.
