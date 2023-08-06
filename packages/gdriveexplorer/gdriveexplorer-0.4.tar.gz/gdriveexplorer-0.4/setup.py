from distutils.core import setup
setup(
  name = 'gdriveexplorer',         # How you named your package folder (MyLib)
  packages = ['gdriveexplorer'],   # Chose the same as "name"
  version = '0.4',      # Start with a small number and increase it with every change you make
  license='GPLv3+',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Class to help managing google drive files',   # Give a short description about your library
  author = 'Sunep',                   # Type in your name
  author_email = 'your.email@domain.com',      # Type in your E-Mail
  url = 'https://github.com/sunep12/gdriveexplorer',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/sunep12/gdriveexplorer/archive/refs/tags/v_04.tar.gz',    # I explain this later on
  keywords = ['GOOGLE DRIVE', 'API', 'WRAPPER'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'PyDrive',
          'google.colab',
          'oauth2client',
          'google-api-python-client',
          'io',
          'pandas',
          'os'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)