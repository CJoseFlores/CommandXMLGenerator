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
Link an example later.
