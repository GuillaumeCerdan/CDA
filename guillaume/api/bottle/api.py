from bottle import route, request, response, template, run

@route('/hello')
def hello():
    return "Hello World!{}".format(request.query)


@route('/forum')
def display_forum():
    forum_id = request.query.id
    page = request.query.page or '1'
    return template('Forum ID: {{id}} (page {{page}})', id=forum_id, page=page)
    #     page = request.args.get('page', default = 1, type = int)
    #   filter = request.args.get('filter', default = '*', type = str)

run(host='localhost', port=8080, debug=True)