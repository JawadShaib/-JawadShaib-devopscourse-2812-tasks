from flask import Flask

# # Excersize 1
#
#
# try:
#     a = 1 / 5
# except:
#     raise ZeroDivisionError
#
# # Excersize 2
#
# "yes the following code is legal , when debugging it will enter the try and will print finally even if execption " \
# "raised "
#
# # Excersize 3
# " this exception will handle all type of exception ( there is no specific )"
#
# # Excersize 4
# "the exception is not fully formative because it can handle almost all type of errors "
# # Excersize 5
# "a:the IOError is raised when an input output operation like open() file, or a method or a simple print statement is " \
# "failed due to IO reasons like “Disk full” or “File not found”. The IOError class is inherited from the "
#
# 'b:dividing number by zero will cause an error'
# # Excersize 6
# file = open('names.txt', 'w')
# with file:
#     file.write("jawad shaib")
#
# # Excersize 7
#
# file = open('names.txt', 'r')
# with file:
#     line = file.readline()
#     print(line)
#
# # Excersize 8
#
# text = input(" hey enter your thoughts here:  ")
# file = open('names.txt', 'w')
# with file:
#     file.write(text)

# Excersize 9 (flask)
app = Flask(__name__)


@app.route("/content")
def read():
    return open("names.txt").read(), 200


@app.route("/register")
def register():
    open("words.txt", "w").write("hello")
    return "success", 20


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True, port=30000)
