def is_character_match(string1, string2):
	new_string1= list(string1.lower())
	new_string1.sort()
	new_string2= list(string2.lower())
	new_string2.sort()
	new_string1="".join(new_string1)
	new_string2="".join(new_string2)
	return new_string1.replace(" ", "")== new_string2.replace(" ", "")

