#This function arranges the weather information received from a page in a nice and proper way.
def str_manipulations(description):



    for character in description:

        if character == "\n":
            new_description = description.replace(character, " ") # This condition switches between adding line breaks and
                                                                  # adjusting word spacing.

        elif character == ":":
            new_description = description.replace(character, "\n") # This condition replaces ":" with a line break.
        else:
            continue

    return (new_description)





