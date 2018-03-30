# Kafka Producer Webservice

Minimal webservice that takes via post some texts and sends it to a kafka topic
You need to have access to a Kafka broker.
The setup makes sense in the following scenario:

You have a kafka broker running. You have some application that consumes data
from that broker (e.g. a Spark streamming application). You want to push data
into that broker so that is processed by your application. If this is your
usecase, use this simple webservice to send data to a kafka topic.

Does it do something else? no.
What exactly gets posted? whatever is in the body of the POST call to the
webservices root.

Usage example:

curl -X POST \\
  http://hostWhereDeployed:8666/ \\
  -H 'broker: BrokerHost:Port' \\
  -H 'cache-control: no-cache' \\
  -H 'topic: topic_name' \\
  -d 'Ah, distinctly I remember it was in the bleak December,
And each separate dying ember wrought its ghost upon the floor.
Eagerly I wished the morrow; — vainly I had tried to borrow
From my books surcease of sorrow — sorrow for the lost Lenore —
For the rare and radiant maiden whom the angels name Lenore —
Nameless here for evermore.
'

