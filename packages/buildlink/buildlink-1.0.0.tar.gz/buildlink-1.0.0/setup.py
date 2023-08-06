import setuptools

with open("README.md", "r") as file:
    readme = file.read()

setuptools.setup(
	name="buildlink",
	version="1.0.0",
	author="Devesh Singh",
	author_email="connect.world12345@gmail.com",
	description="buildlink is a python program which helps you to shorten link with a single command without any registration or using any API Key.Its also provide option to expand any link available on internet on wide range of domain names.",
	long_description=readme,
	long_description_content_type="text/markdown",
	url="https://github.com/TechUX/buildlink",
	license="MIT",
	keywords = "link ",
	classifiers=["License :: OSI Approved :: MIT License",
		    "Operating System :: OS Independent",
		    "Programming Language :: Python"],
	packages=["buildlink"],
	include_package_data=True,
	entry_points ={
		"console_scripts" : [
			"buildlink=buildlink.buildlink:main",
		]
	},
	python_requires='>=2.0',

)
