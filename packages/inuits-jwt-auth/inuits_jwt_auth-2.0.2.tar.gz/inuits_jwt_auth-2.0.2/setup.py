from distutils.core import setup

setup(
    author="Inuits",
    author_email="developers@inuits.eu",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ],
    description="A small library to handle JWT auth including roles and permissions",
    install_requires=[
        "Authlib>=1.2.0",
        "cryptography>=39.0.0",
        "Flask>=2.2.2",
        "requests>=2.28.2",
        "Werkzeug>=2.2.2",
    ],
    license="GPLv2",
    name="inuits_jwt_auth",
    packages=["inuits_jwt_auth"],
    provides=["inuits_jwt_auth"],
    version="2.0.2",
)
