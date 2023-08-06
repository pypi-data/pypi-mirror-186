from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="math_metods",
    version="0.0.3",
    author="Marcio",
    author_email="marcioalexdias@gmail.com",
    description="Esta é a terceira tentativa de disponibilizar os methods",
    long_description=page_description,
    long_description_content_type="text/markdown",
    #url="my_github_repository_project_link"
    packages=find_packages(), # ou posso substituir por ['math_metods'],
    install_requires=requirements,
    python_requires='>=3.8',
)