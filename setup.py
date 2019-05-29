from setuptools import setup

setup(name='good_xc_watch',
      version='0.1',
      description='The funniest joke in the world',
      url='http://github.com/boomerang/good_xc_watch',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      scripts=['bin/good_xc_watch'],
      zip_safe=False,
      install_requires=[
          'aerofiles',
	  'pykml'
      ],
)
