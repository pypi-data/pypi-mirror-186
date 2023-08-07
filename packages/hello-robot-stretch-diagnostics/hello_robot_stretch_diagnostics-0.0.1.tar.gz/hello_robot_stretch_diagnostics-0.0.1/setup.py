import setuptools
from os import listdir
from os.path import isfile, join

scripts=set()
script_paths=['./tools']
for script_path in script_paths:
    scripts=scripts.union({script_path+'/'+f for f in listdir(script_path) if isfile(join(script_path, f))})

setuptools.setup(
    name="hello_robot_stretch_diagnostics",
    version="0.0.1",
    author="Hello Robot Inc.",
    author_email="support@hello-robot.com",
    description="Stretch Diagnostics",
    long_description="Stretch Diagnostics",
    long_description_content_type="text/markdown",
    url="https://github.com/hello-robot/diagnostics",
    scripts = scripts,
    packages=['stretch_diagnostics'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    install_requires=['hello-robot-stretch-factory>=0.3.12','hello-robot-stretch-body>=0.4.14']
)
