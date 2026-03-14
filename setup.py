from setuptools import find_packages, setup

setup(
    name="commitgpt",
    version="0.1.0",
    description="AI-powered git commit message generator",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "openai>=1.0.0",
        "pyperclip",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "cmt=commitgpt.cli:main",
        ]
    },
    python_requires=">=3.9",
)
