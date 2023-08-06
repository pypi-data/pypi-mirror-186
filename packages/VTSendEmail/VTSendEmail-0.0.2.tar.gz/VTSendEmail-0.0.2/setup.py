from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'VTSendEmail',
    version = '0.0.2',
    author = 'Vijay Thoart',
    author_email = 'vijaythorat0804@gmail.com',
    license = 'MIT License',
    description = 'Used to send email',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    # url = '<github url where the tool code will remain>',
    py_modules = ['Email'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        sendmail=Email:cli
    '''
)