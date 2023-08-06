# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['qdrant_txtai', 'qdrant_txtai.ann']

package_data = \
{'': ['*']}

install_requires = \
['qdrant-client==0.11.3', 'txtai>=5.0.0,<6.0.0']

setup_kwargs = {
    'name': 'qdrant-txtai',
    'version': '0.11.3',
    'description': 'An integration of Qdrant ANN vector database backend with txtai',
    'long_description': '# qdrant-txtai\n\n[txtai](https://github.com/neuml/txtai) simplifies building AI-powered semantic \nsearch applications using Transformers. It leverages the neural embeddings and\ntheir properties to encode high-dimensional data in a lower-dimensional space \nand allows to find similar objects based on their embeddings\' proximity. \n\nImplementing such application in real-world use cases requires storing the\nembeddings in an efficient way though, namely in a vector database like \n[Qdrant](https://qdrant.tech). It offers not only a powerful engine for neural\nsearch, but also allows setting up a whole cluster if your data does not fit\na single machine anymore. It is production grade and can be launched easily\nwith Docker.\n\nCombining the easiness of txtai with Qdrant\'s performance enables you to build\nproduction-ready semantic search applications way faster than before.\n\n## Installation\n\nThe library might be installed with pip as following:\n\n```bash\npip install qdrant-txtai\n```\n\n## Usage\n\nRunning the txtai application with Qdrant as a vector storage requires launching\na Qdrant instance. That might be done easily with Docker:\n\n```bash\ndocker run -p 6333:6333 -p:6334:6334 qdrant/qdrant:v0.10.2\n```\n\nRunning the txtai application might be done either programmatically or by \nproviding configuration in a YAML file.\n\n### Programmatically\n\n```python\nfrom txtai.embeddings import Embeddings\n\nembeddings = Embeddings({\n    "path": "sentence-transformers/all-MiniLM-L6-v2",\n    "backend": "qdrant_txtai.ann.qdrant.Qdrant",\n})\nembeddings.index([(0, "Correct", None), (1, "Not what we hoped", None)])\nresult = embeddings.search("positive", 1)\nprint(result)\n```\n\n### Via YAML configuration\n\n```yaml\n# app.yml\nembeddings:\n  path: sentence-transformers/all-MiniLM-L6-v2\n  backend: qdrant_txtai.ann.qdrant.Qdrant\n```\n\n```bash\nCONFIG=app.yml uvicorn "txtai.api:app"\ncurl -X GET "http://localhost:8000/search?query=positive"\n```\n\n## Configuration properties\n\n*qdrant-txtai* allows you to configure both the connection details, and some \ninternal properties of the vector collection which may impact both speed and\naccuracy. Please refer to [Qdrant docs](https://qdrant.github.io/qdrant/redoc/index.html#tag/collections/operation/create_collection)\nif you are interested in the meaning of each property.\n\nThe example below presents all the available options:\n\n```yaml\nembeddings:\n  path: sentence-transformers/all-MiniLM-L6-v2\n  backend: qdrant_txtai.ann.qdrant.Qdrant\n  metric: l2 # allowed values: l2 / cosine / ip\n  qdrant:\n    host: qdrant.host\n    port: 6333\n    grpc_port: 6334\n    prefer_grpc: true\n    collection: CustomCollectionName\n    https: true # for Qdrant Cloud\n    api_key: XYZ # for Qdrant Cloud\n    hnsw:\n      m: 8\n      ef_construct: 256\n      full_scan_threshold:\n      ef_search: 512\n```\n',
    'author': 'Kacper Łukawski',
    'author_email': 'kacper.lukawski@qdrant.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
