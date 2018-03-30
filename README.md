# python_kafka_producer_webservice

Minimal webservice that takes via post some texts and sends it to a kafka topic

Usage example:

curl -X POST \
  http://hostWhereDeployed:8666/ \
  -H 'broker: BrokerHost:Port' \
  -H 'cache-control: no-cache' \
  -H 'postman-token: bb58f13f-8062-2737-e6c9-18d617159b81' \
  -H 'topic: topic_name' \
  -d 'Ah, distinctly I remember it was in the bleak December,
And each separate dying ember wrought its ghost upon the floor.
Eagerly I wished the morrow; — vainly I had tried to borrow
From my books surcease of sorrow — sorrow for the lost Lenore —
For the rare and radiant maiden whom the angels name Lenore —
Nameless here for evermore.
'

