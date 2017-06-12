from lxml import etree as et
from StringIO import StringIO
import datetime
import socket

class CommandXMLWriter:
    # Create a Command to send to the Pi.
    def __init__(self, filename):
        self.__root = et.Element('pi_com_link') # Root element representing a communication link to the Raspberry Pi
        self.__command_schema = self.import_schema(filename)
        self.__message_id = 1

    # Generate an XML document which requests an image from the Raspberry Pi.
    def create_command(self, command_name):
        self.create_header()
        self.create_body(command_name)
        self.generate_xml()

    # Create a header for the command/response.
    def create_header(self):
        # Create the header complexType.
        header = et.SubElement(self.__root, 'header')

        # Generating the simple types that describe the header
        source = et.SubElement(header, 'source')
        source.text = socket.gethostname()
        time_stamp = et.SubElement(header, 'time_stamp')
        time_stamp.text = str(datetime.datetime.utcnow())

        # The signature is used for data integrity (checksum).
        signature = et.SubElement(header, 'signature')
        signature.text = 'HAVE A HASH FUNCTION DO SOMETHING HERE'

        # Message ID is used to keep track of the current message number.
        message_id = et.SubElement(header, 'message_id')
        message_id.text = str(self.__message_id)

        # Increment the message id.
        self.__message_id += 1

    # Create a body for the command.
    def create_body(self, command_name):
        # Create the body complexType.
        body = et.SubElement(self.__root, 'body')

        # Parse the specified command to the body.
        command = et.SubElement(body, 'command')
        command.text = command_name 

    # Import XML Schema file and return an XMLSchema validator.
    def import_schema(self, filename):
        # Open XML Schema and parse it to an Element tree object.
        f = open(filename, 'r')
        xmlschema_doc = et.parse(f)

        # Create an XMLSchema validator from the ET object, and close file.
        xmlschema = et.XMLSchema(xmlschema_doc)
        f.close()

        return xmlschema

    # Validate an XML file against a schema, and return a boolean.
    def validate(self):

        # Generate XML and parse to Element Tree object.
        raw_xml = StringIO(self.generate_xml())
        xml_doc = et.parse(raw_xml)

        # Parse generated XML into XSD Validator.
        return self.__command_schema.validate(xml_doc)

    # Return the generated XML.
    def generate_xml(self):
        return et.tostring(self.__root, pretty_print=True, xml_declaration=True, encoding='UTF-8')

    # Export the generated XML to a file.
    def export(self, file_name):
        f = open(file_name, 'w')
        f.write(self.generate_xml())
        f.close()
