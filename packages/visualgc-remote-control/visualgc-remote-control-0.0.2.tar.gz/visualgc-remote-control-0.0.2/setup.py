from setuptools import setup

setup(
    name="visualgc-remote-control",
    license='Apache v2',
    packages=["visualgc_remote_control",
              "visualgc_remote_control.au3_scripts"],  # this must be the same as the name above
    version="0.0.2",
    description="visualgc-remote-control",
    author="Luis Coelho",
    author_email="luis.coelho.720813@gmail.com",
    url='https://luism.co',
    keywords=["VisualGC", "Configuration", "REST"],  # arbitrary keywords
    data_files=[
        ("/etc/schindler", ["visualgc-remote-control.yaml"]),
    ],
    install_requires=[
        'Flask>=2.2.2',

    ],
    entry_points={
        "console_scripts": ["visualgc-remote-control=visualgc_remote_control.visualgc_remote_control:VisualgcRemoteControl.main"],
    },
)
