"""
py setup.py sdist
twine upload dist/expressmoney-11.1.8.tar.gz
"""
import setuptools

setuptools.setup(
    name='expressmoney',
    packages=setuptools.find_packages(),
    version='11.1.8',
    description='SDK ExpressMoney',
    author='Development team',
    author_email='dev@expressmoney.com',
    install_requires=('requests', 'google-cloud-error-reporting', 'google-cloud-tasks', 'google-cloud-secret-manager'),
    python_requires='>=3.7',
)
