from bottle import route, request, response, template, run
from bottle import request
@route('/hello')
def hello():
    return "Hello World!"


@route('/forum')
def display_forum():
    forum_id = request.query.id
    page = request.query.page or '1'
    return template('Forum ID: {{id}} (page {{page}})', id=forum_id, page=page)

run(host='localhost', port=8080, debug=True)