from textwrap import wrap
lorem = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
    when an unknown printer took a galley of type and scrambled it 
    to make a type specimen book. It has survived not only five centuries, 
    but also the leap into electronic typesetting, remaining essentially 
    unchanged. It was popularised in the 1960s with the release of Letraset sheets 
    containing Lorem Ipsum passages, and more recently with desktop 
    publishing software like Aldus PageMaker including versions of Lorem Ipsum."""
words = "Hey there mate, it’s nice to finally meet you!"

def just(text:str, width:int=16):
    """Formatuje tekst na podaną długość linii.
    text[string] -> text for formatting
    width[int] (default 16) -> max line width
    
    return[list] -> list with formatting line (line = element)
    """
    return wrap(text, width=width)

print(just(words, 16))

print(just(lorem, 24))



# w pdf nie mówiono nic o zakazie korzystaniu z textwrapa :D