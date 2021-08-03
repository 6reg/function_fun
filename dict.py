animal_sounds = {}

animal_sounds['dog'] = 'woof'
animal_sounds["cat"] = "meow"
animal_sounds['bird'] = 'chirp'

dog_sound = animal_sounds['dog'] # 'woof'

def main():
    for sound in animal_sounds:
        print(animal_sounds[sound])

main()
