from	setuptools	import	setup

setup(
	name='openfrom',
	version='0.0.420',
	py_modules=['openfrom'],
	entry_points={
		'console_scripts': [
			'openfrom=openfrom:main'
		]
	}
)
