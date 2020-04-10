from kunapipy.kundelik import kundelik

login = "login"
password = "password"

with kundelik.KunAPI(login=login, password=password) as dn:
    print(dn.get_classmates())

    print(dn.get_context())
