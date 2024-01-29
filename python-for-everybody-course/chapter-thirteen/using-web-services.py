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

#Google Geo API example:
'''
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True :
    address = input('Enter a location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    lat = js['results'][0]["geometry"]["location"]["lat"]
    lng = js['results'][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js["results"][0]["formatted_address"]
    print(location)

'''

#API Security and Rate Limiting
'''
* The compute resources to run these APIs are not "free"
* The data provided by these APIs is usually valuable
* The data providers might limit the number of requests per day, demand an API "key" or even charge for usage
* They might change the rules as things progress

#Example:

import urllib.request, urllib.parse, urllib.error
import twurl
import json

TWITTER_URL = 'https://api.twitter.com/l.l/friends/list.json'

while True:
    print('')
    acct  = input('Enter Twitter Acconunt:')
    if(len(acct) < 1) : break
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    print(json.dumps(js, indent=4))
    
    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print('  ', s[:50])


import urllib.request, urllib.parse, urllib.error
import oauth
import hidden

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

def augment(url, parameters):
    secrets = hidden.oauth()
    consumer = oauth.OAuthConsumer(secrets['consumer_key'],
                                   secrets['consumer_secret'])
    token = oauth.OAuthToken(secrets['token_key'], secrets['token_secret'])

    oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer,
                    token=token, http_method='GET', http_url=url,
                    parameters=parameters)
    oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(),
                               consumer, token)
    return oauth_request.to_url()


def test_me():
    print('* Calling Twitter...')
    url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
                  {'screen_name': 'drchuck', 'count': '2'})
    print(url)
    connection = urllib.request.urlopen(url)
    data = connection.read()
    print(data)
    headers = dict(connection.getheaders())
    print(headers)
'''