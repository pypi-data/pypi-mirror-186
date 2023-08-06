# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tempren', 'tempren.tags', 'tempren.template', 'tempren.template.grammar']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.2.0,<10.0.0',
 'Unidecode>=1.2.0,<2.0.0',
 'antlr4-python3-runtime>=4.10,<5.0',
 'docstring-parser>=0.13,<0.14',
 'isodate>=0.6.1,<0.7.0',
 'mutagen>=1.45.1,<2.0.0',
 'pathvalidate>=2.4.1,<3.0.0',
 'piexif>=1.1.3,<2.0.0',
 'python-magic>=0.4.27,<0.5.0']

extras_require = \
{'video': ['pymediainfo>=5.1.0,<6.0.0']}

entry_points = \
{'console_scripts': ['tempren = tempren.cli:throwing_main']}

setup_kwargs = {
    'name': 'tempren',
    'version': '0.8.0',
    'description': 'Template-based renaming utility',
    'long_description': '# Tempren - template-based file renaming utility\n\n![run-tests](https://github.com/idle-code/tempren/actions/workflows/run-tests.yml/badge.svg)\n[![codecov](https://codecov.io/gh/idle-code/tempren/branch/develop/graph/badge.svg?token=1CR2PX6GYB)](https://codecov.io/gh/idle-code/tempren)\n[![Maintainability](https://api.codeclimate.com/v1/badges/d67f6ebe698b79d75279/maintainability)](https://codeclimate.com/github/idle-code/tempren/maintainability)\n[![PyPI version](https://badge.fury.io/py/tempren.svg)](https://badge.fury.io/py/tempren)\n[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/idle-code/tempren/develop.svg)](https://results.pre-commit.ci/latest/github/idle-code/tempren/develop)\n\n`tempren` is a powerful file renaming utility that uses flexible template expressions to create new file paths and names.\nNew file paths can be based on original filename, created independently or from the underlying file\'s tags.\nRich library of built-in tag extraction modules helps with tagging many common file types.\n\n## Features\n- Template-based filename/path generation\n- Audio/Video/Images/etc metadata extraction\n- Configurable, metadata-based file selection (filtering)\n- Metadata-based sorting\n\n## Installation\nCurrently only PyPI installation is supported, just run following command:\n```commandline\n$ pip install [--user] tempren\n```\n\n## Documentation\n[Manual](MANUAL.md) gives a tour of all `tempren` features and (until quickstart is created) should work as a guide.\n\n<!--\n## [Quickstart](QUICKSTART.md)\nFor quick, five-minute introduction to the most of `tempren` features please refer to the [quickstart](QUICKSTART.md) page.\nYou can also take a look on the following examples.\n-->\n\n## Examples\n**Note: When experimenting on your own please use `--dry-run` flag!** \\\n**Tempren will not override your files by default but invalid template can mangle their names.**\n\n<details>\n<summary>Cleaning up names for sensitive (e.g. FAT32) filesystems</summary>\n\n```commandline\n$ tempren --recursive --name "%Strip(){%Base()|%Unidecode()|%Sanitize()|%Collapse()}%Ext()" ./Some\\ OST/\nRenamed: Disk 1/14 - 接近.flac\n     to: Disk 1/14 - Jie Jin.flac\nRenamed: Disk 1/02 - なつのあお.flac\n     to: Disk 1/02 - natsunoao.flac\nRenamed: Disk 1/11 - 灯火-re.flac\n     to: Disk 1/11 - Deng Huo -re.flac\nRenamed: Disk 1/05 - 記録.flac\n     to: Disk 1/05 - Ji Lu.flac\nRenamed: Disk 1/10 - むかしむかし、あるところに.flac\n     to: Disk 1/10 - mukashimukashi, arutokoroni.flac\nRenamed: Disk 1/09 - 阿良句のテーマ(ハイ).flac\n     to: Disk 1/09 - A Liang Ju notema(hai).flac\n...\n```\n</details>\n\n<details>\n<summary>Adding resolution to the image files</summary>\n\n```commandline\n$ tempren --name "%Base()_%Image.Width()x%Image.Height()%Ext()" ~/Pictures/Wallpapers\nRenamed: 0sa5yfiskqr21.jpg\n     to: 0sa5yfiskqr21_3728x4660.jpg\nRenamed: rkgjq6883fp81.jpg\n     to: rkgjq6883fp81_3024x4032.jpg\nRenamed: lcrkvphf28911.jpg\n     to: lcrkvphf28911_4016x4684.jpg\nRenamed: y6nzcv55k3851.jpg\n     to: y6nzcv55k3851_3784x5670.jpg\nRenamed: 1211740803547.jpg\n     to: 1211740803547_1200x1109.jpg\n...\n```\n</details>\n\n<details>\n<summary>Sorting files into directories based on their MIME type</summary>\n\n```commandline\n$ tempren -d --path "%Capitalize(){%Mime(subtype)}/%Name()" ~/Downloads\nRenamed: dotnet-install.sh\n     to: X-shellscript/dotnet-install.sh\nRenamed: openrgb_0.7_amd64_buster_6128731.deb\n     to: Vnd.debian.binary-package/openrgb_0.7_amd64_buster_6128731.deb\nRenamed: prometheus-2.26.0.linux-amd64.tar.gz\n     to: Gzip/prometheus-2.26.0.linux-amd64.tar.gz\nRenamed: nldb remote.zip\n     to: Zip/nldb remote.zip\nRenamed: artifacts.zip\n     to: Zip/artifacts.zip\nRenamed: 2021-06-11_12-09-34.webm\n     to: X-matroska/2021-06-11_12-09-34.webm\nRenamed: antlr-4.9.2-complete.jar\n     to: Java-archive/antlr-4.9.2-complete.jar\n...\n```\n</details>\n\n<details>\n<summary>Adding checksums to the names of the audio files</summary>\n\n```commandline\n$ tempren --filter-template "%IsMime(\'audio\')" --name "%Base() [%Upper(){%Crc32()}]%Ext()" ./Roger\\ Subirana\\ Mata\\ -\\ Point\\ of\\ no\\ return\nRenamed: 10-169205-Roger Subirana Mata-Island of light.mp3\n     to: 10-169205-Roger Subirana Mata-Island of light [08E46C33].mp3\nRenamed: 12-169207-Roger Subirana Mata-Tales of trees.mp3\n     to: 12-169207-Roger Subirana Mata-Tales of trees [33EFEC5E].mp3\nRenamed: 11-169206-Roger Subirana Mata-Requiem.mp3\n     to: 11-169206-Roger Subirana Mata-Requiem [5E48759B].mp3\nRenamed: 05-168950-Roger Subirana Mata-The mask.mp3\n     to: 05-168950-Roger Subirana Mata-The mask [045DBC19].mp3\nRenamed: 03-168948-Roger Subirana Mata-Thryst.mp3\n     to: 03-168948-Roger Subirana Mata-Thryst [5D23E43B].mp3\n...\n```\n</details>\n\n\n## Contributing\nIf you noticed a bug or have an idea for a new tag please open an issue with appropriate tags.\nIf you would like to contribute to the development you can visit [contributing page](CONTRIBUTING.md) designed specially for that.\n',
    'author': 'Paweł Żukowski',
    'author_email': 'p.z.idlecode@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/idle-code/tempren',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
