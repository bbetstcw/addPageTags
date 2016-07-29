import re
FULL_TAG_REG = r'\#+\s*\<a\s+id\s*\=\s*"%s"\>\s*\</a\>\s*%s\s*\#*'
PARTIAL_TAG_REG = r'(\#+\s*)%s(\s*\#*)'
REPLACE_TAG = r'\1<a id="%s"></a>%s\2'
class TagFinder(object):
    def __init__(self):
        return
    def replaceTags(self, links, lines):
        for link in links:
            fullTag = re.findall(FULL_TAG_REG % (re.escape(link[1]), re.escape(link[0])), lines)
            if len(fullTag) == 0:
                partialTag = re.findall(PARTIAL_TAG_REG % (re.escape(link[0])), lines)
                if len(partialTag) == 0:
                    print('Error: cannot find %s with id="%s"' % (link[0], link[1]))
                else:
                    lines = re.sub(PARTIAL_TAG_REG % (re.escape(link[0])), REPLACE_TAG % (link[1], link[0]), lines)
        return lines


