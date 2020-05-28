movies = []
movies.append({"id": 1, "title": "Movie 1 ", "flagValue": 1})  # 00000000000000000001
movies.append({"id": 2, "title": "Movie 2 ", "flagValue": 2})  # 00000000000000000010
movies.append({"id": 3, "title": "Movie 3 ", "flagValue": 4})  # 00000000000000000100
movies.append({"id": 4, "title": "Movie 4 ", "flagValue": 8})  # 00000000000000001000
movies.append({"id": 5, "title": "Movie 5 ", "flagValue": 16})  # 00000000000000010000
movies.append({"id": 6, "title": "Movie 6 ", "flagValue": 32})  # 00000000000000100000
movies.append({"id": 7, "title": "Movie 7 ", "flagValue": 64})  # 00000000000001000000
movies.append({"id": 8, "title": "Movie 8 ", "flagValue": 128})  # 00000000000010000000
movies.append({"id": 9, "title": "Movie 9 ", "flagValue": 256})  # 00000000000100000000
movies.append({"id": 10, "title": "Movie 10", "flagValue": 512})  # 00000000001000000000
movies.append(
    {"id": 11, "title": "Movie 11", "flagValue": 1024}
)  # 00000000010000000000
movies.append(
    {"id": 12, "title": "Movie 12", "flagValue": 2048}
)  # 00000000100000000000
movies.append(
    {"id": 13, "title": "Movie 13", "flagValue": 4096}
)  # 00000001000000000000
movies.append(
    {"id": 14, "title": "Movie 14", "flagValue": 8192}
)  # 00000010000000000000
movies.append(
    {"id": 15, "title": "Movie 15", "flagValue": 16384}
)  # 00000100000000000000
movies.append(
    {"id": 16, "title": "Movie 16", "flagValue": 32768}
)  # 00001000000000000000
movies.append(
    {"id": 17, "title": "Movie 17", "flagValue": 65536}
)  # 00010000000000000000
movies.append(
    {"id": 18, "title": "Movie 18", "flagValue": 131072}
)  # 00100000000000000000
movies.append(
    {"id": 19, "title": "Movie 19", "flagValue": 262144}
)  # 01000000000000000000
movies.append(
    {"id": 20, "title": "Movie 20", "flagValue": 524288}
)  # 10000000000000000000

flagValue = 1
for movie in movies:
    # print(movie)
    movie["flagValue"] = flagValue
    flagValue *= 2

users = []
users.append(
    {"id": 1, "title": "Usuário 1 ", "selecao": 9}
)  # 00000000000000001001 - Filmes 1 + 4
users.append(
    {"id": 2, "title": "Usuário 2 ", "selecao": 1}
)  # 00000000000000000001 - Filmes 1
users.append(
    {"id": 3, "title": "Usuário 3 ", "selecao": 8}
)  # 00000000000000001001 - Filmes 4
users.append(
    {"id": 4, "title": "Usuário 4 ", "selecao": 32768}
)  # 00001000000000000000 - Filmes 16
users.append(
    {"id": 5, "title": "Usuário 5 ", "selecao": 32769}
)  # 00001000000000000001 - Filmes 1 + 16
users.append(
    {"id": 6, "title": "Usuário 6 ", "selecao": 32777}
)  # 00001000000000000001 - Filmes 1 + 4 + 16
users.append(
    {"id": 7, "title": "Usuário 7 ", "selecao": 524288}
)  # 10000000000000000000 - Filmes 20
users.append(
    {"id": 8, "title": "Usuário 8 ", "selecao": 9}
)  # 00000000000000001001 - Filmes 1 + 4
users.append(
    {"id": 9, "title": "Usuário 9 ", "selecao": 0}
)  # 00000000000000000000 - CHATÃO!
users.append(
    {"id": 10, "title": "Usuário 10 ", "selecao": 0}
)  # 00000000000000000000 - CHATONA

flagTotal = 0
for movie in movies:
    flagTotal += movie["flagValue"]

print(f"flagTotal: {flagTotal}")

a = users[8]
for b in users:
    if a["id"] != b["id"]:
        gostei_a = a["selecao"]
        gostei_b = b["selecao"]
        nao_gostei_a = flagTotal - a["selecao"]
        nao_gostei_b = flagTotal - b["selecao"]

        gostei = {}
        gostei["match"] = gostei_a & gostei_b
        gostei["count_match"] = bin(gostei["match"]).count("1")
        gostei["a"] = gostei_a - gostei["match"]
        gostei["count_a"] = bin(gostei["a"]).count("1")
        gostei["b"] = gostei_b - gostei["match"]
        gostei["count_b"] = bin(gostei["b"]).count("1")

        nao_gostei = {}
        nao_gostei["match"] = nao_gostei_a & nao_gostei_b
        nao_gostei["count_match"] = bin(nao_gostei["match"]).count("1")
        nao_gostei["a"] = nao_gostei_a - nao_gostei["match"]
        nao_gostei["count_a"] = bin(nao_gostei["a"]).count("1")
        nao_gostei["b"] = nao_gostei_b - nao_gostei["match"]
        nao_gostei["count_b"] = bin(nao_gostei["b"]).count("1")

        score = 0
        if gostei["count_a"] == 0 and gostei["count_b"] == 0:
            score = 1
        else:
            score = gostei["count_match"] / (
                gostei["count_match"] + gostei["count_a"] + gostei["count_b"]
            )

        if nao_gostei["count_a"] == 0 and nao_gostei["count_b"] == 0:
            score += 1
        else:
            score += nao_gostei["count_match"] / (
                nao_gostei["count_match"]
                + nao_gostei["count_a"]
                + nao_gostei["count_b"]
            )

        print(f"{a['id']} - {b['id']} - gostei: {gostei}")
        print(f"{a['id']} - {b['id']} - nao_gostei: {nao_gostei}")
        print(f"{a['id']} - {b['id']} - score: {score/2}")

        # matchMovies = []
        # for movie in movies:
        #     if movie['flagValue'] & match == movie['flagValue']:
        #         matchMovies.append(movie)
        #             print(matchMovies)
