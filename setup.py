from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as readme:
    long_description = readme.read()

setup(
    name='tsugu-api-python',
    version='1.5.9',
    author='WindowsSov8',
    author_email='qwertyuiop2333@hotmail.com',
    description='Tsugu BanGDream Bot 的功能 API 统合包',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/WindowsSov8forUs/tsugu-api-python',
    include_package_data=False,
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.8',
    install_requires=[
        'typing_extensions>=4.5.0',
    ],
    extras_require={
        'httpx': [
            'httpx>=0.22.0',
        ],
        'aiohttp': [
            'aiohttp>=3.8.1',
        ],
    },
)