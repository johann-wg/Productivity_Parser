# div의 id와 class로 추출하는 방법 / pip install python-docx
import requests
from bs4 import BeautifulSoup
import docx

url = 'https://n.news.naver.com/article/138/0002143512?cds=news_media_pc'  # 원하는 웹페이지 주소를 입력하세요
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# id와 class 속성이 일치하는 div 태그에서 텍스트 추출
div_tag = soup.find('div', {'id': 'dic_area', 'class': 'go_trans _article_content'})
text = div_tag.get_text()

# docx 파일 생성 및 텍스트 저장
doc = docx.Document()
doc.add_paragraph(text)
doc.save('/Users/jjong/desktop/example.docx')  # 저장할 파일 이름을 지정하세요