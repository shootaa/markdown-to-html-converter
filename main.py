import markdown
import sys

user_input = sys.argv

if len(user_input) == 4:
    if user_input[0] == 'main.py':
        if user_input[1] == 'markdown':
            inputpath = user_input[2]
            outputpath = user_input[3]
            contents = ''
            with open(inputpath) as f:
                contents = f.read()
            html = markdown.markdown(contents)
            with open(outputpath, 'w') as f:
                f.write(html)
            
