from setuptools import find_packages, setup

setup(
    name="depth_anything",
    version="1.0",
    install_requires=[],
    packages=find_packages(exclude="notebooks"),
    extras_require={
        "all": ["matplotlib", "pycocotools", "opencv-python", "onnx", "onnxruntime", "gradio_imageslider", "gradio", "torch", "torchvision", "huggingface_hub"],
        "dev": ["flake8", "isort", "black", "mypy"],
    },
)
