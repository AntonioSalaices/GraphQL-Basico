from flask import Flask
from flask import request
from graphene import ObjectType, String, Schema, Int
from flask import json

app = Flask(__name__)


class Query(ObjectType):
    hello = String(name=String(), age=Int())
    goodbye = String()

   
    def resolve_hello(root, info, name, age):
        return f'Hello {name} you are {age} years old!'

    def resolve_goodbye(root, info):
        return 'See ya!'

schema = Schema(query=Query)
# result = schema.execute('{hello(name: "Antonio",age:24)}')
# print(result.data['hello'])

@app.route('/graphql', methods=['POST'])
def graphql():
    data = json.loads(request.data)
    print(data['query'])
    return json.dumps(schema.execute(data['query']).data)


if __name__ == '__main__':
    app.run(port=8000)


