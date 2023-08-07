# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['forgetailwind']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.0', 'forge-core>=1.0.0,<2.0.0', 'requests>=2.0.0']

entry_points = \
{'console_scripts': ['forge-tailwind = forgetailwind:cli']}

setup_kwargs = {
    'name': 'forge-tailwind',
    'version': '1.0.0',
    'description': 'Work library for Forge',
    'long_description': '# forge-tailwind\n\nUse [Tailwind CSS](https://tailwindcss.com/) with [Django](https://www.djangoproject.com/) *without* requiring JavaScript or npm.\n\nMade possible by the [Tailwind standalone CLI](https://tailwindcss.com/blog/standalone-cli).\n\n```console\n$ forge tailwind\nUsage: forge tailwind [OPTIONS] COMMAND [ARGS]...\n\n  Tailwind CSS\n\nOptions:\n  --help  Show this message and exit.\n\nCommands:\n  compile  Compile a Tailwind CSS file\n  init     Install Tailwind, create a tailwind.config.js...\n  update   Update the Tailwind CSS version\n```\n\n## Installation\n\nFirst, install `forge-tailwind` from [PyPI](https://pypi.org/project/forge-tailwind/):\n\n```sh\npip install forge-tailwind\n```\n\nCreate a new `tailwind.config.js` file in your project root:\n\n```sh\nforge tailwind init\n```\n\nThis will also create a `tailwind.css` file at `static/src/tailwind.css` where additional CSS can be added.\nYou can customize where these files are located if you need to,\nbut this is the default (requires `STATICFILES_DIRS = [BASE_DIR / "static"]`).\n\nThe `src/tailwind.css` file is then compiled into `dist/tailwind.css` by running `tailwind compile`:\n\n```sh\nforge tailwind compile\n```\n\nWhen you\'re working locally, add `--watch` to automatically compile as changes are made:\n\n```sh\nforge tailwind compile --watch\n```\n\nThen include the compiled CSS in your base template `<head>`:\n\n```html\n<link rel="stylesheet" href="{% static \'dist/tailwind.css\' %}">\n```\n\nIn your repo you will notice a new `.forge` directory that contains `tailwind` (the standalone CLI binary) and `tailwind.version` (to track the version currently installed).\nYou should add `.forge` to your `.gitignore` file.\n\n## Updating Tailwind\n\nThis package manages the Tailwind versioning by comparing `.forge/tailwind.version` to the `FORGE_TAILWIND_VERSION` variable that is injected into your `tailwind.config.js` file.\n\n```js\nconst FORGE_TAILWIND_VERSION = "3.0.24"\n\nmodule.exports = {\n  theme: {\n    extend: {},\n  },\n  plugins: [\n    require("@tailwindcss/forms"),\n  ],\n}\n```\n\nWhen you run `tailwind compile`,\nit will automatically check whether your local installation needs to be updated and will update it if necessary.\n\nYou can use the `update` command to update your project to the latest version of Tailwind:\n\n```sh\ntailwind update\n```\n\n## Adding custom CSS\n\nIf you need to actually write some CSS,\nit should be done in `app/static/src/tailwind.css`.\n\n```css\n@tailwind base;\n\n\n@tailwind components;\n\n/* Add your own "components" here */\n.btn {\n    @apply bg-blue-500 hover:bg-blue-700 text-white;\n}\n\n@tailwind utilities;\n\n/* Add your own "utilities" here */\n.bg-pattern-stars {\n    background-image: url("/static/images/stars.png");\n}\n\n```\n\n[Read the Tailwind docs for more about using custom styles →](https://tailwindcss.com/docs/adding-custom-styles)\n\n## Deployment\n\nIf possible, you should add `static/dist/tailwind.css` to your `.gitignore` and run the `forge tailwind compile --minify` command as a part of your deployment pipeline.\n\nWhen you run `forge tailwind compile`, it will automatically check whether the Tailwind standalone CLI has been installed, and install it if it isn\'t.\n\nWhen using Forge on Heroku, we do this for you automatically in our [Forge buildpack](https://github.com/forgepackages/heroku-buildpack-forge/blob/master/bin/files/post_compile).\n',
    'author': 'Dave Gaeddert',
    'author_email': 'dave.gaeddert@dropseed.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.forgepackages.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
