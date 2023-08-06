from typing import Any, Dict

from setuptools import setup, find_packages

version: Dict[str, Any] = {}
with open("./arthurai/version.py") as fp:
    exec(fp.read(), version)

setup(
    name='arthurai',
    version=version['__version__'],
    description='Python SDK for ArthurAI',
    url='https://arthur.ai',
    author='ArthurAI',
    author_email='info@arthur.ai',
    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='api arthur ArthurAI sdk',

    packages=find_packages(include=['arthurai*']),
    include_package_data=True,

    install_requires=[
        'dataclasses==0.7;python_version<"3.7"',
        'dataclasses-json==0.4.5',
        'dill>=0.3.1.1,<=0.3.3',
        'docker>=4.2.0,<4.4.0',
        'requests>=2.13.0,<=2.26.0',
        'requests-toolbelt==0.9.1',
        'numpy>=1.16.0,<=1.22.2',
        'pandas>=1.0.0,<=1.4.1',
        'lime~=0.2.0.0',
        'pyarrow>=0.16.0,<=8',
        'python-dateutil>=2.7.0,<2.9',
        'pytz>=2019.1',
        'shap==0.41.0',
        'shortuuid==1.0.1',
        'seaborn>=0.11.1,<=0.11.2'
    ]
)
