# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['np_workflows',
 'np_workflows.experiments',
 'np_workflows.services',
 'np_workflows.workflows',
 'np_workflows.workflows.behavior',
 'np_workflows.workflows.dynamic_routing',
 'np_workflows.workflows.passive']

package_data = \
{'': ['*'],
 'np_workflows': ['resources/config/*', 'resources/images/*'],
 'np_workflows.workflows': ['passive_old/*']}

install_requires = \
['backoff',
 'fabric>=2.7.1,<3.0.0',
 'gevent==21.1.2',
 'greenlet==1.1.2',
 'np_config',
 'np_logging',
 'np_session',
 'pyzmq>=19.0,<20.0',
 'requests',
 'zope-event==4.5.0',
 'zope-interface==5.3.0']

extras_require = \
{'dev': ['pip-tools', 'isort', 'mypy', 'black', 'pytest', 'poetry']}

setup_kwargs = {
    'name': 'np-workflows',
    'version': '0.0.1a1',
    'description': 'Ecephys and behavior workflows for the Mindscope Neuropixels team.',
    'long_description': "# services\n![Services](./services.drawio.svg)\n\n# requirements \n\n**graphviz**\n    \n- 64bit .exe: https://gitlab.com/api/v4/projects/4207231/packages/generic/graphviz-releases/3.0.0/windows_10_cmake_Release_graphviz-install-3.0.0-win64.exe\n\n- homepage: https://graphviz.org/download/\n\n- install and choose option to add to path\n\n**router**\n\n- download: http://aibspi2/release/router/latest/\n\n- unzip to `C:\\Program Files\\AIBS_MPE\\router\\`\n\n- `router.exe` must be started before `workflow_launcher.exe` (router can be left running if launcher restarted)\n\n**workflow_launcher**\n\n- download: http://aibspi2/release/workflow_toolkit/latest/\n\n- unzip to `C:\\Program Files\\AIBS_MPE\\workflow_launcher\\` \n\n## installation \n\nrun `install.bat` \n\nlaunch `C:\\Program Files\\AIBS_MPE\\workflow_launcher\\workflow_launcher.exe`\n\n# notes\n\n- if 'C:\\ProgramData\\AIBS_MPE\\wfltk\\workflows\\' can't be reached, try running `workflow_launcher` as admin\n\n- TextValue error displayed in WSE GUI cmay indicate an accidental capitalization, ie `type: Note` should be `type: note`",
    'author': 'Ben Hardcastle',
    'author_email': 'ben.hardcastle@alleninstitute.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
