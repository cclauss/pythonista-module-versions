# coding: utf-8
import bs4, importlib, inspect, requests, itertools

modules = '''canvas clipboard console contacts editor keychain linguistictagger
             location motion notification photos scene sound speech ui'''.split()
modules += '''appex cb ctypes dialogs sk'''.split()  # modules added in Pythonista v1.6 Beta

def inspect_functions(module_name):
    module = importlib.import_module(module_name)
    return [member[0] for member in inspect.getmembers(module)
            if callable(member[1]) and not member[0].startswith('_')]

def get_html(mondule_name):
    fmt = 'http://omz-software.com/pythonista/docs/ios/{}.html'
    return requests.get(fmt.format(module_name)).text

def website_functions(module_name):
    headerlinks = bs4.BeautifulSoup(get_html(module_name)).find_all('a', 'headerlink')
    return sorted(list(set([hl['href'].partition('.')[2]
                        for hl in headerlinks if '.' in hl['href']])))

def undocumented_functions(module_name):
    print('looking for undocumented in {} module...'.format(module_name))
    inspect_funcs = inspect_functions(module_name)
    website_funcs = website_functions(module_name)
    return ['{}.{}()'.format(module_name, f) for f in inspect_funcs
                                           if f not in website_funcs]

undocumented = [x for x in [undocumented_functions(module_name)
                                 for module_name in sorted(modules)]]
print('=' * 40)
print('\n'.join(itertools.chain(*undocumented)))  # flatten()
