from setuptools import setup

setup(
    name='clemoni_utilities',
    version='1.3.1',
    url='https://github.com/clemoni/clemoni_utilities',
    author='Clement Liscoet',
    author_email='clement.liscoet@gmail.com',
    license='MIT',
    description='A short utility library for Python',
    long_description="""Provide helper functions""",
    packages=['utilities'],
    install_requires=['SQLAlchemy',
                      'mysql-connector-python', 
                      'pymysql',
                      'pyyaml'                  
                      ],
    py_modules=['add_package', 'branching_funcs', 'db_funcs', 'files_system_funcs', 'fp_funcs', 'utils_funcs', 
    'logs_handler', 'ui_funcs', 'yml_funcs']
)