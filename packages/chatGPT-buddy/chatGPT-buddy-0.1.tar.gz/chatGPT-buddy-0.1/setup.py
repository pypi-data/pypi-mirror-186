from setuptools import setup, find_packages

setup(
    name='chatGPT-buddy',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'SpeechRecognition',
        'Pyaudio',
        'gTTS',
        'transformers',
        'torch'
    ],
    author='Khaled Achech',
    author_email='achechkhaled@gmail.com',
    description='A voice command tool that uses ChatGPT as NLU',
)
