while(True):
    dict = {"atul": "cute", "shubham": "simple ", "harshita": "cartoon", "atul sinha": "bade log", "khusi": "taikondu",
            "abhishek": "tesnsion free","abhijeet":"cr","suraj":" serious ladka", "golu":"Ara jila ghar ba kon baat k dar ba","aditya":"bestiiii","jivan":"legend"}
    print("Enter the name to know about him/her")
    print("atul")
    print("shubham")
    print("harshita")
    print("atul sinha")
    print("khusi")
    print("abhishek")
    print("abhijeet")
    print("suraj")
    print("golu")
    print("aditya")
    print("jivan")

    key = input("Enter one of the name\n")

    print(dict[key])
    print("do you want to conti...")
    xy=input()
    if xy=="yes":
        continue
    else:
        break
