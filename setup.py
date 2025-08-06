from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="epo-ops-mcp-server",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A server that exposes the European Patent Office's Open Patent Services API as an MCP server using fastMCP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/epo-ops-mcp-server",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.10",
    install_requires=[
        "fastmcp",
        "pydantic",
        "python-epo-ops-client",
        "dogpile.cache",
        "pydantic-settings",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.0",
        ],
        "test": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "responses>=0.20.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "epo-ops-mcp-server=epo_ops_mcp_server.main:main",
        ],
    },
)