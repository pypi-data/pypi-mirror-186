import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='rabbitmqsimple',
    version='0.4',
    author='Vikash Jain',
    author_email='vikash.jain@galaxyweblinks.co.in',
    description='A library to use RabbitMQ Package for multi-tenant application',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/vcjain/rabbitmq-simple',
    project_urls = {
        "Bug Tracker": "https://github.com/vcjain/rabbitmq-simple/issues"
    },
    license='MIT',
    packages=['rabbitmqsimple'],
    install_requires=['rabbitmqpy', 'rabbitpy'],
)
