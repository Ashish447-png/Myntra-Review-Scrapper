from setuptools import find_packages, setup

setup(
    name="scrapper",
    version="0.0.1",
    author="Ashish",
    author_email="ashishjana065@gmail.com",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4",
        "selenium",
        "flask",
        "flask-cors",
        "gunicorn",
        "plotly",
        "python-dotenv",
        "streamlit",
        "pandas",
        "pymongo",
    ],
)