from setuptools import setup, find_packages

install_requires = [
    "twilio==7.16.1"
]

setup(
    name="textfy",
    version="0.2",
    description="Send text message with Twilio",
    author="JuYoung Oh",
    author_email="juyoung.oh@snu.ac.kr",
    url="https://github.com/ojy0216/textfy",
    license="MIT",
    packages=find_packages(exclude=["test"]),
    python_requires=">=3",
    install_requires=install_requires,
    keywords=["sms", "twilio"]
)

