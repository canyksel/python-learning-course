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

