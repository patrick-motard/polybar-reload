from setuptools import setup

with open('README.md') as f:
    long_description = f.read()
setup(
    name = 'polybar-reload',
    packages = ['polybar-reload'],
    long_description = long_description,
    version = '0.1.6',
    description = 'reloads polybar when screen resolution changes',
    long_description_content_type = 'text/markdown',
    author = 'Patrick Motard',
    author_email = 'motard19@gmail.com',
    url = 'https://github.com/patrick-motard/polybar-reload',
    download_url = 'https://github.com/patrick-motard/polybar-reload/archive/0.1.6.tar.gz',
    keywords = ['polybar', 'reload', 'resize', 'resolution'],
    classifiers = [
        'Programming Language :: Python :: 3'
    ],
    scripts = [
        'bin/polybar-reload'
    ],
    install_requires = [
        'Xlib'
    ]
)
