#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='vizzy',
    version='0.0.1',
    description='Useful tools to visualize NLP data',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Evan Anthony',
    author_email='anthonyevanm@gmail.com',
    keywords=['EDA', 'visualization', 'NLP'],
    url='https://github.com/eanthony1224',
    download_url='https://pypi.org/project/vizzy/'
)

install_requires = [
   'pandas',
    'matplotlib',
    'numpy',
    'nltk',
    'seaborn',
    'sklearn',
    'gensim',
    'pyldavis',
    'wordcloud',
    'textblob',
    'spacy',
    'textstat'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)

