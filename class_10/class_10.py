persons = {
    "3500000000000": {
        "name": "John",
        "age": 30,
        "gender": "male",
        "address":{
            "apt. no":"417",
            "city":"karachi"
        }
    },
    "350000000001": {
        "name": "Aun",
        "age": 24,
        "gender": "male"
    }
}
persons["3500000000000"]["address"]["city"] = "London"
persons.pop("3500000000000")
print(persons)
