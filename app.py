from bottle import route, run, request, abort, static_file

from fsm import TocMachine
import os


VERIFY_TOKEN = "123456789"
machine = TocMachine(
    states=[
        'user',
        'state1',#choose type
        'state2',#choose top3 movies
        'state3',#choose movies with high score
        'state4',#link for movie introduction
        'choice',#choose one movie
        'theather',#choose one theather
        'intro',#introduction of the bot
        'contact',#reflect the problem
        'theather2',
        'theather3',
        'hug',
        'test'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'contact',
            'conditions': 'is_going_to_contact'
        },
        {
             'trigger': 'advance',
            'source': 'user',
            'dest': 'hug',
            'conditions': 'is_going_to_hug'
        },
        {
             'trigger': 'advance',
            'source': 'user',
            'dest': 'test',
            'conditions': 'is_going_to_test'
        },
        {
             'trigger': 'advance',
            'source': 'user',
            'dest': 'intro',
            'conditions': 'is_going_to_intro'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'choice',
            'conditions': 'is_going_to_choice'
        },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'choice',
            'conditions': 'is_going_to_choice'
        },
        {
            'trigger': 'advance',
            'source': 'choice',
            'dest': 'theather',
            'conditions': 'is_going_to_theather'
        },
        {
            'trigger': 'advance',
            'source': 'choice',
            'dest': 'theather2',
            'conditions': 'is_going_to_theather2'
        },
        {
            'trigger': 'advance',
            'source': 'choice',
            'dest': 'theather3',
            'conditions': 'is_going_to_theather3'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'intro',
                'contact',
                'hug',
                'state4',
                'theather',
                'theather2',
                'theather3',
                'test'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')

PORT = os.environ['PORT']
if __name__ == "__main__":
    run(host="0.0.0.0", port=PORT, debug=True, reloader=True)
