from setuptools import setup, find_packages

setup(
    name='resource_manager',
    version='0.0.1',

    url='https://github.com/celaut-project/resource-manager.git',
    author='jossemii',
    author_email='jossemii@proton.me',

    py_modules=['resource_manager'],
    install_requires=[],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.11",
)
