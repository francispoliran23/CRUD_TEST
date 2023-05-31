from flask import Flask


app = Flask(__name__)


@app.route("/home")
def home():
    return "Hello World"


# import controller.user_connection as user_connection
# import controller.product as product
# import controller.__init__ as __init__

from controller import user_connection, product, __all__, category


# hahahahah
        
# if __name__ == "__main__":
#     app.run(debug=True)