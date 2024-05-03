entry_var = r'{"response": "```python\nfrom transformers import pipeline\n\nclassifier = pipeline(\"sentiment-analysis\")\nresult = classifier(\"I love using transformers. The library is amazing!\")\nprint(result)\n``` \n"}'

def line_partition(raw_code):
    r = raw_code[25:-10]
    return recursive_line_seperator(r)

def recursive_line_seperator(string, line_catch =[]):

    temp_line_catch = line_catch
    current_partition = string.partition(r'\n')
    if len(current_partition[2]) < 1:
        return line_catch
    temp_line_catch.append(current_partition[0])
    return recursive_line_seperator(current_partition[2], temp_line_catch)

def delete_silly_slash(list_of_python_lines):
    lines =list_of_python_lines
    fixed_lines = []
    for line in lines:
        linefix1 = line.replace("\\\"","\"")
        fixed_lines.append(linefix1)
    
    return fixed_lines

final_lines = delete_silly_slash(line_partition(entry_var))

file = open("megapog.py","w+")

for line in final_lines:
    file.writelines(line+ '\n')
