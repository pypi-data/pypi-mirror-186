from setuptools import setup, find_packages

readme = "Some README"
license = "Some License"
version = "0.0.3"

setup(
    name='serenity-module-root-cause-finder',
    version=version,
    url='https://soemthing.hehe',
    author='Noone',
    author_email='someoneelse@nonaaaae.com',
    description='A schema and validator for YAML.',
    long_description=readme,
    long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
