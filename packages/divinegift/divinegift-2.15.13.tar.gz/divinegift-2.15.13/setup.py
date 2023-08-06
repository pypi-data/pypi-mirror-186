from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

from divinegift import version

setup(name='divinegift',
      version=version,
      description='Ver.2.15.13. Fix parse_data / parse_json.',
      long_description=long_description,
      long_description_content_type='text/markdown',  # This is important!
      classifiers=[
                   'Development Status :: 5 - Production/Stable',
                   #'Development Status :: 3 - Alpha',
                   'License :: OSI Approved :: MIT License',
                   'License :: OSI Approved :: Apache Software License',
                   'Programming Language :: Python :: 3',
                   "Operating System :: OS Independent",
                   ],
      keywords='',
      url='https://gitlab.com/gng-group/divinegift.git',
      author='Malanris',
      author_email='admin@malanris.ru',
      license='MIT',
      packages=find_packages(),
      install_requires=['requests>=2.23.0', 'deprecation>=2.1.0',
                        'cryptography>=2.9.2', 'pyyaml>=5.1', 'python-dateutil>=2.8.1', 'schedule==1.1.0'],
      include_package_data=True,
      zip_safe=False)
