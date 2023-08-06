from setuptools import setup, find_packages
from pathlib import Path


with open("README.md", "r", encoding="UTF-8") as f:
     readme = f.read()

setup_args = dict(
    name='weatheril',
    version='0.3.0',
    description='Israel Meteorological Service unofficial python api wrapper',
    long_description_content_type="text/markdown",
    long_description=readme,
    license='MIT',
    packages=find_packages(),
    author='Tomer Klein',
    author_email='tomer.klein@gmail.com',
    keywords=['ims', 'weatheril', 'Israel Meteorological Service','Meteorological Service','weather'],
    url='https://github.com/t0mer/py-weatheril',
    download_url='https://pypi.org/project/weatheril/',
    project_urls={
        "Documentation": "https://github.com/t0mer/py-weatheril",
        "Source": "https://github.com/t0mer/py-weatheril",
    },
    python_requires=">=3.6",
    install_requires=["requests",
                    "pillow",
                    "pandas",
                    "urllib3"],
)



if __name__ == '__main__':
    setup(**setup_args)