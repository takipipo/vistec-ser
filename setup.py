import setuptools

requirements = [
    "chardet<4.0,>=2.0",
    "torch>=1.7.1",
    "torchvision>=0.8.2",
    "torchtext>=0.8.2",
    "torchaudio>=0.7.2",
    "pytorch-lightning>=1.2.0",
    "pandas>=1.1.5",
    "numpy>=1.26.4",
    "soundfile>=0.10.3",
    "PyYAML!=5.4.*,>=5.1",
    "wget>=3.2",
    "fastapi>=0.63.0",
    "aiofiles>=0.6.0",
    "python-multipart>=0.0.5",
    "uvicorn>=0.13.4",
    "torchmetrics==1.6.0",
]

setuptools.setup(
    name="vistec-ser",
    version="0.4.6a3",
    author="Chompakorn Chaksangchaichot",
    author_email="chompakorn.cc@gmail.com",
    description="Speech Emotion Recognition models and training using PyTorch",
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tann9949/vistec-ser',
    packages=setuptools.find_packages(include=['vistec_ser*']),
    install_requires=requirements,
    classifiers=[
        # "2 - Pre-Alpha", "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires=">=3.6",
)
