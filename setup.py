from setuptools import setup, find_packages

setup(
    name='openai_cost_tracker',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'tiktoken==0.5.2',
        'lorem-text==2.1',
        'openai==0.28.0'
    ],
    author='Roy Xie',
    author_email='royx252@gmail.com',
    description='OpenAi Cost Tracker',
    #url='https://github.com/royx252/openai_cost_tracker'
)
