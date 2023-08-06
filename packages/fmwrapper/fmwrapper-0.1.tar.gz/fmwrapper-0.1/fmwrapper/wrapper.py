'''
FMWrapper (Facts Museum Wrapper) - wrapper for https://facts.museum/.
Can get random (or not) facts.

What this library can extract?:
- Title of fact
- Description of fact
- Url to https://facts.museum/(number)
- Number of fact
- Image from fact
- Total value of facts, available on site
- Tags of fact

Contact with developer:
GitHub | https://github.com/Its-MatriX
'''

import re, requests

SUP_ALPHA = {
    '0': '\u2070',
    '1': '\u00b9',
    '2': '\u00b2',
    '3': '\u00b3',
    '4': '\u2074',
    '5': '\u2075',
    '6': '\u2076',
    '7': '\u2077',
    '8': '\u2078',
    '9': '\u2079'
}


class FactNotFound(Exception):
    pass


class Tag:

    def __init__(self, html: str) -> None:
        href = re.findall('href=[\'\"]/[a-zA-Z0-9\-]*[\'\"]', html)[0]

        self.path = '/' + re.sub('[\'\"]', '', re.sub('href=[\'\"]/', '',
                                                      href))

        self.url = 'https://facts.museum' + self.path

        self.name = re.findall('>.*</a>',
                               html)[0].replace('</a>', '').replace('>', '')

        name_arr = list(self.name)

        if name_arr[0].islower():
            name_arr[0] = name_arr[0].upper()

        self.fixed_name = ''.join(name_arr)


class Fact:

    def __init__(self, http_response: requests.Response) -> None:
        '''
        Function for init "Fact" class.
        Args: `description`, `title`, `url`, `number`, `image_url`, `total_facts`, `tags`, `fulldict`
        '''

        data = http_response.text

        fact_desc_html = re.findall('<p class=\"content\">.*</p>', data)

        fact_title_html = re.findall('<h2>.*</h2>', data)

        fact_total_html = re.findall('[0-9]*\s+фактов\.</p>', data)

        fact_tags_html = re.findall(
            '<a href=[\'\"]+/[a-zA-Z0-9\-]*[\'\"]+>[^(</a>)]*</a>', data)

        try:
            self.description = fact_desc_html[0].replace(
                '<p class="content">', '').replace('</p>', '')

            sups = re.findall('<sup>[^(</sup>)]*</sup>', self.description)

            for sup in sups:
                string = sup.replace('<sup>', '').replace('</sup>', '')
                result = []

                for item in string:
                    val = SUP_ALPHA.get(item)

                    if val:
                        result.append(val)

                    else:
                        result.append(item)

                self.description = self.description.replace(
                    sup, ''.join(result))

            self.title = fact_title_html[0].replace('<h2>',
                                                    '').replace('</h2>', '')

            self.url = http_response.url

            self.number = int(
                http_response.url.replace('https://facts.museum/', ''))

            self.image_url = f'https://facts.museum/img/facts/{self.number}.jpg'

            self.total_facts = int(
                re.sub('\s+фактов\.</p>', '', fact_total_html[0]))

            self.tags = []

            for html in fact_tags_html:
                tag = Tag(html)

                if not tag.path == '/random':
                    self.tags.append(tag)

        except IndexError:
            raise FactNotFound('Failed to extract data from HTTP response.')

    def fulldict(self):
        d = {}

        d.update({'description': self.description})
        d.update({'title': self.title})
        d.update({'url': self.url})
        d.update({'number': self.number})
        d.update({'image_url': self.image_url})
        d.update({'total_facts': self.total_facts})
        d.update({'tags': []})

        for tag in self.tags:
            d['tags'].append({
                'path': tag.path,
                'url': tag.url,
                'name': tag.name,
                'fixed_name': tag.fixed_name
            })

        return d

    def __repr__(self) -> str:
        return '{}(description="{}", title="{}", url="{}", number={})'.format(
            str(self.__class__.__name__), self.description, self.title,
            self.url, str(self.number))


def get_fact(number=None) -> Fact:
    '''
    Function to get random (or not) fact.
    If "number" option is None, choiced random fact.
    '''

    if number:
        is_random = False

    else:
        is_random = True

    if is_random:
        url = 'https://facts.museum/random'

    else:
        url = f'https://facts.museum/{number}'

    response = requests.get(url, allow_redirects=True)
    return Fact(response)