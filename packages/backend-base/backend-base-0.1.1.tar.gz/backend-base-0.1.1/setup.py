import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="backend-base",
    version="0.1.1",
    author="Carlos Osuna",
    author_email="carlosalvaroosuna1@gmail.com",
    description="Backend base package based of some django modules",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Carlososuna11/backend-base",
    project_urls={
        "Bug Tracker": "https://github.com/Carlososuna11/backend-base/issues",
        "repository": "https://github.com/Carlososuna11/backend-base"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8"
)
