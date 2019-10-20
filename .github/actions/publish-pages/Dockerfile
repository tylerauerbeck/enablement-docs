FROM registry.access.redhat.com/ubi8/python-36 bash

RUN pip install requests jmespath

COPY publish.py /publish.py

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
