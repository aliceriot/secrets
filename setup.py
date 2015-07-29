from setuptools import setup

setup(
        name = 'secrets',
        version = '0.1',
        py_modules = ['secrets', 'notes'],
        test_suite = "tests",
        license = 'GPLv3',
        long_description = open('README.md').read(),
        maintainer = 'Alice Pote',
        maintainer_email = 'alice.writes.wrongs@gmail.com',
        description = 'store your secrets using GPG!',
)
