def write_file(file_name, file_content):
    with open(f'{file_name}.txt', 'w', encoding='utf-8') as log_file:
        log_file.write(file_content)
    pass

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a', encoding='utf-8') as log_file:
        log_file.write(append_content)
    pass

def read_file(file_name):
    with open(f'{file_name}.txt', encoding='utf-8') as text_file:
        return text_file.read()
    pass
