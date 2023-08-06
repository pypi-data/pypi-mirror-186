from setuptools import setup

APP_NAME = "djangobuk_envsettings"

setup(
    name=APP_NAME,
    zip_safe=False,
    version="0.3.0",
    include_package_data=True,
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    packages=[APP_NAME],
    python_requires=">=3.8",
    url="https://github.com/bukdjango/envsettings",
    install_requires=["django>=3.0.8"],
)
