from setuptools import setup, find_packages

setup(name='lev_mess_client',
      version='0.0.2',
      description='lev_mes_client',
      author='Anton Levochkin',
      author_email='www.garu33@mail.ru',
      packages=find_packages(),
      install_requires=['PyQT5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
