import webbrowser
from string import Template
import os
# Documentation: https://docs.python.org/3/library/string.html#template-strings

file_dir_path_str = os.path.dirname(os.path.abspath(__file__))

print("os.getcwd() = " + os.getcwd())

TEMPLATE_FILE_STR = file_dir_path_str + "/web/template.html"

SOURCE_INDEX_FILE_STR = file_dir_path_str + "/web/index.content.html"
SOURCE_USER_GUIDE_FILE_STR = file_dir_path_str + "/web/user_guide.content.html"

TARGET_INDEX_FILE_STR = file_dir_path_str + "/public/index.html"
TARGET_USER_GUIDE_FILE_STR = file_dir_path_str + "/public/user_guide.html"

# CONTENT_STR = ".content"
# SUFFIX_STR = ".html"

with open(TEMPLATE_FILE_STR, "r") as template_file,\
open(SOURCE_INDEX_FILE_STR, "r") as index_content_file,\
open(SOURCE_USER_GUIDE_FILE_STR, "r") as user_guide_content_file:
    template = Template(template_file.read())
    home_str = template.substitute(content=index_content_file.read())
    user_guide_str = template.substitute(content=user_guide_content_file.read())

with open(TARGET_INDEX_FILE_STR, "w+") as index_file,\
open(TARGET_USER_GUIDE_FILE_STR, "w+") as user_guide_file:
    index_file.write(home_str)
    user_guide_file.write(user_guide_str)

webbrowser.open(file_dir_path_str + "/public/index.html")

"""

About:
History, more description, about SunyataZero, 

Participate:
Suggest a feature, an improvement
Report a bug

Main page
Screenshots

User guide
Features

News

-> Question and tag ideas
import from application file?


"""
