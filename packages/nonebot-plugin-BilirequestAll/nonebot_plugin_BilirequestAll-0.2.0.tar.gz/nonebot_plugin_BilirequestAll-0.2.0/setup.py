import setuptools
 
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="nonebot_plugin_BilirequestAll",
    version="0.2.0",
    author="Shadow403",
    author_email="anonymous_hax@foxmail.com",
    description="通过B站UID审核入群",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Shadow403/nonebot_plugin_BiliRequestAll.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires =
        [
            'nonebot2 >= 2.0.0b1',
            'nonebot-adapter-onebot >= 2.0.0b1',
            'requests >= 2.2'
        ],
    python_requires = '>=3.8'
)
