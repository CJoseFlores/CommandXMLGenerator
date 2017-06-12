# Generate commands to a Raspberry Pi running SensorBeat.
This program generates XML AND Validates XML using XSD schemas through a _python_ parser.

## API Documentation

### Importing and Constructing a CommandXMLWriter Object
```python
from xmlparsing import xml_generator
xml_writer = xml_generator.CommandXMLWriter(/path/to/your/xsd/file)
# The object is constructed with the .xsd you'd like to validate your .xml with
```

### Creating a Command to send to the Raspberry Pi
```python
xml_writer.create_comand('Enter the command name here')
```

### Returning a string of the generated XML
```python
xml_writer.generate_xml()
```

### Exporting the generated XML to file
```python
xml_writer.export('filename')
```

### Sample output of generated XML file
```xml
<?xml version='1.0' encoding='UTF-8'?>
<pi_com_link>
  <header>
    <source>intern5</source>
    <time_stamp>2017-06-12 19:25:56.465237</time_stamp>
    <signature>HAVE A HASH FUNCTION DO SOMETHING HERE</signature>
    <message_id>1</message_id>
  </header>
  <body>
    <command>take_still</command>
  </body>
</pi_com_link>
```
