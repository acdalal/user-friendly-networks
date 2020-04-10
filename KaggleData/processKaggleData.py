'''
processKaggleData.py

A Python script that processes StackOverflow data from Kaggle.

Takes in one or more text files of some combination of Q and A and comments.

author: Amy Csizmar Dalal
creation date: 6 April 2020
'''
import re
import sys
# TODO: is there an HTML processing module so that we don't have to use regex to remove tags?

def storeAllData(lines):
    '''
    Separates out the data into questions, answers, and comments, and stores each of them   
    separately, with the question post ID as the storage key.

    PARAMETER:
        a list of lines read in from the source file, cleaned up
    
    RETURNS:
        three dictionaries, one each to store questions, answers, and comments 
    '''
    questions = {}
    answers = {}
    comments = {}
    currPostID = 0
    lineItemCount = 0

    for item in lines:
        if item[0] == '[':
            # this is a post ID
            currPostID = int(item[1:])
            lineItemCount = 1
        else:
            if lineItemCount == 1:
                addToQuestions(currPostID, item, questions)
            lineItemCount += 1

    return questions, answers, comments

def addToQuestions(postID, item, questions):
    '''
    adds the question, unless it's a duplicate, to the questions dictionary

    PARAMETERS:
        postID, the ID number associated with the post
        item, the question associated with the post ID
        questions, the dictionary storing the questions. This will be updated if the question is not already stored in the dictionary.
    '''
    if postID not in questions:
        questions[postID] = item
    

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
    if len(sys.argv) < 2:
        sys.exit("usage: python3 processKaggleData.py filename")
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
        cleanedLines = cleanData(lines)
        
    '''outfileName = "cleaned/" + sys.argv[1]
    with open(outfileName, "w") as outfile:
        for line in cleanedLines:
            outfile.write(line)'''

    questions, answers, comments = storeAllData(cleanedLines)
    print(questions)
    print(answers)
    print(comments)

if __name__ == '__main__':
    main()