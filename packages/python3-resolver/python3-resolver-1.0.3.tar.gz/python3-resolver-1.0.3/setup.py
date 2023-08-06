import setuptools

with open('README.md', 'r', encoding='utf-8') as info:
    long_description = info.read()

setuptools.setup(
    name='python3-resolver',
    version='1.0.3',
    author='René Rath',
    author_email='contact@superstes.eu',
    description='Module to resolve A/AAAA DNS records',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/superstes/python3-resolver',
    project_urls={
        'Repository': 'https://github.com/superstes/python3-resolver',
        'Bug Tracker': 'https://github.com/superstes/python3-resolver/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.3'  # ipaddress builtin
)
