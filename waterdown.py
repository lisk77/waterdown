fileName = "test"
template = "index"

def main():
    with open(f"{fileName}.md", "r") as f:
        lines = f.readlines()

    splitted = "".join(lines).split("\n")

    interpreted = []

    def paragraphParse(line):
        if "[" and "]" in line:
            _link = line.split("[")
            link_ = line.split("]")
            link = [_link[0], _link[1], link_[-1]]
            comma = link[1].split(",")
            if comma[1].startswith(" "):
                t = list(comma[1])
                t.pop(0)
                y = "".join(t)
            x = y.replace("]", "")
            comma[1] = x
            interpreted.append(f"<p>{link[0]}<a href='{comma[1]}'>{comma[0]}</a>{link[2]}</p>")
        elif "*" in line:
            bold = line.split("*")
            interpreted.append(f"<p>{bold[0]}<b>{bold[1]}</b>{bold[2]}</p>")
        elif "/" in line:
            italic = line.split("/")
            interpreted.append(f"<p>{italic[0]}<i>{italic[1]}</i>{italic[2]}</p>")
        elif "~" in line:
            strike = line.split("~")
            interpreted.append(f"<p>{strike[0]}<s>{strike[1]}</s>{strike[2]}</p>")
        else:
            interpreted.append(f"<p>{line}</p>")

    for i in splitted:
        j = i.split(" ")
        if j[0] == "#":
            interpreted.append(f"<h1>{i[2:]}</h1>")
        if j[0] == "##":
            interpreted.append(f"<h2>{i[3:]}</h2>")
        if j[0] == "###":
            interpreted.append(f"<h3>{i[4:]}</h3>")
        if i == "":
            interpreted.append("<br>")
        if "#" not in j[0] and i != "":
            paragraphParse(i)

    with open(f"{template}.html", "r") as ind:
        htm = ind.readlines()

    html = "".join(htm).split("\n")
    index = html.index("<body>")

    for i,j in enumerate(interpreted):
        html.insert(index+i+1, j)

    with open(f"{fileName}.html", "a") as nind:
        for i in html:
            nind.writelines(i + "\n")
        
if __name__ == "__main__":
    main()
