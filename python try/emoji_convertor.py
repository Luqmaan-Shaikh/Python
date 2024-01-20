# mess = (input(">"))
# words = mess.split(' ')
# emojis = {
# ":)" : "😀",
# ":(" : "😔"
# }
# output = ""
# for word in words:
#     output += emojis.get(word,word) + " "
# print(output)

# creating reusable function
def emoji_convertor(mess):
    words = mess.split(' ')
    emojis = {
    ":)" : "😀",
    ":(" : "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word,word) + " "
    return output

mess = (input(">"))
print(emoji_convertor(mess))
