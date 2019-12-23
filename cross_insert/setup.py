import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name='cross insert',
	version='1.0.0',
	py_modules=['cross_insert'],
	author='chuanping',
	author_email='2394958302@qq.com',
	url='http://www.baidu.com',
	description='cross insert second list to first list',
	long_description=long_description,
	long_description_content_type='text/markdown',
	packages=setuptools.find_packages(),
	python_requires='>=3.6',
)
