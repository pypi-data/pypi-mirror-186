from setuptools import find_packages, setup


if __name__ == "__main__":
    setup(
        packages=find_packages(),
        package_data={"pontyredis": ["py.typed"]},
        name="pontyredis",
        version="0.2.2",
        license="BSD",
        url="https://github.com/csira/pontyredis",
        description="Redis provider for ponty.",
        install_requires=[
            "aioredis==1.3.1",
            "ponty>=0.2.1",
        ],
        python_requires=">=3.8",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Web Environment",
            "Framework :: AsyncIO",
            "Intended Audience :: Developers",
            "License :: Freely Distributable",
            "License :: OSI Approved :: BSD License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Topic :: Database",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Typing :: Typed",
        ]
    )
