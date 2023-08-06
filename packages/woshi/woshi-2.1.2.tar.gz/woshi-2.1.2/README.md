# woshi
On-the-go HTML Abstraction and Generator for Python.

Woshi is simple, it abstracts XML nesting and leverages CSS3 selectors to append elements into the HTML document!

Version 2.0 is a breaking upgrade, which means the general usage and the internal algorithms were change to make it more flexible and lighter. The package lxml was removed in favor of a custom-made builder function. Only simple CSS3 selectors are supported, but will add support in the upcoming versions.

Here's a sample syntax:
```python
page["tag#id"] = "tag #id.class property='10' > inner text"
```
And scroll down below for more examples.

## Official Release
Current version is 2.0, but more updates are coming soon. Compatible with Python 3.10 or later.

`pip install woshi`


## Usage
**Import Package**
```python
from woshi import Woshi
```

**Initialization**
```python
page = Woshi()

# initializing with a valid HTML text
page = Woshi("<div></div>")

# setting up filename
page = Woshi(filepath="home.html")
```

**Creating elements with an inner text**
```python
page["head"] = "title > Woshi v1.0"
```

**Creating other elements**
Basically, you set the parent selector to append the new element.
```python
# create container box
page["body"] = "div #content"
page["#content"] = "div #box.container.light"

# create the popup text
page["#box"] = "div #title.header > Woshi"
page["#box"] = "div .message data-default='Lorem ipsum...' > Hello, world!"

# populate the action buttons
page["#box"] = "div #action.btn-list"
page["#action"] = "button #btn1.btn.btn-no style='background-color:#b22222;color:#fff;' > CLOSE"
page["#action"] = "button #btn2.btn.btn-maybe > LATER"
```

**Setting Properties**
```python
page["html"] = "lang=en"
page["body"] = "#canvas"
```

**Yield all matches**
```python
for match in page["button"]:
    print(match)
```

**Save to HTML file**
```python
page.save()
page.save("newFile.html")
```