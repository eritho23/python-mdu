class Celeb:
    def __init__(self, name, gender, hair_color, eye_color):
        self.name = name
        self.gender = gender
        self.hair_color = hair_color
        self.eye_color = eye_color
    def __eq__(self, other):
        return self.gender == other.gender and self.hair_color == other.hair_color and self.eye_color == other.eye_color

celebs = [
    Celeb("Daniel Radcliffe", "male", "brown", "brown"),
    Celeb("Rupert Grint", "male", "red", "blue"),
    Celeb("Emma Watson", "female", "brown", "brown"),
    Celeb("Selena Gomez", "female", "brown", "brown"),
    #Celeb("Eric Thorburn", "male", "brown", "blue"),
    #Celeb("Alwin Kjell Urban Forslund", "male", "brown", "blue"),
    #Celeb("Jakob Sven Geffen", "female", "brown", "brown"),
    #Celeb("Hannes Gingby", "male", "blonde", "blue")
]

gender = input("Gender: ")
hair_color = input("Hair color: ")
eye_color = input("Eye color: ")

me = Celeb("", gender, hair_color, eye_color)

printed = False
for celeb in celebs:
    #if not celeb.gender == gender:
        #continue
    #if not celeb.hair_color == hair_color:
        #continue
    #if not celeb.eye_color == eye_color:
        #continue
    if celeb == me:
        printed = True
        print(celeb.name)

if not printed:
    print("No celeb found")


