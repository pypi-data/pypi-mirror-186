# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['another']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'another',
    'version': '0.2.1',
    'description': '',
    'long_description': '# Another\n"Another" Python backend framework, for fun.\n\n## Installation\n\n```bash\npip install another\n```\n\nYou also need an ASGI server, such as [Uvicorn](https://github.com/encode/uvicorn) or [Granian](https://github.com/emmett-framework/granian).\n\n```bash\npip install uvicorn\n# or\npip install granian\n```\n\n## Usage\n\nCreate a `main.py` file and copy-paste the following snippet into it.\n\n```python\nfrom another import Another, Status, Request, Response\n\n\napp = Another()\n\n@app.get("/hello")\ndef hellow_another(req: Request):\n\treturn Response({\n        "message": "Hello!",\n        "extra": req.query\n    }, status=Status.HTTP_200_OK)\n```\n\nAnd then run the server:\n\n```bash\nuvicorn main:app\n```\n\nNow open this link [localhost:8000/hello?first_name=Mads&last_name=Mikkelsen](http://localhost:8000/hello?first_name=Mads&last_name=Mikkelsen) in your browser.\n',
    'author': 'Vahid Al',
    'author_email': 'thevahidal@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
