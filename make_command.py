from xmlparsing import xml_generator

# Create a PhoneStoreXMLWriter object.
xml_writer = xml_generator.CommandXMLWriter('/home/cflores/eclipse/workspace/SensorBeatXML/xmlparsing/server_command.xsd')

# Adding phones to the phone store.
user_input = raw_input('Would you like to send a command to the Pi? (y/n)')
if user_input == 'y':
    command = raw_input('Enter the command you\'d like to send to the Pi: ')
    xml_writer.create_command(command)
else :
    print 'Have a good day!'

# Printing the generated XML to console.
print xml_writer.generate_xml()

print "\n"
print xml_writer.validate()
