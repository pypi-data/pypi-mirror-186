## 10.0.13
- Fixed argparser bug when running as script.
 
## 10.0.12
- Fixed PyPi Upload issue.

## 10.0.11
- Fixed ValueError bug.

## 10.0.10
- Fixed UnboundLocalError bug.

## 10.0.9
- Enhanced licence validation code checking.

## 10.0.8
- Added support for Python 3.11.
- Added pyproject.toml

## 10.0.7
- Enabed the '--crossover' option by default prior to deprecating it.

## 10.0.6
- Updated Documentation on PyPi.
- Fixed 'validate' command so it works before activation.

## 10.0.5
- Updated PyPi Documentation in README.md.
- Fixed typo in '--help' section.

## 10.0.4
- Fixed bug where pack didn't work for trail users.
- Refactored pip installation code.

## 10.0.3
- Fixed wildcard import issue when using: 'from package import *' imports.

## 10.0.2
- Fixed crossover code detection error.

## 10.0.1
- Fixed bug in '--crossover'.

## 10.0.0
- Added '--crossover' as an option to enable cross Python version support.
- Changed auto-upgrade to keep sourcedefender in the current release branch e.g sourcedefender~=10.

## 9.4.2
- Changed defaults to '--minify' to keep Python annotations.

## 9.4.1
- Bugfixes

## 9.4.0
- Changed 'feedparser' & 'python-minifier' to get installed on-demand.
- Added '--minify' as an option rather than the default.
- Updated deployment process to include reviewing CHANGELOG.md before uploading to PyPi.
- Added 'changelog' to see changes since the last release.
- Added '--all' to the changelog option to view all changes, not just since the last release.
- Added CHANGELOG.md
