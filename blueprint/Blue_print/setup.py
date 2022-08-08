import configparser

from setuptools import setup

config = configparser.ConfigParser()
config.read('setup.cfg')

setup(name=config['application']['package'], packages=[config['application']['package']], version=config['application']['version'], description='Just to test the blue print structure out there', python_requires=config['application']['python'], author=config['application']['author'], author_email=config['application']['email'], maintainer=config['application']['author'], maintainer_email=config['application']['email'], license='MIT', entry_points={'console_scripts': [f"awesome-project-cli={config['application']['package']}.commands.cmd:main"]})
