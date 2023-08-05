# Watch Path
[heading__top]:
  #watch_path
  "&#x2B06; Runs command or callback function when watched path modified time changes"


Runs command or callback function when path file modified time changes


## [![Byte size of Watch Path][badge__master__watch_path__source_code]][watch_path__master__source_code] [![Open Issues][badge__issues__watch_path]][issues__watch_path] [![Open Pull Requests][badge__pull_requests__watch_path]][pull_requests__watch_path] [![Latest commits][badge__commits__watch_path__master]][commits__watch_path__master]



------


- [:arrow_up: Top of Document][heading__top]

- [:building_construction: Requirements][heading__requirements]

- [:zap: Quick Start][heading__quick_start]

  - [:memo: Your Requirements File][heading__your_requirements_file]
  - [:floppy_disk: Commit and Push][heading__commit_and_push]
  - [&#x1F9F0; Usage][heading__usage]

- [&#x1F5D2; Notes][heading__notes]

- [:card_index: Attribution][heading__attribution]

- [:balance_scale: Licensing][heading__license]


------



## Requirements
[heading__requirements]:
  #requirements
  "&#x1F3D7; Prerequisites and/or dependencies that this project needs to function properly"


Python version 2 or 3


______


## Quick Start
[heading__quick_start]:
  #quick-start
  "&#9889; Perhaps as easy as one, 2.0,..."


Install this project via Pip version 2 or 3


```Bash
pip3 install --user --upgrade watch-path
```


### Your Requirements File
[heading__your_requirements_file]:
  #your-requirements-file
  "&#x1F4DD; Suggested additions for your requirements.txt file so everyone has a good time with dependencies"


Suggested additions for your requirements.txt file so everyone has a good time with dependencies


```txt
watch-path
```


### Commit and Push
[heading__commit_and_push]:
  #commit-and-push
  "&#x1F4BE; It may be just this easy..."


```Bash
git add requirements.txt


git commit -F- <<'EOF'
:heavy_plus_sign: Adds `python-utilities/watch_path#1` as dependency


## Anything else worth committing
EOF


git push
```


**:tada: Excellent :tada:** your project is now ready to begin unitizing code from this repository!


------


### Usage
[heading__usage]:
  #usage
  "&#x1F9F0;"


- Print available CLI (Command Line Interface) options


```Bash
watch_path --help
```


- Run command when `test.txt` file changes


```Bash
watch_path --file test.txt
  --command 'cat test.txt'\
  --sleep 0.5\
  --decode utf-8
```


------


Example of inheriting and modifying a class from watch_path...


```Python
#!/usr/bin/env python


from watch_path import Watch_Path


class Customized_Watch_Path(Watch_Path):
    """
    Customizes `watch_path` class
    """

    def __init__(self, ignore_empty, **kwargs):
        """
        Adds `ignore_empty` to initialization parameters of class
        """
        super(watch_path, self).__init__(**kwargs)
        self.update(ignore_empty = ignore_empty)

    def next(self):
        """
        Adds logic to ignore empty/non-existent paths
        """
        try:
            new_time_stamp = self.file_modified_time(self['path'])
        except OSError as e:
            print(e)
            if self['ignore_empty'] is not True:
                self.throw(GeneratorExit)

        if new_time_stamp != self['time_stamp']:
            self['time_stamp'] = new_time_stamp
            return self['callback'](path = self['path'],
                                    time_stamp = new_time_stamp,
                                    **self['callback_kwargs'])


def custom_callback(**kwargs):
    print("Detected disturbances in {path}".format(path = kwargs['path']))


if __main__ == '__name__':
    """
    Code that is run if this file is executed as a script instead of imported
    """
    custom_file_watcher = Customized_Watch_Path(callback = custom_callback
                                                path = 'test.txt',
                                                ignore_empty = True)

    try:
        for callback_results in custom_file_watcher:
            if callback_results:
                print(callback_results['stdout'].decode('UTF-8'))

            sleep(1)

    except KeyboardInterrupt:
        print('Stopping watcher and exiting...')
```


______


## Notes
[heading__notes]:
  #notes
  "&#x1F5D2; Additional things to keep in mind when developing"


This repository may not be feature complete and/or fully functional, Pull Requests that add features or fix bugs are certainly welcomed.


______


## Attribution
[heading__attribution]:
  #attribution
  "&#x1F4C7; Resources that where helpful in building this project so far."


- [GitHub -- `github-utilities/make-readme`](https://github.com/github-utilities/make-readme)

- [StackOverflow -- How do I import `FileNotFounderror` from Python 3?](https://stackoverflow.com/questions/26745283)

- [StackOverflow -- How do i watch a file for changes?](https://stackoverflow.com/questions/182197)

- [StackOverflow -- What does the `b` character do in front of a string literal?](https://stackoverflow.com/questions/6269765)


______


## License
[heading__license]:
  #license
  "&#x2696; Legal side of Open Source"


```
Documentation for Watch Path
Copyright (C) 2023 S0AndS0

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```


For further details review full length version of [AGPL-3.0][branch__current__license] License.



[branch__current__license]:
  /LICENSE
  "&#x2696; Full length version of AGPL-3.0 License"


[badge__commits__watch_path__master]:
  https://img.shields.io/github/last-commit/python-utilities/watch_path/master.svg

[commits__watch_path__master]:
  https://github.com/python-utilities/watch_path/commits/master
  "&#x1F4DD; History of changes on this branch"


[watch_path__community]:
  https://github.com/python-utilities/watch_path/community
  "&#x1F331; Dedicated to functioning code"


[issues__watch_path]:
  https://github.com/python-utilities/watch_path/issues
  "&#x2622; Search for and _bump_ existing issues or open new issues for project maintainer to address."

[pull_requests__watch_path]:
  https://github.com/python-utilities/watch_path/pulls
  "&#x1F3D7; Pull Request friendly, though please check the Community guidelines"

[watch_path__master__source_code]:
  https://github.com/python-utilities/watch_path/
  "&#x2328; Project source!"

[badge__issues__watch_path]:
  https://img.shields.io/github/issues/python-utilities/watch_path.svg

[badge__pull_requests__watch_path]:
  https://img.shields.io/github/issues-pr/python-utilities/watch_path.svg

[badge__master__watch_path__source_code]:
  https://img.shields.io/github/repo-size/python-utilities/watch_path
