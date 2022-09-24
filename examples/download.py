from browser_extension import ChromeExtension

extension_url = "https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi"
chrome_version = '105.0.5195'
path = ChromeExtension(extension_url, chrome_version).download()

print(path)
