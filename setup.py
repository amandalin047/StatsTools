import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='statstools',
    version='0.0.3',
    author='Amanda Lin',
    author_email='amanda.lin0103@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/amandalin047/StatsTools',
    project_urls = {
        'Project_Urls': 'https://github.com/amandalin047/StatsTools'
    },
    license='MIT',
    packages=['statstools'],
    install_requires=['statsmodels'],
)
