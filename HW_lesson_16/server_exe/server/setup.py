import sys
from cx_Freeze import setup, Executable

build_exe_options = {
      'packages': ['common', 'logs', 'server', 'unit_tests']
}
setup(name='lev_message_server',
      version='0.0.3',
      description='lev_message_server',
      options={
            'build_exe': build_exe_options
      },
      executables=[Executable('server.py',
                              # base='Win32GUI',
                              targetName='server.exe',
                              )]
      )