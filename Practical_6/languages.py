from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

print()
print("The dynamically typed languages are:")

language_list = [python, ruby, visual_basic]
for line in language_list:
    if line.is_dynamic():
        print(line.name)
