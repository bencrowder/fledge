from distutils.core import setup

setup(name='fledge',
      version='0.1',
      description='File processing language/shell',
      author='Ben Crowder',
      author_email='ben@bencrowder.net',
      url='http://bencrowder.net/coding/fledge',
      packages=['fledge', 'fledge.actions'],
      data_files=[('/usr/local/bin', ['fl']),
          ]
      )

print("Creating and populating ~/.fledge")

import os
fledge_path = os.path.expanduser('~/.fledge')

# Make ~/.fledge/
if not os.path.exists(fledge_path):
    os.mkdir(fledge_path)

# Make ~/.fledge/fledgerc
if not os.path.exists('%s/fledgerc' % fledge_path):
    f = open('%s/fledgerc' % fledge_path, 'w')
    f.write('')
    f.close()

# Make ~/.fledge/actions/
if not os.path.exists('%s/actions' % fledge_path):
    os.mkdir('%s/actions' % fledge_path)

    # Make ~/.fledge/actions/__init__.py
    f = open('%s/actions/__init__.py' % fledge_path, 'w')
    f.write('')
    f.close()
