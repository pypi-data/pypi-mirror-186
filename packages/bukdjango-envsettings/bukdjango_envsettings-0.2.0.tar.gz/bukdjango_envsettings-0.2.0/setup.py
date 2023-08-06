from setuptools import setup

APP_NAME = "bukdjango_envsettings"

setup(
    name=APP_NAME,
    zip_safe=False,
    version="0.2.0",
    include_package_data=True,
    packages=[APP_NAME],
    python_requires=">=3.8",
    url="https://github.com/bukdjango/envsettings",
    install_requires=["django>=3.0.8"],
)
