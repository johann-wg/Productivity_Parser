# span 으로 추출하는 방법 / pip install python-docx
import requests
from bs4 import BeautifulSoup
import docx
import sys
url = 'https://www.ytn.co.kr/_ln/0105_202303031200389798'

try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(e)
    sys.exit(1)

soup = BeautifulSoup(response.content, 'html.parser')
span_tag = soup.find('span', style='display:inline-block;width:740px;')
text = span_tag.get_text()

doc = docx.Document()
doc.add_paragraph(text)

doc.save('/Users/jjong/desktop/example.docx')
