#Transport Control Protocol (TCP)
'''
* Built on top of IP (Internet Protocol)
* Assumes IP might lose some data-stores and retransmits data if it seems to be lost
* Handles "flow control" using a transmit window
* Provides a nice reliable pipe
'''

#TCP Connections / Sockets
'''
* In computer networking, an Internet socket or network socket is an endpoint of a bidirectional inter-process communication flow across an Internet Protocol-based computer network, such as the Internet.
'''

#TCP Port Numbers
'''
* A port is an application-specific or process-specific software communications endpoint
* It allows multiple networked applications to coexist on the same server
* There is a list of well-known TCP port numbers
    * Incoming E-Mail -> 25
    * Login -> 23
    * Web Server -> 80, 443
    * Personal Mail Box -> 109, 110
'''

#Common TCP Ports
'''
* Telnet (23) - Login        * IMAP (143/220/993) - Mail Retrieval
* SSH (22) - Secure login    * POP (109/110) - Mail Retrieval
* HTTP (80)                  * DNS (53) - Domain Name
* HTTPS (443) - Secure       * FTP (21) - File Transfer
* SMTP (25) - Mail
'''

#Sockets in Python
'''
* Python has built-in support for TCP Sockets

#Example:
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
'''

#Application Protocols
'''
* Since TCP(and Python) gives us a reliable socket, what do we want to do with the socket? What problem do we want to solve?
* Applicaiton Protocols
    * Mail
    * World Wide Web
'''

#HTTP - Hypertext Transfer Protocol
'''
* The dominant Application Layer Protocol on the Internet
* Invented for the Web-to Retrieve HTML, Images, Documents, etc
* Extended to be data in addition to documents - RSS, Web Services etc.. 
    #Basic Concept
        -Make a Connection
        -Request a document
        -Retrieve the Document
        -Close the Connection

* The HyperText Transfer Protocol is the set of rules to allow browsers to retrieve web documents from servers over the Internet

htttps://example.com/page.htm
(protocol -> https://)
(host -> example.com)
(document -> page.htm)
'''

#Getting Data From The Server
'''
* Each the user clicks on an anchor tag with an href= value to switch to a new page, the browser makes a connection to the web server and issues a "GET" request- to GET the content of the page at the specified URL
* Ther server returns the HTML document to the Browser which formats and displays the document to the user.
'''

#Internet Standards
'''
* The standards for all of the Internet protocols (inner working) are developed by an organization
* Internet Engineering Task Force(IETF)
* Standards are called "RFCs" - "Request for Comments"
'''

#Making an HTPP request
'''
* Connect to the server like "www.example.com"
* Request a document (or the default document)
    * Get http://www.example.com/page1.htm HTTP/1.0
'''