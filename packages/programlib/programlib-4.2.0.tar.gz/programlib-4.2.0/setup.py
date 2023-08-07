# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['programlib']

package_data = \
{'': ['*'], 'programlib': ['programs/*']}

setup_kwargs = {
    'name': 'programlib',
    'version': '4.2.0',
    'description': 'Programs as Objects',
    'long_description': '# Programlib: programs as objects\n\nProgramlib is a tool that turns programs in any programming language into convenient Python objects, letting you run any string as a C++/Python/Clojure/etc program from a Python script.\nThis project is aimed to help develop automatic programming and genetic software improvement systems, though many other applications are possible.\n\n## Installation\n\nProgramlib can be installed with\n\n```\npip install programlib\n```\n\nHowever, you have to also make sure that the programming languages you want to use are installed.\nBy default, programlib uses command line tools that come with the programming languages, i.e. `python3` or `javac`.\n\n## Standard usage\n\nCreate a program object with\n\n```python\nfrom programlib import Program\nprogram = Program(source_code, language=\'C++\')\n```\n\nThis object has\n- a `run` method that runs the program and returns a list of strings it printed to `stdout`. You can optionally provide a list of input strings as well.\n- a `test` method that takes a list of test cases. A test case is a tuple of 2 lists: the first list is the input strings, the second is the expected output strings. The method returns percentage of output strings that matched expectations.\n- a `save` method that will save the source code to a file at the specified path.\n\nSee also `examples`.\n\nCurrently supported programming languages out of the box are C++, Python, Java, Clojure, Ruby, Rust, Go, Haskell, Scala, Kotlin, PHP, C#, Swift, D, Julia, Clojure, Elixir and Erlang.\nSee "Advanced usage" below for instructions on how to add other languages.\n\n## Advanced usage\n\n### Language configuration\n\nWhen you create a program object with a language name like `language=\'C++\'`, `programlib` retrieves an appropriate language configuration from it\'s database.\nIf you have a different opinion on how to compile or run in this language or want to use a language that is not supported out of the box, you can create your own language configuration object:\n\n```python\nfrom programlib import Program, Language\nlanguage = Language(\n        build_cmd=\'g++ {name}.cpp -o {name}\',\n        run_cmd=\'./{name}\',\n        source=\'{name}.cpp\',\n        artefacts=[\'{name}\']\n    )\nprogram = Program(source_code, language=language)\n```\n\n`source` parameter describes the naming convention for the source file (usually `{name}.extension`). Make sure that this parameter contains a `{name}` placeholder, so that `programlib` can keep track of several source files at the same time.\n`build_cmd` and `run_cmd` respectively instruct `programlib` which commands to use to compile and run the program in this language.\n`artefacts` is a list of all the files produced by `build_cmd` command.\nIt is needed to clean up the artefacts when the program object is destroyed.\n\n### Error handling\n\nAny output written to `stderr` is considered an error.\nBy default, any errors at build time or run time will lead to an exception being raised, with 2 exceptions:\n- `test` function that catches exceptions during test cases execution and marks these tests as failed.\n- Setting `program.run(force=True)` or `program.test(force=True)` will make `programlib` ignore all errors.\n\nYou can check `program.stdout` and `program.stderr` to see what the program printed to `stdout` and `stderr` during the last run (or, if in was never run, during build).',
    'author': 'Vadim Liventsev',
    'author_email': 'dev@vadim.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
