from setuptools import setup
setup(
    name = 'polybar-reload',
    packages = ['polybar-reload'],
    version = '0.1.2',
    description = 'reloads polybar when screen resolution changes',
    author = 'Patrick Motard',
    author_email = 'motard19@gmail.com',
    url = 'https://github.com/patrick-motard/polybar-reload',
    download_url = 'https://github.com/patrick-motard/polybar-reload/archive/0.1.2.tar.gz',
    keywords = ['polybar', 'reload', 'resize', 'resolution'],
    classifiers = [
        'Programming Language :: Python :: 3'
    ],
    scripts = [
        ''
    ],
    install_requires = [
        'Xlib'
    ]
)
