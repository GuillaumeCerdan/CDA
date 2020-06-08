import string
text = """Suspendisse ac mauris pharetra, consectetur ante in, lobortis magna. Curabitur interdum, nisi eu lobortis congue, leo augue sagittis ligula, id elementum sem dolor nec diam. 
Mauris tempus ullamcorper est a ultricies. Donec pharetra, massa id ultrices pulvinar, eros nibh feugiat nulla, id consectetur mauris neque non libero.
Phasellus porttitor vel nulla ut lacinia. Pellentesque sit amet urna id purus tincidunt rhoncus eleifend in ipsum. Praesent eu libero sapien. 
Praesent in ex nec nunc blandit faucibus eu id purus.
"""
print(text.translate(str.maketrans('', '', string.punctuation)).replace("\n", " ").split(" "))