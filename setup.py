from setuptools import setup, find_packages

setup(name='infrabbitmq3',
      version='0.0.1',
      author='Bifer Team',
      description='felix rabbitmq infrastructure components for python3',
      platforms='Linux',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      scripts=['bin/event_processor.py', 'bin/event_publisher.py', 'bin/queue_delete.py', 'bin/queue_unbind.py']
      )
