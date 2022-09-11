fileName = input("Waterdown file name: ")
template = "index"

with open(f"{fileName}.wd", "r") as f:
    lines = f.readlines()

splitted = "".join(lines).split("\n")

interpreted = []

def generalParse(line):
    print("cum")

def paragraphParse(line):
    if "{" and "}" in line:
        _line = list(line)
        _line.pop(-1)
        image = _line[1:]
        if "," in image:
            before, after = "".join(image).split(",")
            width, height = "".join(after).split("x")
            if " " in list(width):
                _width = list(width)
                _width.pop(0)
                width = "".join(_width)
        interpreted.append(f"<img src='{before}' width='{width}' height='{height}'/>")
    elif "[" and "]" in line:
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
        if list(line)[0] == "-":
            return
        
        interpreted.append(f"<p>{line}</p>")

def main():
    uListItems = []
    oListItems = []
    for i in splitted:
        j = i.split(" ")
        if j[0] == "#":
            interpreted.append(f"<h1>{i[2:]}</h1>")
        if j[0] == "##":
            interpreted.append(f"<h2>{i[3:]}</h2>")
        if j[0] == "###":
            interpreted.append(f"<h3>{i[4:]}</h3>")
        if i == "":
            if len(uListItems) == 0 and len(oListItems) == 0:
                interpreted.append("<br>")
        if j[0] == "-":
            if len(uListItems) == 0:
                interpreted.append(f"<ul>")
            uListItems.append(f"<li>{i[2:]}</li>")
        if j[0] == "--":
            if len(oListItems) == 0:
                interpreted.append("<ol>")
            oListItems.append(f"<li>{i[3:]}</li>")
        if "-" not in i:
            if len(uListItems) != 0:
                for item in uListItems:
                    interpreted.append(item)
                interpreted.append("</ul>")
                uListItems = []
            if len(oListItems) != 0:
                for item in oListItems:
                    interpreted.append(item)
                interpreted.append("</ol>")
                oListItems = []
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
