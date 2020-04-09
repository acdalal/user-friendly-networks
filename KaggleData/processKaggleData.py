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
    # Note: sometimes we'll see escaped string in the text; get rid of those, too.
    cleanedStr = cleanedStr.replace('\\n', ' ')
    return cleanedStr


def main():
    with open("queryQandAandComments.txt", "r") as file:
        lines = file.readlines()
        cleanedLines = cleanData(lines)
        for line in cleanedLines:
            print(line)
    

if __name__ == '__main__':
    main()