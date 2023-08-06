# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['iscc_core']

package_data = \
{'': ['*']}

install_requires = \
['base58>=2.1,<3.0',
 'bases>=0.2,<0.3',
 'bitarray-hardbyte>=2.3,<3.0',
 'blake3>=0.3,<0.4',
 'data-url>=1.0,<2.0',
 'jcs>=0.2,<0.3',
 'loguru>=0.6,<0.7',
 'more-itertools>=9.0,<10.0',
 'pybase64>=1.2,<2.0',
 'pydantic[dotenv]',
 'uvarint>=1.2,<2.0',
 'xxhash>=3.0,<4.0']

extras_require = \
{'turbo': ['cython>=0.29,<0.30']}

setup_kwargs = {
    'name': 'iscc-core',
    'version': '0.2.14',
    'description': 'ISCC - Core Algorithms',
    'long_description': '# ISCC - Codec & Algorithms\n\n[![Build](https://github.com/iscc/iscc-core/actions/workflows/tests.yml/badge.svg)](https://github.com/iscc/iscc-core/actions/workflows/tests.yml)\n[![Version](https://img.shields.io/pypi/v/iscc-core.svg)](https://pypi.python.org/pypi/iscc-core/)\n[![Coverage](https://codecov.io/gh/iscc/iscc-core/branch/main/graph/badge.svg?token=7BJ7HJU815)](https://codecov.io/gh/iscc/iscc-core)\n[![Quality](https://app.codacy.com/project/badge/Grade/ad1cc48ac0c0413ea2373a938148f019)](https://www.codacy.com/gh/iscc/iscc-core/dashboard)\n[![Downloads](https://pepy.tech/badge/iscc-core)](https://pepy.tech/project/iscc-core)\n\n`iscc-core` is the reference implementation of the core algorithms of the [ISCC](https://iscc.codes)\n(*International Standard Content Code*)\n\n## What is the ISCC\n\nThe ISCC is a similarity preserving fingerprint and identifier for digital media assets.\n\nISCCs are generated algorithmically from digital content, just like cryptographic hashes. However,\ninstead of using a single cryptographic hash function to identify data only, the ISCC uses various\nalgorithms to create a composite identifier that exhibits similarity-preserving properties (soft\nhash).\n\nThe component-based structure of the ISCC identifies content at multiple levels of abstraction. Each\ncomponent is self-describing, modular, and can be used separately or with others to aid in various\ncontent identification tasks. The algorithmic design supports content deduplication, database\nsynchronization, indexing, integrity verification, timestamping, versioning, data provenance,\nsimilarity clustering, anomaly detection, usage tracking, allocation of royalties, fact-checking and\ngeneral digital asset management use-cases.\n\n## What is `iscc-core`\n\n`iscc-core` is a python based reference library of the core algorithms to create standard-compliant\nISCC codes. It also a good reference for porting ISCC to other programming languages.\n\n!!! tip\n    This is a low level reference implementation that does not inlcude features like mediatype\n    detection, metadata extraction or file format specific content extraction. Please have a look at\n    the [iscc-sdk](https://github.com/iscc/iscc-sdk) which adds those higher level features on top\n    of the `iscc-core` library.\n\n## Project Status\n\nThe ISCC is under development as [ISO/CD 24138](https://www.iso.org/standard/77899.html) -\nInternational Standard Content Code within\n[ISO/TC 46/SC 9/WG 18](https://www.iso.org/committee/48836.html).\n\n## ISCC Architecture\n\n![ISCC Architecture](https://raw.githubusercontent.com/iscc/iscc-core/master/docs/images/iscc-codec-light.png)\n\n## ISCC MainTypes\n\n| Idx | Slug     | Bits | Purpose                                                |\n| --- | :------- | ---- | ------------------------------------------------------ |\n| 0   | META     | 0000 | Match on metadata similarity                           |\n| 1   | SEMANTIC | 0001 | Match on semantic content similarity                   |\n| 2   | CONTENT  | 0010 | Match on perceptual content similarity                 |\n| 3   | DATA     | 0011 | Match on data similarity                               |\n| 4   | INSTANCE | 0100 | Match on data identity                                 |\n| 5   | ISCC     | 0101 | Composite of two or more components with common header |\n\n## Installation\n\nUse the package manager [pip](https://pip.pypa.io/en/stable/) to install `iscc-core`.\n\n```bash\npip install iscc-core\n```\n\n## Quick Start\n\n```python\nimport json\nimport iscc_core as ic\n\nmeta_code = ic.gen_meta_code(name="ISCC Test Document!")\n\nprint(f"Meta-Code:     {meta_code[\'iscc\']}")\nprint(f"Structure:     {ic.iscc_explain(meta_code[\'iscc\'])}\\n")\n\n# Extract text from file\nwith open("demo.txt", "rt", encoding="utf-8") as stream:\n    text = stream.read()\n    text_code = ic.gen_text_code_v0(text)\n    print(f"Text-Code:     {text_code[\'iscc\']}")\n    print(f"Structure:     {ic.iscc_explain(text_code[\'iscc\'])}\\n")\n\n# Process raw bytes of textfile\nwith open("demo.txt", "rb") as stream:\n    data_code = ic.gen_data_code(stream)\n    print(f"Data-Code:     {data_code[\'iscc\']}")\n    print(f"Structure:     {ic.iscc_explain(data_code[\'iscc\'])}\\n")\n\n    stream.seek(0)\n    instance_code = ic.gen_instance_code(stream)\n    print(f"Instance-Code: {instance_code[\'iscc\']}")\n    print(f"Structure:     {ic.iscc_explain(instance_code[\'iscc\'])}\\n")\n\n# Combine ISCC-UNITs into ISCC-CODE\niscc_code = ic.gen_iscc_code(\n    (meta_code["iscc"], text_code["iscc"], data_code["iscc"], instance_code["iscc"])\n)\n\n# Create convenience `Code` object from ISCC string\niscc_obj = ic.Code(iscc_code["iscc"])\nprint(f"ISCC-CODE:     {ic.iscc_normalize(iscc_obj.code)}")\nprint(f"Structure:     {iscc_obj.explain}")\nprint(f"Multiformat:   {iscc_obj.mf_base32}\\n")\n\n# Compare with changed ISCC-CODE:\nnew_dc, new_ic = ic.Code.rnd(mt=ic.MT.DATA), ic.Code.rnd(mt=ic.MT.INSTANCE)\nnew_iscc = ic.gen_iscc_code((meta_code["iscc"], text_code["iscc"], new_dc.uri, new_ic.uri))\nprint(f"Compare ISCC-CODES:\\n{iscc_obj.uri}\\n{new_iscc[\'iscc\']}")\nprint(json.dumps(ic.iscc_compare(iscc_obj.code, new_iscc["iscc"]), indent=2))\n```\n\nThe output of this example is as follows:\n\n```\nMeta-Code:     ISCC:AAAT4EBWK27737D2\nStructure:     META-NONE-V0-64-3e103656bffdfc7a\n\nText-Code:     ISCC:EAAQMBEYQF6457DP\nStructure:     CONTENT-TEXT-V0-64-060498817dcefc6f\n\nData-Code:     ISCC:GAA7UJMLDXHPPENG\nStructure:     DATA-NONE-V0-64-fa258b1dcef791a6\n\nInstance-Code: ISCC:IAA3Y7HR2FEZCU4N\nStructure:     INSTANCE-NONE-V0-64-bc7cf1d14991538d\n\nISCC-CODE:     ISCC:KACT4EBWK27737D2AYCJRAL5Z36G76RFRMO4554RU26HZ4ORJGIVHDI\nStructure:     ISCC-TEXT-V0-MCDI-3e103656bffdfc7a060498817dcefc6ffa258b1dcef791a6bc7cf1d14991538d\nMultiformat:   bzqavabj6ca3fnp757r5ambeyqf6457dp7isywhoo66i2npd46hiutektru\n\nCompare ISCC-CODES:\nISCC:KACT4EBWK27737D2AYCJRAL5Z36G76RFRMO4554RU26HZ4ORJGIVHDI\nISCC:KACT4EBWK27737D2AYCJRAL5Z36G7Y7HA2BMECKMVRBEQXR2BJOS6NA\n{\n  "meta_dist": 0,\n  "content_dist": 0,\n  "data_dist": 33,\n  "instance_match": false\n}\n```\n\n## Documentation\n\nDocumentation is published at<https://core.iscc.codes>\n\n## Development\n\n**Requirements**\n\n- [Python 3.7.2](https://www.python.org/) or higher for code generation and static site building.\n- [Poetry](https://python-poetry.org/) for installation and dependency management.\n\n**Development Setup**\n\n```shell\ngit clone https://github.com/iscc/iscc-core.git\ncd iscc-core\npoetry install\n```\n\n**Development Tasks**\n\nTests, coverage, code formatting and other tasks can be run with the `poe` command:\n\n```shell\npoe\n\nPoe the Poet - A task runner that works well with poetry.\nversion 0.18.1\n\nResult: No task specified.\n\nUSAGE\n  poe [-h] [-v | -q] [--root PATH] [--ansi | --no-ansi] task [task arguments]\n\nGLOBAL OPTIONS\n  -h, --help     Show this help page and exit\n  --version      Print the version and exit\n  -v, --verbose  Increase command output (repeatable)\n  -q, --quiet    Decrease command output (repeatable)\n  -d, --dry-run  Print the task contents but don\'t actually run it\n  --root PATH    Specify where to find the pyproject.toml\n  --ansi         Force enable ANSI output\n  --no-ansi      Force disable ANSI output\nCONFIGURED TASKS\n  gentests       Generate conformance test data\n  format         Code style formating with black\n  docs           Copy README.md to /docs\n  format-md      Markdown formating with mdformat\n  lf             Convert line endings to lf\n  test           Run tests with coverage\n  sec            Security check with bandit\n  all\n```\n\nUse `poe all` to run all tasks before committing any changes.\n\n## Maintainers\n\n[@titusz](https://github.com/titusz)\n\n## Contributing\n\nPull requests are welcome. For significant changes, please open an issue first to discuss your\nplans. Please make sure to update tests as appropriate.\n\nYou may also want join our developer chat on Telegram at <https://t.me/iscc_dev>.\n',
    'author': 'Titusz',
    'author_email': 'tp@py7.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://iscc.codes',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.2,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
