import json


# Class
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("John", 28)


# Custom Encoder
def custom_encoder(obj):
    if isinstance(obj, User):
        return {"name": obj.name, "age": obj.age, obj.__class__.__name__: True}
    else:
        print("Object can not be serialized")


userJSON = json.dumps(user, default=custom_encoder, indent=4, sort_keys=True)
print(userJSON)


# Custom Decoder
def custom_decoder(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct


user = json.loads(userJSON, object_hook=custom_decoder)
print(user.name, user.age)
