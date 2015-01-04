import bs4, importlib, requests  #, pkgutil

pypi_dict = { 'bs4'      : 'beautifulsoup4',
              'dateutil' : 'py-dateutil',
              'faker'    : 'Faker' }

def get_module_version(in_module_name = 'requests'):
    mod = importlib.import_module(in_module_name)
    fmt = "### hasattr({}, '{}')".format(in_module_name, '{}')
    for attr_name in '__version__ version __VERSION__ VERSION'.split():
    #for attr_name in '__VERSION__ VERSION'.split():
        if hasattr(mod, attr_name):
            if attr_name != '__version__':
                print(fmt.format(attr_name))
            the_attr = getattr(mod, attr_name)
            if isinstance(the_attr, tuple):  # mechanize workaround
                the_attr = '.'.join([str(i) for i in the_attr[:3]])
            return the_attr() if callable(the_attr) else the_attr
    return '?' * 5

def get_module_version_from_pypi(module_name = 'bs4'):
    module_name = pypi_dict.get(module_name, module_name)
    url = 'https://pypi.python.org/pypi/{}'.format(module_name)
    soup = bs4.BeautifulSoup(requests.get(url).content)
    vers_str = soup.title.string.partition(':')[0].split()[-1]
    if vers_str == 'Packages':
        return soup.find('div', class_='section').a.string.split()[-1]
    return vers_str
    
#for pkg in pkgutil.walk_packages():
#    print ('{:<10} {}'.format(pkg[1], get_module_version(pkg[1])))
#print('=' * 16)

modules = ('bottle bs4 dateutil dropbox ecdsa evernote faker feedparser flask html5lib markdown markdown2 mechanize paramiko PIL pygments pyparsing requests six wsgiref xmltodict')
for module_name in modules.split():
    print('{:<10} {:<7} v.s. {}'.format(module_name, get_module_version(module_name),
                                        get_module_version_from_pypi(module_name)))
print('=' * 16)

'''
bottle     0.12.5  v.s. 0.12.8  OLDER VERSION
bs4        4.3.2   v.s. 4.3.2   current version
dateutil   1.5-mpl v.s. 2.2     correct version for Python2
dropbox    ?????   v.s. 2.2.0   unclear
ecdsa      0.11    v.s. 0.11    current version
evernote   ?????   v.s. 1.25.0  unclear
faker      ?????   v.s. 0.0.4   unclear
feedparser 5.1.3   v.s. 5.1.3   current version
flask      0.10.1  v.s. 0.10.1  current version
html5lib   0.999   v.s. 0.999   current version
### hasattr(markdown, 'version')
markdown   2.2.0   v.s. 2.5.2   OLDER VERSION
markdown2  2.2.1   v.s. 2.3.0   OLDER VERSION
mechanize  0.2.5   v.s. 0.2.5  current version
paramiko   1.13.0  v.s. 1.15.2  OLDER VERSION
PIL        ?????   v.s. 1.1.6   unclear
pygments   1.6     v.s. 2.0.1   OLDER VERSION
pyparsing  2.0.1   v.s. 2.0.3   OLDER VERSION
requests   2.2.1   v.s. 2.5.1   OLDER VERSION
six        1.6.1   v.s. 1.9.0   OLDER VERSION
wsgiref    ?????   v.s. 0.1.2   unclear
xmltodict  0.8.7   v.s. 0.9.0   OLDER VERSION
================
'''
