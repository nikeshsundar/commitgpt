from setuptools import setup, find_packages

setup(
    name="commitgpt-nikesh",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "openai>=1.0.0",
        "pyperclip",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "cmt=commitgpt.cli:main",
        ],
    },
    author="Nikesh Sundar",
    author_email="nikeshsundar@users.noreply.github.com",
    description="AI-powered commit messages, standups and PR descriptions from your git diff",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nikeshsundar/commitgpt",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
