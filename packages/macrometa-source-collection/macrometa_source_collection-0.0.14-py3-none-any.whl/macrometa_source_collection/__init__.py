"""GDN data connector source for GDN Collections."""
from collections import Counter

import pkg_resources
import singer
from c8 import C8Client
from c8connector import C8Connector, Sample, ConfigProperty, ConfigAttributeType, Schema, SchemaAttributeType, \
    SchemaAttribute
from macrometa_source_collection.client import GDNCollectionClient
from singer import utils
from singer.catalog import Catalog, CatalogEntry
from singer.schema import Schema as SingerSchema

LOGGER = singer.get_logger('macrometa_source_collection')

REQUIRED_CONFIG_KEYS = [
    'region',
    'fabric',
    'api_key',
    'source_collection'
]


class GDNCollectionSourceConnector(C8Connector):
    """GDNCollectionSourceConnector's C8Connector impl."""

    def name(self) -> str:
        """Returns the name of the connector."""
        return "collection"

    def package_name(self) -> str:
        """Returns the package name of the connector (i.e. PyPi package name)."""
        return "macrometa-source-collection"

    def version(self) -> str:
        """Returns the version of the connector."""
        return pkg_resources.get_distribution('macrometa_source_collection').version

    def type(self) -> str:
        """Returns the type of the connector."""
        return "source"

    def description(self) -> str:
        """Returns the description of the connector."""
        return "Data connector source for GDN Collections"

    def logo(self) -> str:
        """Returns the logo image for the connector."""
        return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJoAAAAgCAMAAADdcJE2AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXN" \
               "SR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAACQUExURQAAADBAQEBAQDo6Sjg4QDg4SDU1RTU6RTo6QDo6RTg4RDg8RDc9RDY5QzY5" \
               "RjY9Qzk5Rjk9Rjg7Rjg6RTc5RTk5Rzc5RDk5Rzk7RDk7Rzg6Rjg6Rjg8Rjc7Rzk7Rjk6RTk8RTg7RTg7Rzg5Rjg7Rjc6Rjk6Rjc6R" \
               "jg7RTc7Rjk7Rjg6Rjg7Rjc7Rjk7Rjg7Rr/bIT0AAAAvdFJOUwAQEB8gIDAwMDBAQE9QUFBQUF9gb29wcHBwf4CAj4+QkJ+foKCvr7" \
               "C/z8/f3+/vzCRp0QAAA6RJREFUWMPtl2tz4jYUhl8UGVKrTUKVkgQRYB3Iykjm+f//rh9kc8mQtrOz2zKdPV8s2zqHx+cqpJ/y/5V" \
               "6GePWXyGY2QJAnlwdWiTPrHEb9vbKyDzZSJIWxKtz2viwurkuNPbDasWVlULaHkP7sRCsPUk/Y39ELppvxQZ3+eY7da30l4GahMEZ" \
               "M38BLR59+gPQuIxmfPCSWppyfw83Uh28PUUbcGz699BsArLReng7SVmaA/vpKVouyzkHtHFdS9aWLDF1PT5koqlNv8Ec03Nc15Jky" \
               "6XXsZJkfoU/ekP2xOgtWx8J57z3ZL85fkkCeJIky4BWJyBPoZFkI0D2Ug1uCTfSYwfQWEkBbASynUQgT3XQiVYKZQwFqW6B7NMQQW" \
               "lElsaHjzEf+0di37E3khqI4KRHBml6zwO8qoYdcKNl/yiX3y47dh0Ae3PUyfaINj012geVVp67gfOrVsPNgJY9BMlCE8DJJroXI99" \
               "BI0VYG1WbXKkGulUwHnZO1QKiFKBzqhKwNmYNT1KEF6NniMdcS7Aw8ukEraFRGBxV0cqR7TmaInujLVQBnHxv7B4a3Q6mjFRDriS1" \
               "5aI1OIWy+75k7KjXeVWJtRnQPLxIkjui7ciV3g91R5Y2Z2yJLAevv8FCAZzeh+HR0cif1GzdJ+Vg3cGTAowlVZScTjS6hzbGGHfgB" \
               "rQVGA0b+k61q6SEOZ2hZ0M+FVoS2RS0OFRsolHgOHVruDuhKIsA/doPOv6QVke0t7JNigPaO2PJE2WD0WyiwKukbv8BreoAr4L2Vq" \
               "riotfcqddquPsEbeGKmM+9tuJ1PO9wCviKrxolmvGU9gOaAsPFadanyhwajfphYdwRLVImcYTqEtpBZyrptrxwvdHHQ+5WCeBFBS1" \
               "KkwRn/bmgjdo0GdBGCZr6oSl1vob8UM8STwc0B3lW+wiNLqFpDe1DPUvMpQp2D3OjYnQ5NI/l3lar7WpiTEFrZUzl4xenlM/Regng" \
               "pEnpULmjkUZtnzaLA5oW/aOduYx2oiPF0tOLT+j6gIZSizbt9Y5Tt1ezd5JMw+GYFNNJTcxScpKqTUcXq5hWkuRb6KKTbstbSb9sO" \
               "4iLXkWSqpTuirlzHalqIflilDh5Kxu0ITfhS8daCaPIzTPEsOz6xvSPz1jmGw5hf6ezAOgW8qVxv8ongFjpvxfjvDOyiak06vhdct" \
               "4bXYvYecdiGD31Ff0xWALdS38gSsDuatCeU1wcI+i37U4/5XP5E2d/q4LTooGsAAAAAElFTkSuQmCC"

    def validate(self, integration: dict) -> None:
        """Validate given configurations against the connector.
        If invalid, throw an exception with the cause.
        """
        config = self.get_config(integration)
        C8Client(
            "https",
            host=config["region"],
            port=443,
            geofabric=config["fabric"],
            apikey=config["api_key"]
        ).collection(config["source_collection"])
        pass

    def samples(self, integration: dict) -> list[Sample]:
        """Fetch sample data using the given configurations."""
        config = self.get_config(integration)
        schema, data = get_schema_and_data(C8Client(
            "https",
            host=config["region"],
            port=443,
            geofabric=config["fabric"],
            apikey=config["api_key"]
        ), config["source_collection"], 10)
        return [Sample(
            schema=Schema(config["source_collection"],
                          [SchemaAttribute(k, get_attribute_type(v)) for k, v in schema.items()]),
            data=data
        )]

    def schemas(self, integration: dict) -> list[Schema]:
        """Get supported schemas using the given configurations."""
        config = self.get_config(integration)
        schema, _ = get_schema_and_data(C8Client(
            "https",
            host=config["region"],
            port=443,
            geofabric=config["fabric"],
            apikey=config["api_key"]
        ), config["source_collection"], 50)
        return [Schema(config["source_collection"],
                       [SchemaAttribute(k, get_attribute_type(v)) for k, v in schema.items()])]

    def config(self) -> list[ConfigProperty]:
        """Get configuration parameters for the connector."""
        return [
            ConfigProperty('region', 'Region URL', ConfigAttributeType.STRING, True, False,
                           description='Fully qualified region URL.',
                           placeholder_value='api-sample-ap-west.eng.macrometa.io'),
            ConfigProperty('fabric', 'Fabric', ConfigAttributeType.STRING, True, False,
                           description='Fabric name.',
                           default_value='_system'),
            ConfigProperty('api_key', 'API Key', ConfigAttributeType.STRING, True, False,
                           description='API key.',
                           placeholder_value='my_apikey'),
            ConfigProperty('source_collection', 'Source Collection', ConfigAttributeType.STRING, True, True,
                           description='Source collection name.',
                           placeholder_value='my_collection')
        ]

    def capabilities(self) -> list[str]:
        """Return the capabilities[1] of the connector.
        [1] https://docs.meltano.com/contribute/plugins#how-to-test-a-tap
        """
        return ['catalog', 'discover', 'state']

    @staticmethod
    def get_config(integration: dict) -> dict:
        try:
            return {
                # Required config keys
                'region': integration['region'],
                'api_key': integration['api_key'],
                'fabric': integration['fabric'],
                'source_collection': integration['source_collection']
            }
        except KeyError as e:
            raise KeyError(f'Integration property `{e}` not found.')


def get_schema_and_data(client: C8Client, collection: str, sample_size: int):
    cursor = client.execute_query(f"FOR d IN @@collection LIMIT 0, @count RETURN d",
                                  bind_vars={"@collection": collection, "count": sample_size})
    schemas = []
    schema_map = {}
    data_map = {}
    while not cursor.empty():
        rec = cursor.next()
        h = str(hash(rec.keys().__str__()))
        schema_map[h] = rec.keys()
        schemas.append(h)
        if h in data_map:
            data_map[h].append(rec)
        else:
            data_map[h] = [rec]
    schema = {"data": "object"}
    data = []
    if len(schemas) > 0:
        most_common, _ = Counter(schemas).most_common(1)[0]
        schema_keys = schema_map[most_common]
        data = data_map[most_common]
        schema = {
            k: get_singer_data_type(data[0][k]) for k in schema_keys
        }
    return schema, data


def get_singer_data_type(val):
    if type(val) == str:
        return "string"
    elif type(val) == int:
        return "integer"
    elif type(val) == float:
        return "number"
    elif type(val) == bool:
        return "boolean"
    else:
        return "object"


def get_attribute_type(source_type: str) -> SchemaAttributeType:
    if source_type == 'string':
        return SchemaAttributeType.STRING
    elif source_type == 'integer':
        return SchemaAttributeType.LONG
    elif source_type == 'boolean':
        return SchemaAttributeType.BOOLEAN
    elif source_type == 'number':
        return SchemaAttributeType.DOUBLE
    else:
        return SchemaAttributeType.OBJECT


def do_discovery(config):
    collection_name = config['source_collection']
    schema, _ = get_schema_and_data(C8Client(
        "https",
        host=config["region"],
        port=443,
        geofabric=config["fabric"],
        apikey=config["api_key"]
    ), collection_name, 50)
    schema_properties = {k: SingerSchema(type=v, format=None) for k, v in schema.items()}
    # inject `_sdc_deleted_at` prop to the schema.
    schema_properties['_sdc_deleted_at'] = SingerSchema(type=['null', 'string'], format='date-time')
    singer_schema = SingerSchema(type='object', properties=schema_properties)
    catalog = Catalog([CatalogEntry(
        table=collection_name,
        stream=collection_name,
        tap_stream_id=collection_name,
        schema=singer_schema,
        key_properties=["_key"]
    )])
    dump_catalog(catalog)
    return catalog


def dump_catalog(catalog: Catalog):
    catalog.dump()


def do_sync(conn_config, catalog, default_replication_method):
    client = GDNCollectionClient(conn_config)
    client.sync(catalog.streams[0])


def main_impl():
    args = utils.parse_args(REQUIRED_CONFIG_KEYS)
    conn_config = {'api_key': args.config['api_key'],
                   'region': args.config['region'],
                   'fabric': args.config['fabric'],
                   'source_collection': args.config['source_collection']}

    if args.discover:
        do_discovery(conn_config)
    elif args.catalog:
        do_sync(conn_config, args.catalog, args.config.get('default_replication_method'))
    else:
        LOGGER.info("No properties were selected")
    return


def main():
    try:
        main_impl()
    except Exception as exc:
        LOGGER.critical(exc)
