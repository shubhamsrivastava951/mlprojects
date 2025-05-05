from setuptools import setup, find_packages

def get_requirements(file_path):
    with open(file_path) as file:
        lines = file.readlines()
        return [line.strip() for line in lines if line.strip() and not line.startswith('#') and line.strip() != '-e .']

setup(
    name="mlprojects",
    version="0.0.1",
    author="Shubham Srivastava",
    author_email="shubhamsrivastava951@gmail.com",
    description="ML Projects",
    long_description="Various machine learning projects including preprocessing and model training.",
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements('requirements.txt'),
    python_requires='>=3.6',
)
