from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'License :: OSI Approved :: MIT License',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python',
]

setup(
    name='albalacalculator',
    version='0.0.1',
    description='A very basic calculator',
    url='',
    author='Alex Georgiev',
    author_email='aagueorguiev@gmai.com',
    license='MIT',
    classifiers=classifiers,
    keywords='calculator',
    packages=find_packages(),
    install_requirments=[]
)
