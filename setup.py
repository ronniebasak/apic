from setuptools import setup, find_packages

setup(
    name='apic',
    version='0.1',
    packages=find_packages(),
    url='http://github.com/ronniebasak/apic',
    license='MIT',
    author='Sohan Basak',
    author_email='ronnie.basak96@gmail.com',
    description='A short description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        # add your project dependencies here
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)