from setuptools import setup

setup(
    name='test_blablababa',
    version='0.2',
    description='A fake package',
    author='practiccollie',
    author_email='practiccollie@gmail.com',
    packages=['test_blablababa'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'your-listener-name = test_blablababa:listen',
        ],
    },
)
