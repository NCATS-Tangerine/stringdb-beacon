#!/usr/bin/env python3
import connexion
from .encoder import JSONEncoder

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'This is the Translator Knowledge Beacon web service application programming interface (API).  This OpenAPI (\&quot;Swagger\&quot;) document may be used as the input specification into a tool like [Swagger-Codegen](https://github.com/swagger-api/swagger-codegen/blob/master/README.md) to generate client and server code stubs implementing the API, in any one of several supported computer languages and frameworks. In order to customize usage to your web site, you should change the &#39;host&#39; directive below to your hostname. '})
    app.run(host='0.0.0.0')
