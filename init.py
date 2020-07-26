
print("0:rewrite 1:continue")
a = input()
if a=="0":
    f = open("SUMMARY.md","w", encoding="utf-8")
    f.write("# Summary")
    f.write("\n* [Introduction](README.md)")
else:
    f = open("SUMMARY.md","a", encoding="utf-8")

while True:
    print("input rxn name, type 0 to stop: ")
    name = input()
    if name=="0":
        break

    f1 = open(name+".md","w", encoding="utf-8")
    f.write("\n* ["+name+"]("+name+".md)")
    f1.write("# "+name)

    while True:
        print("input rxn key word, type 0 to stop: ")
        key = input()
        if key=="0":
            break
        f1.write("\n"+key)

    f1.close()

f.close()
print("thanks for using, check your files.")
input()
