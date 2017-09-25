import nltk
from nltk.corpus import brown

print(brown.categories())

categories_choice = str(input('What type of categories : '))
display_category = brown.words(categories = categories_choice)

count_text = [w for w in display_category]

print(display_category)

print('There are {} words in this category.'.format(len(count_text)))

count = 0

while True:

	count_letter = [letter for letter in display_category if len(letter) == count]
	count += 1

	if len(count_letter) == 0:
		pass
	else:
		print('#{} : {}'.format(count, len(count_letter)))

	if count > 30:
		break
	else:
		continue