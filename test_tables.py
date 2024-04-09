from flask import Flask, request, jsonify

app = Flask(__name__)

tickets = [
    {"id": 1, "title": "Ticket 1", "description": "Description for Ticket 1", "priority": "High", "severity": "Medium", "category": "Bug", "assigned_to": "user1"},
    {"id": 2, "title": "Ticket 2", "description": "Description for Ticket 2", "priority": "Low", "severity": "Low", "category": "Feature Request", "assigned_to": "user1"},
    {"id": 3, "title": "Ticket 3", "description": "Description for Ticket 3", "priority": "Medium", "severity": "High", "category": "Bug", "assigned_to": "user1"},
    {"id": 4, "title": "Ticket 4", "description": "Description for Ticket 4", "priority": "Low", "severity": "Low", "category": "Feature Request", "assigned_to": "user1"},
    {"id": 5, "title": "Ticket 5", "description": "Description for Ticket 5", "priority": "High", "severity": "Medium", "category": "Bug", "assigned_to": "user1"},
    {"id": 6, "title": "Ticket 6", "description": "Description for Ticket 6", "priority": "Low", "severity": "Low", "category": "Feature Request", "assigned_to": "user1"},
    {"id": 7, "title": "Ticket 7", "description": "Description for Ticket 7", "priority": "Medium", "severity": "High", "category": "Bug", "assigned_to": "user1"},
    {"id": 8, "title": "Ticket 8", "description": "Description for Ticket 8", "priority": "Low", "severity": "Low", "category": "Feature Request", "assigned_to": "user1"},
    {"id": 9, "title": "Ticket 9", "description": "Description for Ticket 9", "priority": "High", "severity": "Medium", "category": "Bug", "assigned_to": "user1"},
    {"id": 10, "title": "Ticket 10", "description": "Description for Ticket 10", "priority": "Low", "severity": "Low", "category": "Feature Request", "assigned_to": "user1"},
    {"id": 11, "title": "Ticket 11", "description": "Description for Ticket 11", "priority": "Medium", "severity": "High", "category": "Bug", "assigned_to": "user1"},
    {"id": 12, "title": "Ticket 12", "description": "Description for Ticket 12", "priority": "Low", "severity": "Low", "category": "Feature Request", "assigned_to": "user1"},
    {"id": 13, "title": "Ticket 13", "description": "Description for Ticket 13", "priority": "High", "severity": "Medium", "category": "Bug", "assigned_to": "user1"},
    {"id": 14, "title": "Ticket 14", "description": "Description for Ticket 14", "priority": "Low", "severity": "Low", "category": "Feature Request", "assigned_to": "user1"},
    {"id": 15, "title": "Ticket 15", "description": "Description for Ticket 15", "priority": "Medium", "severity": "High", "category": "Bug", "assigned_to": "user1"},
    {"id": 16, "title": "Ticket 16", "description": "Description for Ticket 16", "priority": "Low", "severity": "Low", "category": "Feature Request", "assigned_to": "user1"},
    {"id": 17, "title": "Ticket 17", "description": "Description for Ticket 17", "priority": "High", "severity": "Medium", "category": "Bug", "assigned_to": "user1"},
    {"id": 18, "title": "Ticket 18", "description": "Description for Ticket 18", "priority": "Low", "severity": "Low", "category": "Feature Request", "assigned_to": "user1"},
    {"id": 19, "title": "Ticket 19", "description": "Description for Ticket 19", "priority": "Medium", "severity": "High", "category": "Bug", "assigned_to": "user1"},
    {"id": 20, "title": "Ticket 20", "description": "Description for Ticket 20", "priority": "Low", "severity": "Low", "category": "Feature Request", "assigned_to": "user1"}
]


@app.route('/')
def welcome():
    return 'Welcome to the Ticketing System'

@app.route('/api/tickets/<user_id>', methods=['GET'])
def get_user_tickets(user_id):
    user_tickets = [ticket for ticket in tickets if ticket['assigned_to'] == user_id]
    return jsonify(user_tickets)

@app.route('/api/assign/<username>', methods=['POST'])
def assign_ticket(username):
    data = request.json
    ticket_id = data.get('ticket_id')
    if not ticket_id:
        return jsonify({'error': 'Ticket ID is required'}), 400
    ticket = next((ticket for ticket in tickets if ticket['id'] == ticket_id), None)
    if not ticket:
        return jsonify({'error': 'Ticket not found'}), 404
    ticket['assigned_to'] = username
    return jsonify({'message': f'Ticket {ticket_id} assigned to {username}'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
