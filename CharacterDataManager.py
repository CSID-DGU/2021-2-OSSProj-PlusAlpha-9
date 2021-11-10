import os
import json
from Character import Character

class CharacterDataManager:
    def save(characters):
        char_dict = {"Characters":[char.__dict__ for char in characters]}
        json_str = json.dumps(char_dict)
        json_file = open("characterdata.json", "w")
        json_file.write(json_str)
        json_file.close()

    def load():
        if(os.path.isfile("characterdata.json")):
            try:
                characters = []
                with open("characterdata.json", "r") as json_file:
                    data = json.loads(json_file.read())
                    for i in data["Characters"]:
                        characters.append(Character(**i))
                    json_file.close()
                    return characters
            except:
                print("파일 불러오는 중 에러가 발생했습니다.")
        else:
            print("불러올 데이터가 없습니다.")