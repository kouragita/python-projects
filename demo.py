file = open("demo.txt", 'w')
file.write("NWOG acts as a magnet for a ranging market ")
file.close()


file = open("demo.txt", 'r')
content = file.read()
print(content)
file.close()

file = open("demo.txt", 'a')
file.write("note the consequent encroachment of it")
file.close()
