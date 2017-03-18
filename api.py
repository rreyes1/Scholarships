#!flask/bin/python
from flask import Flask
from flask import request, jsonify
from collections import deque

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/max_scholarship', methods=['POST'])
def max_scholarship():
#    if not request.json:# or not 'data' in request.json:
#        abort(400)
    content = request.json
    A = content['data']
    product, path = max_product_and_path(A)
    return jsonify({'sequence': path, 'total':product})

def max_product_and_path(A):
    n = len(A)
    k = 11
    maxsofar = 0
    finalPath = deque()
    for i in range(len(A)):
        path = deque()
        product = A[i][0]
        path.append(A[i][0])
        first = 0
        for j in range(1,len(A[i])):
            if A[i][j] !=0:
                product = A[i][j] * product
                path.append(A[i][j])
            else:
                product = 0
                path = deque()
            if len(path) == k+1:            
                product = product / A[i][first]
                path.popleft()
                first = first + 1
            if product > maxsofar:
                maxsofar = product
                finalPath = path
    for j in range(len(A[0])):
        path = deque()
        product = A[0][j]
        path.append(A[0][j])
        first = 0
        for i in range(1,len(A)):
            if A[i][j] !=0:
                product = A[i][j] * product
                path.append(A[i][j])
            else:
                product = 0
                path = deque()
            if len(path) == k+1:
                product = product / A[first][j]
                path.popleft()
                first = first + 1
            if product > maxsofar:
                maxsofar = product
                finalPath = path
    for o in range(n):
        path = deque()
        fi,fj = 0,o
        product = A[fi][fj]
        path.append(A[fi][fj])
        for i in range(1,n):
            j = (i + o) % n
            if A[i][j] !=0:
                product = product * A[i][j]
                path.append(A[i][j])
            else:
                product = 0
                path = deque()
            if len(path) == k +1:
                product = product / A[fi][fj]
                path.popleft()
                fi = fi + 1
                fj = (fj + 1) % n
            if product > maxsofar:
                maxsofar = product
                finalPath = path
    return maxsofar, list(finalPath)
if __name__ == '__main__':
    app.run(debug=True)