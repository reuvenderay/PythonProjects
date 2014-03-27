def reverse(string):
    #takes a string and returns it in reverse
    length = len(string)-1
    result = ""
    while length >= 0:
        result += string[length]
        length -= 1
    print result
        
reverse("this process reverses any string you give it!")
