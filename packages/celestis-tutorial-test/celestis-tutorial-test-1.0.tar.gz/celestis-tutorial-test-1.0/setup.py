from setuptools import setup

setup(
    name="celestis-tutorial-test",
    version="1.0",
    description="A simple backend framework built using python",
    author="Aryaan Hegde",
    author_email="aryhegde@gmail.com",
    # packages=["celestis.controller", "celestis.model", "celestis.view"]
    # package_dir={"celestis.controller": "controller", "celestis.view": "view", "celestis.model": "model"},
    py_modules=["command", "create_files"],
    include_package_data=True,
    install_requires=['requests', 'click'],
    entry_points={
        "console_scripts": [
            "celestis=command:celestis"
        ]
    }
)