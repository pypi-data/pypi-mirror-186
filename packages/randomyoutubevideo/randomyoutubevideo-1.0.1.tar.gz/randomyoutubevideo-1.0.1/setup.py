from setuptools import setup, find_packages

setup(
    name='randomyoutubevideo',
    version='1.0.1',
    author='emresvd',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4==4.11.1',
        'requests==2.28.1',
        'youtube-search==1.1.1',
        'youtube-search-python==1.4.2',
    ],
    keywords=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)