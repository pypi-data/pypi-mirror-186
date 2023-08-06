from distutils.core import setup

DEPTH = 20

setup(
    name='web-foundation',  # How you named your package folder (MyLib)
    packages=['web_foundation'],  # Chose the same as "name"
    package_data={
        'web_foundation': [('*/' * i).rstrip("/") for i in range(1, DEPTH)],
    },
    version='0.2.45',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Python microprocessors web-foundation',  # Give a short description about your library
    author='Yaroha',  # Type in your name
    author_email='yaroher2442@gmail.com',  # Type in your E-Mail
    keywords=['SOME', 'MEANINGFULL', 'KEYWORDS'],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        "sanic==22.9.1",
        "sanic-ext==22.9.1",
        "tortoise-orm==0.19.1",
        "asyncpg==0.26.0",
        "pydantic==1.10.2",
        "orjson==3.8.0",
        "apscheduler==3.9.1",
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
    ],
    extras_require={
        "aerich": ["aerich==0.7.3"],
        "prometheus": ["prometheus-client==0.14.1"],
    }
)
