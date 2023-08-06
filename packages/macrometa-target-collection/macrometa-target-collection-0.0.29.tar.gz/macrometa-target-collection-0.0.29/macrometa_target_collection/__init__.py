"""GDN data connector target for Macrometa GDN collections."""
import pkg_resources
from c8connector import C8Connector, Sample, ConfigAttributeType, Schema
from c8connector import ConfigProperty


class GDNCollectionTargetConnector(C8Connector):
    """GDNCollectionTargetConnector's C8Connector impl."""

    def name(self) -> str:
        """Returns the name of the connector."""
        return "collection"

    def package_name(self) -> str:
        """Returns the package name of the connector (i.e. PyPi package name)."""
        return "macrometa-target-collection"

    def version(self) -> str:
        """Returns the version of the connector."""
        return pkg_resources.get_distribution('macrometa_target_collection').version

    def type(self) -> str:
        """Returns the type of the connector."""
        return "target"

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
        pass

    def samples(self, integration: dict) -> list[Sample]:
        """Fetch sample data using the given configurations."""
        return []

    def schemas(self, integration: dict) -> list[Schema]:
        """Get supported schemas using the given configurations."""
        return []

    def config(self) -> list[ConfigProperty]:
        """Get configuration parameters for the connector."""
        return [
            ConfigProperty('region', 'Region URL', ConfigAttributeType.STRING, True, False,
                           description="Fully qualified region URL.",
                           placeholder_value='api-sample-ap-west.eng.macrometa.io'),
            ConfigProperty('api_key', 'API Key', ConfigAttributeType.STRING, True, False,
                           description="API key.",
                           placeholder_value='my_apikey'),
            ConfigProperty('fabric', 'Fabric', ConfigAttributeType.STRING, True, False,
                           description="Fabric name.",
                           default_value='_system'),
            ConfigProperty('target_collection', 'Target Collection', ConfigAttributeType.STRING, True, True,
                           description="Target collection name.",
                           placeholder_value='my_collection'),
            ConfigProperty('batch_size_rows', 'Batch Size', ConfigAttributeType.INT, False, False,
                           description='Maximum number of rows inserted per batch.',
                           default_value='50'),
            ConfigProperty('batch_flush_interval', 'Batch Flush Interval (Seconds)',
                           ConfigAttributeType.INT, False, False,
                           description='Time between batch flush executions.',
                           default_value='60'),
            ConfigProperty('batch_flush_min_time_gap', 'Batch Flush Minimum Time Gap (Seconds)',
                           ConfigAttributeType.INT, False, False,
                           description='Minimum time gap between two batch flush tasks.',
                           default_value='60'),
        ]

    def capabilities(self) -> list[str]:
        """Return the capabilities[1] of the connector.
        [1] https://docs.meltano.com/contribute/plugins#how-to-test-a-tap
        """
        return []
