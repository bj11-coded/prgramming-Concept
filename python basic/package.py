import camelcase 

c = camelcase.CamelCase()

text = "hello world"
print(c.hump(text))  # converts the text to CamelCase