"""
'AliceInWonderland' challenge.
Solved by Yarden Curiel.
"""


def function_one(text, unknown_base_number_location, number_base, constant):
    """
    This function get a text, location, base for the location and constant number.
    and return the text at the current location base on the given base after multiple
    by the given constant.
`
    :param text: String. for get the characters by there location.
    :param unknown_base_number_location: List. list of string representing the location in the given base.
    :param number_base: Int. base of the locations.
    :param constant: Int. number to multiple by each of the location.

    :return: Tuple. (message: String, base: String, Constant: String), if location
    is out of bound, message will be empty.
    """
    locations = []

    for unknown_base_number in unknown_base_number_location:
        location = 0
        for index, char in enumerate(unknown_base_number[::-1]):
            try:
                number = int(char)
            except ValueError:
                char = char.lower()
                number = ord(char) - 96 + 9
            location = location + number * pow(number_base, index)
        locations.append(location * constant)

    message = ""
    for index, location in enumerate(locations):
        if location < 0:
            message += '/'
        elif location < len(text):
            message += text[location]
        else:
            message = ""
            break

    return message, f'base:{number_base}', f'constant:{constant}'


def get_message_from_location_unknown_base(text, unknown_base_location, max_base, max_constant):
    """

    :param text: String. for get the characters by there location.
    :param unknown_base_location: List. list of string representing the location in the given base.
    :param max_base: Int. max number the location can be represented by.
    :param max_constant: Int. max number the location can be represented by.

    :return: List. return list of potential message with their, base and constant, parameters.
    """
    messages = []

    for constant in range(1, max_constant):
        for base in range(14, max_base):
            potential_message = function_one(text, unknown_base_location, base, constant)
            if potential_message[0] != '':
                messages.append(potential_message)

    return messages


text = "CHAPTER I. Down the Rabbit-Hole Alice was beginning to get very tired of sitting by her sister on the bank, " \
       "and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no " \
       "pictures or conversations in it, ‘and what is the use of a book,’ thought Alice ‘without pictures or " \
       "conversations?’ So she was considering in her own mind (as well as she could, for the hot day made her feel " \
       "very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting " \
       "up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her. There was nothing " \
       "so VERY remarkable in that; nor did Alice think it so VERY much out of the way to hear the Rabbit say to " \
       "itself, ‘Oh dear! Oh dear! I shall be late!’ (when she thought it over afterwards, it occurred to her that " \
       "she ought to have wondered at this, but at the time it all seemed quite natural); but when the Rabbit " \
       "actually TOOK A WATCH OUT OF ITS WAISTCOAT-POCKET, and looked at it, and then hurried on, Alice started to " \
       "her feet, for it flashed across her mind that she had never before seen a rabbit with either a " \
       "waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after " \
       "it, and fortunately was just in time to see it pop down a large rabbit-hole under the hedge. In another " \
       "moment down went Alice after it, never once considering how in the world she was to get out again. "
text = text.replace(" ", "")
unknown_base_numbers = ["36", "17", "17", "44", "12", "3A", "/", "/", "3D", "09", "26A", "18", "1B", "/", "58", "19C", "58", "13", "31", "18"]

top_base = 36
max_constant = 4

potential_messages = get_message_from_location_unknown_base(text, unknown_base_numbers, top_base, max_constant)
[print(message) for message in potential_messages]

#  SAVE PLAINTEXT TO FILE
file = open("Stage 1/messages.txt", "w")
[file.write(str(message) + "\n") for message in potential_messages]
file.close()
