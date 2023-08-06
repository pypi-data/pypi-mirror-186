# bonggoQuery version 2.0.1
## _The way to make your journey easy with python3_


This is a module made by Sudip Bera and this module help you to increase your coding experience.
This module fully based on wolframalpha and pyttsx3. This module is developed to make your query too exciting and also you can get much features, like :
 
## Features
- weather report
- Time
- ✨Date
- Location
- Search on google as you wish.

The main goal to work on this project is to make the problems easy to the people who are going to make any virtual assistant or like this.
© 2022 Sudip Bera


## Tech

[Bonggo Hriday](https://github.com/SudipBera083/) 
uses a number of open source projects to work properly:

- [wolframalpha](wolframalpha.com)- Compute expert-level answers using Wolfram’s breakthrough
algorithms, knowledgebase and AI technology
- [pyttsx3](https://pypi.org/project/pyttsx3/) - is a text-to-speech conversion library in Python. Unlike alternative libraries.
- [wikipedia](https://pypi.org/project/wikipedia/) - Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia.
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) - Library for performing speech recognition, with support for several engines and APIs, online and offline.



## Installation

bonggoQuery requires [python3](https://www.python.org/downloads/)  to run.

Install the dependencies and devDependencies..


```sh
pip install bonggoQuery
```

For production environments...

```sh
pip install wolframalpha
pip install pytsx3 
pip install SpeechRecognition
pip install wikipedia
```

## Plugins

bonggoQuery is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |

| GitHub | [https://github.com/SudipBera083/][PlGh] |
| Blogger | [bit.ly/3JQIdVW][PlGh] |



## How to use ?

bonggoQuery  is very easy to install and use.

# 1.Take Command From the User :

```sh
import bonggoQuery
query = bonggoQuery.takeCommand()
```
# 2. Speaking the Query

```sh
import bonggoQuery
bonggoQuery.speak("Hello World !")
```
# 3.Giving an answer to your custom Query in speaking:
```sh
import bonggoQuery
bonggoQuery.Query.normal_query.speaking("weather report")
```

# 4. Giving an answer to your custom Query in written:
```sh
import bonggoQuery
print(bonggoQuery.Query.normal_query.printing("weather report"))
```

## License

MIT

**Free Software, Hell Yeah!**


License
--------------------

© 2022 Sudip Bera


This repository is licensed under the MIT license. See LICENSE for details.

> MIT License

Copyright (c) 2021 Sudip Bera

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


