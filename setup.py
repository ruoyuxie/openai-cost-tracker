from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='openai_cost_tracker',
    version='0.4',
    packages=find_packages(),
    install_requires=[
        'tiktoken==0.5.2',
        'lorem-text==2.1',
        'openai==0.28.0'
    ],
    author='Roy Xie',
    author_email='royx252@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ruoyuxie/openai-cost-tracker'
)
