from setuptools import setup

with open("./README.rst",'r') as f:
	data= f.read()


setup(name='hackebds',
      version='0.3.2',
      description='This tool is used for backdoor and shellcode generation for various architecture devices',
      long_description_content_type="text/markdown",
      long_description=data,
      url='https://github.com/doudoudedi/hackEmbedded',
      author='doudoudedi',
      author_email='doudoudedi233@gmail.com',
      license='GPL-3.0',
      install_requires=[
      'pwn',
      'requests',
      'colorama',
      'mako',
      'pygments',
      'multidict'
      ],
      python_requires='>=3',
      py_modules=['hackebds.arm','hackebds.mips',"hackebds.aarch64","hackebds.extract_shellcode",'hackebds.model_choise','hackebds.cve_info','hackebds.powerpc_info','hackebds.ESH','hackebds.sparc32','hackebds.sparc64','hackebds.my_package','hackebds.backdoor_encode','hackebds.hackebds_cmd','hackebds.power_reverse_shell','hackebds.power_bind_shell'],
      data_files=["README.md"],
      entry_points={
      'console_scripts': [
      'hackebds = hackebds:main',
    ]
  },
)

