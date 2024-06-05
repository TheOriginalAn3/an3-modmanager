from setuptools import setup, find_packages

setup( 
    name='TOA3-ModManager',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'svmodmanager=toa3_modmanager.cli:cli',
        ],
    },
    author='TheOriginalAn3',
    author_email='andreigubani22+toa3mm@gmail.com',
    description='A simple mod manager for SV mods',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/TheOriginalAn3/an3-modmanager',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)