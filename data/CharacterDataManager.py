import json
import os

from object.Character import Character


class CharacterDataManager:
    def save(characters):
        char_dict = {"Characters":characters}
        json_str = json.dumps(char_dict,indent=4,default=Character.json_dump_obj)
        json_file = open("./data/characterdata.json", "w")
        json_file.write(json_str)
        json_file.close()

    def load():
        if(os.path.isfile("./data/characterdata.json")):
            try:
                characters = []
                with open("./data/characterdata.json", "r") as json_file:
                    data = json.loads(json_file.read())
                    for i in data["Characters"]:
                        characters.append(Character(**i))
                    json_file.close()
                    return characters
            except:
                print("파일 불러오는 중 에러가 발생했습니다.")
        else:
            print("불러올 데이터가 없습니다.")
