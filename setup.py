from setuptools import find_packages, setup

setup(
    name="depth_anything",
    version="0.1",
    install_requires=["gradio_imageslider", "gradio==4.14.0", "torch", "torchvision", "opencv-python", "huggingface_hub"],
    packages=find_packages(),
)
