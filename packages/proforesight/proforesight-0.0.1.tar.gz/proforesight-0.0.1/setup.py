from setuptools import find_packages, setup

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')

except (IOError, ImportError):
    long_description = open('README.md').read()


classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
]

setup(
    name='proforesight',
    version='0.0.1',
    description='Automation of the creation of a machine learning forecaster of company revenues',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Nil-Andreu/proforesight',
    author='Nil Andreu',
    author_email='nilandreug@email.com',
    keywords=[
        'forecasting',
        'forecast',
    ],
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[],
    classifiers=classifiers,
)
