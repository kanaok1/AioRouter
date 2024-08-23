from setuptools import setup, find_packages

with open(r"C:\Users\said7\Desktop\bot\AiogramRouterManager\README", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="aiorouter",
    author='@vanya_developer',
    version="0.1.0",
    description="Library to manage aiogram routers more easily.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "aiogram>=3.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)