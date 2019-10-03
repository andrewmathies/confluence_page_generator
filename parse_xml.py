import re
import xml.dom.minidom

from node import Node

root = Node('root')
lastDepth = 0
lastNode = root
count = 1

def addToTree(text, depth):
    if depth == 0:
        return

    global lastDepth, lastNode, count
    count += 1
    newNode = Node(text)

    if depth > lastDepth:
        lastNode.children.append(newNode)
        newNode.parent = lastNode
    else:
        while depth < lastDepth and lastDepth >= 0:
            lastNode = lastNode.parent
            lastDepth -= 1
        lastNode.parent.children.append(newNode)
        newNode.parent = lastNode.parent

    lastNode = newNode
    lastDepth = depth

def printTree(node, depth=0):
    if node == None:
        return
    
    print('\t' * depth + str(node))

    for child in node.children:
        printTree(child, depth + 1)

def buildTree():
    fileName = input('Enter the xml filename.\n')
    dom = xml.dom.minidom.parse(fileName)
    formattedXml = dom.toprettyxml()
    lines = formattedXml.splitlines()

    depth = -1
    text = ''

    for line in lines:
        ilvlMatches = re.findall('<w:ilvl w:val="(\d+)"/>', line)
        textMatches = re.findall('>(.+)</w:t>', line)

        if ilvlMatches:
            if len(ilvlMatches) != 1:
                print('ERR, found too many ilvls')
                print(line)
                return

            # we got all of the text before the next ilvl object in the dom, time to store it as a node in the tree
            addToTree(text, depth + 1)
            
            text = ''
            depth = int(ilvlMatches[0])
        
        if textMatches:
            if len(textMatches) != 1:
                print('ERR, found too many texts')
                print(line)
                return

            text += textMatches[0]
    
    addToTree(text, depth + 1)
    return root

def main():
    buildTree()
    print('Successfully parsed xml file. Tree contains: ', str(count), ' nodes')
    #printTree(root)

if __name__ == '__main__':
    main()