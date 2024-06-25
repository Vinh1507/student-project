FROM fluent/fluentd:v1.12.0-debian-1.0
USER root
RUN gem install excon -v 0.109.0
RUN gem install faraday -v 2.8.1
RUN gem install faraday-net_http -v 3.0.2
RUN gem uninstall -I elasticsearch
RUN gem install elasticsearch -v 7.14.0
RUN gem install fluent-plugin-elasticsearch -v 5.2.5

USER fluent