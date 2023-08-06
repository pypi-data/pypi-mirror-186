# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prometheus_distributed_client']

package_data = \
{'': ['*']}

install_requires = \
['prometheus-client<0.12', 'redis>=2.10.5']

setup_kwargs = {
    'name': 'prometheus-distributed-client',
    'version': '1.2.2',
    'description': '',
    'long_description': "[![Build Status](https://travis-ci.org/dolead/prometheus-distributed-client.svg?branch=master)](https://travis-ci.org/dolead/prometheus-distributed-client)\n[![Code Climate](https://codeclimate.com/github/dolead/prometheus-distributed-client/badges/gpa.svg)](https://codeclimate.com/github/dolead/prometheus-distributed-client)\n[![Coverage Status](https://coveralls.io/repos/github/dolead/prometheus-distributed-client/badge.svg?branch=master)](https://coveralls.io/github/dolead/prometheus-distributed-client?branch=master)\n\n# Prometheus Distributed Client\n\n### Purpose and principle\n\n```prometheus-distributed-client``` is aimed at shorted lived process that can expose [Prometheus](https://prometheus.io/) metrics through HTTP.\n\n### Advantages over Pushgateway\n\nThe prometheus project provides several ways of publishing metrics. Either you publish them directly like the [official client](https://github.com/prometheus/client_python) allows you to do, or you push them to a [pushgateway](https://github.com/prometheus/pushgateway).\n\nThe first method implies you've got to keep your metrics in-memory and publishs them over http.\nThe second method implies that you'll either have a pushgateway per process or split your metrics over all your processes to avoid overwriting your existing pushed metrics.\n\n```prometheus-distributed-client``` allows you to have your short lived process push metrics to a database and have another process serving them over HTTP. One of the perks of that approach is that you keep consistency over concurrent calls. (Making multiple counter increment from multiple process will be acknowledge correctly by the database).\n\n### Code examples\n\n```prometheus-distributed-client``` uses the base of the [official client](https://github.com/prometheus/client_python) but replaces all write and read operation by database call.\n\n#### Declaring and using metrics\n\n```python\nfrom prometheus-distributed-client import set_redis_conn, Counter, Gauge\n# we use the official clients internal architecture\nfrom prometheus_client import CollectorRegistry\n\n# set your own registry\nREGISTRY = CollectorRegistry()\n# declare metrics from prometheus-distributed-client\nCOUNTER = Counter('counter_metric_name', 'metric documentation',\n                  [labels], registry=REGISTRY)\nGAUGE = Gauge('gauge_metric_name', 'metric documentation',\n                  [labels], registry=REGISTRY)\n\n# increment a counter and set a value for a gauge\nCOUNTER.labels('label_value').inc()\nGAUGE.labels('other_label_value').set(12)\n```\n\n### Serving the metrics\n\n```prometheus-distributed-client``` use the registry system from the official client and is de facto compatible with it. If you want to register regular metrics alongside the one from ```prometheus-distributed-client``` it is totally feasible.\nHere is a little example of how to serv metrics from ```prometheus-distributed-client```, but you can also refer to the [documentation of the official client](https://github.com/prometheus/client_python#exporting).\n\n```python\n# with flask\n\nfrom flask import Flask\nfrom prometheus_client import generate_latest\n# get the registry you declared your metrics in\nfrom metrics import REGISTRY\n\napp = Flask()\n\n@app.route('/metrics')\ndef metrics():\n    return generate_latest(REGISTRY)\n```\n",
    'author': 'François Schmidts',
    'author_email': 'francois@schmidts.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
