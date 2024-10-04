import re

def format_paragraph(text):
    
    text = text.replace("**", "</b>").replace("**", "<b>")
    
    pattern = re.compile(r'</b>')
    url_pattern = re.compile(r'https?://[^\s]+')
    
    text = re.sub(url_pattern, lambda m: f'<a href="{m.group(0).rstrip(")")}" target="_blank" rel="noopener noreferrer">{m.group(0).rstrip(")")}</a>', text)


    text = re.sub(pattern, lambda m: "<b>" if pattern.subn('', text[:m.start()])[1] % 2 == 0 else m.group(0), text)
    text = text.replace('\n','<br>')
    text = text.replace('*','&#8226')
    return text