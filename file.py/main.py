with open("metn.txt", "w", encoding="utf-8") as f:
    f.write("salam dunyali")

with open("metn.txt", "r", encoding="utf-8") as f:
    cumle = f.readline().upper()

with open("new.txt", "w", encoding="utf-8") as ff:
    ff.write(cumle)