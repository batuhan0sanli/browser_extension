# Browser Extension

A tool to download and use browser extensions on Selenium/Browsers!

## Installation

```bash
pip install browser-extension
```

## Usage

### For Download and Use

```python
from browser_extension import ChromeExtension

extension_url = '<extension_url>'
chrome_version = '<chrome_version>'

path = ChromeExtension(extension_url, chrome_version).download()
print(path)
```

### Use With Selenium

```python
from browser_extension import ChromeExtension

# Load the extension
extension_url = '<extension_url>'
chrome_version = '<chrome_version>'
path = ChromeExtension(extension_url, chrome_version).download()

# Load the extension in Selenium
options = webdriver.ChromeOptions()
options.add_extension(path)
driver = webdriver.Chrome(options=options)  # or add to your existing options
```

