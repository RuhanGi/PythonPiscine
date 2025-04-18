from setuptools import setup, find_packages


def main():
    setup(
        name='ft_package',
        version='0.0.1',
        description='A sample test package',
        author='mgoltay',
        author_email='mgoltay@student.42abudhabi.ae',
        url='https://github.com/RuhanGi/PythonPiscine/\
0-Starting/ex_09/ft_package',
        packages=find_packages(),
        entry_points={
            'console_scripts': [],
        },
    )


if __name__ == "__main__":
    main()
