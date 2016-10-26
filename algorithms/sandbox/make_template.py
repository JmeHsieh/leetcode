from bs4 import BeautifulSoup


def main():
    with open('./leet.html', 'r') as f:
        html = f.read()

    # extract necessary info
    soup = BeautifulSoup(html, 'html.parser')
    ps = soup.find_all('p')[7:]
    ps_ = filter(lambda tup: tup[0] % 7 == 1 or tup[0] % 7 == 2, enumerate(ps))
    ps_ = list(map(lambda tup: tup[1], ps_))
    leet_ids = [tup[1].span.string for tup in enumerate(ps_) if tup[0] % 2 == 0]
    leet_urls = [tup[1].a['href'] for tup in enumerate(ps_) if tup[0] % 2 == 1]
    problems = zip(leet_ids, leet_urls)

    # create template source files with correct 'id' as filename
    # with problem_url on the top of source file
    for _id, url in problems:
        with open('./{}.py'.format(_id), 'w') as f:
            f.writelines('# {}'.format(url))
        with open('./{}.swift'.format(_id), 'w') as f:
            f.writelines('// {}'.format(url))


if __name__ == '__main__':
    main()
