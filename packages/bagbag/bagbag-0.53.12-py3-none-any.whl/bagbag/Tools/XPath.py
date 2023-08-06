from __future__ import annotations

import lxml.html 

class XPath():
    def __init__(self, html:str|lxml.html.HtmlElement):
        if type(html) == str:
            self.root = lxml.html.fromstring(html)
        elif type(html) == lxml.html.HtmlElement:
            self.root = html 
        else:
            raise Exception("Unsupport type: ", str(type(html)))
    
    def Find(self, xpath:str) -> XPath | None:
        """
        > If the xpath is found, return the first matched XPath object, otherwise return None
        
        :param xpath: The XPath expression to search for
        :type xpath: str
        :return: XPath object
        """
        res = self.root.xpath(xpath)
        if len(res) == 0:
            return None 
        else:
            return XPath(res[0])
    
    def Attribute(self, name:str) -> str | None:
        """
        If the attribute name is in the element, return the attribute value, otherwise return None
        
        :param name: The name of the attribute to get
        :type name: str
        :return: The value of the attribute name.
        """
        if name in self.root.attrib:
            return self.root.attrib[name]
        else:
            return None 
        
    def Text(self) -> str:
        """
        It returns the text content of the element of the HTML document

        :return: The text content of the root element.
        """
        return self.root.text_content()

    def Html(self) -> str:
        """
        Return the HTML of the element.

        :return: The HTML of the element.
        """
        return lxml.html.tostring(self.root).decode('utf-8')

