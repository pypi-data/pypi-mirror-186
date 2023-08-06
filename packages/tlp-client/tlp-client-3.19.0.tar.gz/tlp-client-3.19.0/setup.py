import setuptools

def readme():
    with open('README.md') as f:
        return f.read()

def version(micro=None):
    with open("../../../VERSION") as f:
        v = f.read().strip()
    if micro == None:
        return v
    else:
        nv = v.split(".")
        nv[-1] = "%s" % micro
        return ".".join(nv)

setuptools.setup(
    name="tlp-client",
    version=version(),
    author="MLLP-VRAIN",
    author_email="mllp-support@upv.es",
    description="The MLLP-VRAIN's transLectures Platform (TLP) Python3 API client library and tools",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://www.mllp.upv.es",
    project_urls={
        "Documentation (TLP Platform)": "https://ttp.mllp.upv.es/doc",
        "Documentation (library)": "https://ttp.mllp.upv.es/doc/clients/python3",
    },
    packages=["tlp_client"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=['requests', 'requests-toolbelt==0.10.1'],
    scripts=['bin/tlp-api-cli',
             'bin/tlp-player-urlgen',
             'bin/tlp-transedit-urlgen']
)
