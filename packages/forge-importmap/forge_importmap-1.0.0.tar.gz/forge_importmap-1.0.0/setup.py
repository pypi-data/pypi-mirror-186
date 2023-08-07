# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['forgeimportmap', 'forgeimportmap.templatetags']

package_data = \
{'': ['*'], 'forgeimportmap': ['templates/importmap/*']}

install_requires = \
['click',
 'forge-core>=1.0.0,<2.0.0',
 'marshmallow>=3.14.1,<4.0.0',
 'requests',
 'tomli']

entry_points = \
{'console_scripts': ['forge-importmap = forgeimportmap:cli']}

setup_kwargs = {
    'name': 'forge-importmap',
    'version': '1.0.0',
    'description': 'JavaScript import maps for Django',
    'long_description': '# forge-importmap\n\nHeavily inspired by [rails/importmap-rails](https://github.com/rails/importmap-rails),\nthis app adds a simple process for integrating [import maps](https://github.com/WICG/import-maps) into Django.\n\nThis is a new project and it hasn\'t been used in production yet.\nBut if you\'re looking to use import maps with Django, give it a try and tell us how it goes.\nThe structure (and code) is pretty simple.\nContributions are welcome!\n\n## How to use it\n\nYou\'ll need to do four things to use forge-importmap.\n\nThe TL;DR is:\n\n- Add "importmap" to `INSTALLED_APPS`\n- Create an `importmap.toml`\n- Run `python manage.py importmap_generate`\n- Use `{% importmap_scripts %}` in your template\n\n### 1. Install it\n\nDo the equivalent of `pip install forge-importmap` and add it to your `INSTALLED_APPS` list in your `settings.py` file.\n\n```python\n# settings.py\nINSTALLED_APPS = [\n    ...\n    "importmap",\n]\n```\n\n### 2. Create an `importmap.toml` file\n\nThis should live next to your `manage.py` file.\nHere you\'ll add a list of "packages" you want to use.\n\nThe "name" can be anything, but should probably be the same as what it you would import from in typical bundling setups (i.e. `import React from "react"`).\n\nThe "source" will get passed on to the [jspm.org generator](https://jspm.org/docs/api#install), but is basically the `<npm package>@<version>` you want to use.\n\n```toml\n[[packages]]\nname = "react"\nsource = "react@17.0.2"\n```\n\n### 3. Run `importmap_generate`\n\nTo resolve the import map, you\'ll need to run `python manage.py importmap_generate`.\n\nThis will create `importmap.lock` (which you should save and commit to your repo) that contains the actual import map JSON (both for development and production).\n\nYou don\'t need to look at this file yourself, but here is an example of what it will contain:\n\n```json\n{\n  "config_hash": "09d6237cdd891aad07de60f54689d130",\n  "importmap": {\n    "imports": {\n      "react": "https://ga.jspm.io/npm:react@17.0.2/index.js"\n    },\n    "scopes": {\n      "https://ga.jspm.io/": {\n        "object-assign": "https://ga.jspm.io/npm:object-assign@4.1.1/index.js"\n      }\n    }\n  },\n  "importmap_dev": {\n    "imports": {\n      "react": "https://ga.jspm.io/npm:react@17.0.2/dev.index.js"\n    },\n    "scopes": {\n      "https://ga.jspm.io/": {\n        "object-assign": "https://ga.jspm.io/npm:object-assign@4.1.1/index.js"\n      }\n    }\n  }\n}\n```\n\n### 4. Add the scripts to your template\n\nThe import map itself gets added by using `{% load importmap %}` and then `{% importmap_scripts %}` in the head of your HTML. This will include the [es-module-shim](https://github.com/guybedford/es-module-shims).\n\nAfter that, you can include your own JavaScript!\nThis could be inline or from `static`.\nJust be sure to use `type="module"` and the "name" you provided when doing your JS imports (i.e. "react").\n\n```html\n{% load importmap %}\n<!DOCTYPE html>\n<html lang="en">\n<head>\n    {% importmap_scripts %}\n    <script type="module">\n        import React from "react"\n\n        console.log(React);\n    </script>\n</head>\n<body>\n\n</body>\n</html>\n```\n\nWhen it renders you should get something like this:\n\n```html\n<!DOCTYPE html>\n<html lang="en">\n<head>\n    <script async src="https://ga.jspm.io/npm:es-module-shims@1.3.6/dist/es-module-shims.js"></script>\n    <script type="importmap">\n    {\n        "imports": {\n            "react": "https://ga.jspm.io/npm:react@17.0.2/dev.index.js"\n        },\n        "scopes": {\n            "https://ga.jspm.io/": {\n                "object-assign": "https://ga.jspm.io/npm:object-assign@4.1.1/index.js"\n            }\n        }\n    }\n    </script>\n\n    <script type="module">\n        import React from "react"\n\n        console.log(React);\n    </script>\n</head>\n<body>\n\n</body>\n</html>\n```\n\n## Project status\n\nThis is partly an experiment,\nbut honestly it\'s so simple that I don\'t think there can be much wrong with how it works currently.\n\nHere\'s a list of things that would be nice to do (PRs welcome):\n\n- Command to add new importmap dependency (use `^` version automatically?)\n- Django check for comparing lock and config (at deploy time, etc.)\n- Use [deps](https://www.dependencies.io/) to update shim version\n- Preload option\n- Vendoring option (including shim)\n- More complete error handling (custom exceptions, etc.)\n',
    'author': 'Dave Gaeddert',
    'author_email': 'dave.gaeddert@dropseed.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/forgepackages/forge-importmap',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
