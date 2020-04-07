'''
processKaggleData.py

A Python script that processes StackOverflow data from Kaggle.

Takes in one or more text files of some combination of Q and A and comments.

author: Amy Csizmar Dalal
creation date: 6 April 2020
'''
import re
# TODO: is there an HTML processing module so that we don't have to use regex to remove tags?

# TODO: read in lines from file and process all lines at once

def cleanData(lines):
    '''
    Removes any extraneous tags (code, HTML, etc) from the data.

    PARAMETER:
        a list of lines read in from the source file

    RETURNS
        a cleaned up list of lines
    '''
    cleanedLines = []

    for entry in lines:
        cleanedEntry = removeCodeTags(entry)
        cleanedEntry = removeHTMLTags(cleanedEntry)
        cleanedEntry = removeEndlines(cleanedEntry)
        cleanedLines.append(cleanedEntry)

    return cleanedLines

def removeCodeTags(str):
    '''
    Removes tags related to code from a string, and returns the modified string
    '''
    parser = re.compile('<pre>.+</pre>')
    cleanedStr = parser.sub('', str)
    parser = re.compile('<code>.+</code>')
    cleanedStr = parser.sub('', cleanedStr)
    return cleanedStr

def removeHTMLTags(str):
    '''
    Removes HTML tags from a string, and returns the modified string
    '''
    parser = re.compile('<[^>]*>')
    cleanedStr = parser.sub('', str)
    return cleanedStr

def removeEndlines(str):
    '''
    Removes extraneous \n's from a string, and returns the modified string
    '''
    cleanedStr = str.replace('\n', ' ')
    return cleanedStr


def main():
    line = '<p>I am using Red Hat 8 (rhel8), my home router is Asus AC5300 running OpenVPN server. But my rhel8 VPN in Network Manager can\'t not connect to my OpenVPN Server.</p>\n\n<p>Here is the error message I got:  </p>\n\n<blockquote>\n  <p>[root@my-machine ~]# journalctl -f\n  nm-openvpn[30404]: TLS error: Unsupported protocol. This typically indicates that client and server have no common TLS version enabled. This can be caused by mismatched tls-version-min and tls-version-max options on client and server. If your OpenVPN client is between v2.3.6 and v2.3.2 try adding tls-version-min 1.0 to the client configuration to use TLS 1.0+ instead of TLS 1.0 only</p>\n  \n  <p>[root@my-machine ~]# openvpn --version<br>\n  OpenVPN 2.4.7 x86_64-redhat-linux-gnu</p>\n</blockquote>\n\n<p>I\'ve tried by adding <code>tls-version-min 1.0</code> to my <code>.ovpn</code> file but still not working.</p>\n\n<p>Note: In Linux Ubuntu it is working just fine, BUT not Red Hat 8</p>'
    cleanedUpLine = removeEndlines(line)
    cleanedUpLine = removeCodeTags(cleanedUpLine)
    cleanedUpLine = removeHTMLTags(cleanedUpLine)
    print(cleanedUpLine)

if __name__ == '__main__':
    main()