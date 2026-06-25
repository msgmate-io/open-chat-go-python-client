from setuptools import setup, find_packages
# pip install git+https://github.com/msgmate-io/open-chat-go-python-client.git

setup(
    name="open_chat_client_python",
    version="0.1",
    packages=find_packages(),
    python_requires=">=3.10, <4",
    install_requires=[
        "attrs>=22.2.0",
        "httpx>=0.28,<0.29",
        "requests",
        "websocket-client",
    ],
    entry_points={
        "console_scripts": [
            "open_chat_client_python=client.client:main",
            "oc_client=client.client:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
