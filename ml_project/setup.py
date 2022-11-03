from setuptools import find_packages, setup


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name="src",
    packages=find_packages(),
    version="0.1.0",
    description="Homeworks for the course 'ML in production' from VK Education (Technopark)",
    author="Your name (or your organization/company/team)",
    entry_points={
        "console_scripts": [
            "ml_example_train = src.train_pipeline:train_pipeline_command"
        ]
    },
    install_requires=required,
    license="MIT",
)
