favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print('the following languages have been mentioned: ')
for languague in favorite_languages.values():
    print(languague.title())

print('\nthis store the last iteration of the for', 
      'in this case the last iteration is', languague)

for language in set(favorite_languages.values()):
    print(language.title())