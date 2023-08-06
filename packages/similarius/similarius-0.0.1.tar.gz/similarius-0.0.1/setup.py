# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['similarius']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0',
 'lxml>=4.9.2,<5.0.0',
 'nltk>=3.8.1,<4.0.0',
 'requests>=2.28.1,<3.0.0',
 'scikit-learn>=1.2.0,<2.0.0']

entry_points = \
{'console_scripts': ['similarius = similarius:main']}

setup_kwargs = {
    'name': 'similarius',
    'version': '0.0.1',
    'description': 'Compare web page and evaluate the level of similarity.',
    'long_description': '# Similarius\n\nSimilarius is a Python library to compare web page and evaluate the level of similarity.\n\nThe tool can be used as a stand-alone tool or to feed other systems.\n\n\n\n# Requirements\n\n- Python 3.8+\n- [Requests](https://github.com/psf/requests)\n- [Scikit-learn](https://github.com/scikit-learn/scikit-learn)\n- [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/)\n- [nltk](https://github.com/nltk/nltk)\n\n\n\n# Installation\n\n## Source install\n\n**Similarius** can be install with poetry. If you don\'t have poetry installed, you can do the following `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python`.\n\n~~~bash\n$ poetry install\n$ poetry shell\n$ similarius -h\n~~~\n\n## pip installation\n\n~~~bash\n$ pip3 install similarius\n~~~\n\n\n\n# Usage\n\n~~~bash\ndacru@dacru:~/git/Similarius/similarius$ similarius --help\nusage: similarius.py [-h] [-o ORIGINAL] [-w WEBSITE [WEBSITE ...]]\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -o ORIGINAL, --original ORIGINAL\n                        Website to compare\n  -w WEBSITE [WEBSITE ...], --website WEBSITE [WEBSITE ...]\n                        Website to compare\n~~~\n\n\n\n# Usage example\n\n~~~bash\ndacru@dacru:~/git/Similarius/similarius$ similarius -o circl.lu -w europa.eu circl.eu circl.lu\n~~~\n\n\n\n# Used as a library\n\n~~~python\nimport argparse\nfrom similarius import get_website, extract_text_ressource, sk_similarity, ressource_difference, ratio\n\nparser = argparse.ArgumentParser()\nparser.add_argument("-w", "--website", nargs="+", help="Website to compare")\nparser.add_argument("-o", "--original", help="Website to compare")\nargs = parser.parse_args()\n\n# Original\noriginal = get_website(args.original)\n\nif not original:\n    print("[-] The original website is unreachable...")\n    exit(1)\n\noriginal_text, original_ressource = extract_text_ressource(original.text)\n\nfor website in args.website:\n    print(f"\\n********** {args.original} <-> {website} **********")\n\n    # Compare\n    compare = get_website(website)\n\n    if not compare:\n        print(f"[-] {website} is unreachable...")\n        continue\n\n    compare_text, compare_ressource = extract_text_ressource(compare.text)\n\n    # Calculate\n    sim = str(sk_similarity(compare_text, original_text))\n    print(f"\\nSimilarity: {sim}")\n\n    ressource_diff = ressource_difference(original_ressource, compare_ressource)\n    print(f"Ressource Difference: {ressource_diff}")\n\n    ratio_compare = ratio(ressource_diff, sim)\n    print(f"Ratio: {ratio_compare}")\n~~~\n\n',
    'author': 'David Cruciani',
    'author_email': 'david.cruciani@securitymadein.lu',
    'maintainer': 'Alexandre Dulaunoy',
    'maintainer_email': 'a@foo.be',
    'url': 'https://github.com/ail-project/Similarius',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
