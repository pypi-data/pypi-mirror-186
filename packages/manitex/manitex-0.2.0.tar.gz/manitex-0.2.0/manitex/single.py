"""
single.py

Construct a single document from a latex main document that uses input commands 
to support composition and collaboration.
"""
input_re = re.compile(r'\\input\{(.*?)\}')

text = """
blah blah

\input{abstract}
blah blaha
blah blaha
blah blaha
\input{introduction}
"""