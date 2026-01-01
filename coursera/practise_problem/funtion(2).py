# 1. DEFINE the function with a placeholder 'lang'
def greet(lang):
    if lang == "Spanish":
        print("Hola")
    elif lang == "French":
        print("Bonjour")
    elif lang == "Telugu":
        print("Namaskaram")
    else:
        print("Hello")

# 2. CALL the function with different arguments
greet("Spanish")
greet("Telugu")
greet("Alien Language")