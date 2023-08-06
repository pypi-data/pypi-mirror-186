import markdown 
import markdownify

def Markdown2Html(text:str) -> str:
    return markdown.markdown(text)

def Html2Markdown(html:str) -> str:
    return markdownify.markdownify(html)