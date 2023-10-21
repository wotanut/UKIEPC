tasksDeps = str(input()).split(" ")
tasks = tasksDeps[0]
deps = tasksDeps[1]

furtherDepsStr = []
furtherDeps = []

for _ in range(deps):
    furtherDp = str(input()).split(" ")

    furtherDeps.append([int(furtherDp[0]), int(furtherDp[1])])

    