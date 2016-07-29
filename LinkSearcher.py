import re

LINK_REG = r"\[\s*(?P<title>[^\[|^\]]+)\s*\]\s*\(\s*\#\s*(?P<id>[^\(|^\)]+)\s*\)"
REPLACE_REG = r"\[\s*%s\s*\]\s*\(\s*\#\s*%s\s*\)"

class LinkSearcher(object):
    def __init__(self):
        return

    def getLinks(self, lines):
        links = re.findall(LINK_REG, lines)
        needToRemove = []
        for i in range(0,len(links)-1):
            for j in range(i+1,len(links)):
                if links[i][0] == links[j][0]:
                    if links[i][1] != links[j][1]:
                        lines = re.sub(REPLACE_REG % (re.escape(links[j][0]), re.escape(links[j][1])), "[%s](#%s)" % (links[i][0], links[i][1]), lines)
                    needToRemove.append(links[j])
        for link in set(needToRemove):
            links.remove(link)
        return (lines, links)


