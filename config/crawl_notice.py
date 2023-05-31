import requests
from bs4 import BeautifulSoup


def crawl_notice(src):
    """
    공지 크롤링 함수
    :param src: 게시판 번호. 1: 일반공지, 2: 학사공지, 3: 종합봉사실 공지
    :return: 공지사항 Dictionary
    """
    notice_url = f'http://www.sogang.ac.kr/front/boardlist.do?bbsConfigFK={src}'

    response = requests.get(notice_url)

    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table in the HTML
    table = soup.find_all('table')[1]

    # Find all rows in the table, skip the first row (header)
    rows = table.find_all('tr')[1:]

    data = []

    for row in rows:
        # Find all columns in the row
        cols = row.find_all('td')

        # Extract text from columns
        num = cols[0].get_text(strip=True)
        title = cols[1].find('a').get_text(strip=True)
        writer = cols[2].get_text(strip=True)
        files = [link.get_text(strip=True) for link in cols[3].find_all('a')]
        date = cols[4].get_text(strip=True)
        views = cols[5].get_text(strip=True)
        # Add the data to the list as a dictionary
        data.append({
            'Number': num,
            'Title': title,
            'Writer': writer,
            'Files': files,
            'Date': date,
            'Views': views,
        })

        print('Number:', num)
        print('Title:', title)
        print('Writer:', writer)
        print('Files:', files)
        print('Date:', date)
        print('Views:', views)
        print('---'*10)
