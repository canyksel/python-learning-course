#Data on the Web
'''
* With the HTTP Request/Response well understood and well supported, there was a natural move toward exchanging data between programs using these protocols
* We needed to come up with an agreed way to represent data going between applications and across networks
* There are two commonly used formats: XML and JSON

Sending Data across the "Net"
    * PHP -> Array
    * Pyhton -> Dictionary
    * JavaScript -> Object
    * Java HashMap
'''

#XML (eXtensible Markup Language)
'''
* Primary purpose is to help information systems share structured data
* It started as a simplified subset of the Standard Generalized Markup Language(SGML) and is designed to be relatively human-legible

XML Terminology:
* Tags indicate the beginning and ending of elements
* Attributes - Keyword/value pairs on the opening tag of XML
* Serialize / De-Serialize - Convert data in one program into a common format that can be stored and/or transmitted between systems in a programming language-independent manner

XML Basics
* Start Tag
* End Tag
* Text Content
* Attribute
* Self Closing Tag

<person>
 <name>Chuck</name>
 <phone type="intl">
  +1 734 303 4456
 </phone>
 <email hide="yes" />
</person>

* Line ends do not matter. White space is generally discarded on text elements. We indent only to be readable.

XML as Paths
<a>
 <b>X</b>
 <c>
  <d>Y</d>
  <e>Z</e>
 </c>
</a>

/a/b -> X
/a/c/d -> Y
/a/c/e -> Z
'''
#Example-1
import xml.etree.ElementTree as ET

data = '''
<person>
 <name>Chuck</name>
 <phone type="intl">
  +1 734 303 4456
 </phone>
 <email hide="yes" />
</person>
'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

#Example-2
import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Can</name>
        </user>
    </users>
</stuff>
'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count: ', len(lst))

for item in lst :
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))

#XML Schema
'''
* Description of the legal format of an XML document
* Expressed in terms of constraints on the structure and content of documents
* Often used to specify a "contract" between systems - "My system will only accept XML that conforms to this particular Schema."
* If a particular piece of XML meets the specification of the Schema - it is said to "validate"

#Many XML Schema (W3C spec)
* Document Type Definition (DTD)
* Standard Generalized Markup Languaga
* XML Schema from W3C - (XSD)
'''

#XSD Structure
'''
* xs:element
* xs:sequence
* xs:complexType

<person>
    <lastname>Severance</lastname>
    <age>17</age>
    <dateborn>2001-04-17</dateborn>
</person>

<xs:complexType name="person">
    <xs:sequence>
        <xs:element name="lastname" type="xs:string"/>
        <xs:element name="age" type="xs:integer"/>
        <xs:element name="dateborn" type="xs:date"/>
    </xs:sequence>
</xs:complexType>

<xs:element name="full_name" type="xs:string" minOccurs="1" maxOccurs="1" /> -> required

#XSD Data Types
 <xs:element name="customer" type="xs:string" />
 <xs:element name="start" type="xs:date" />
 <xs:element name=""startdate" type="xs:dateTime" />
 <xs:element name="prize" type="xs:decimal" />
 <xs:element name="weeks" type="xs:integer" />
'''