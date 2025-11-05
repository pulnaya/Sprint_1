
types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
} 


def delete_duplicate_tickets():
    unique = set()
    for key, value in tickets.items():
        new_list = []
        for ticket in value:
            if ticket not in unique:
                unique.add(ticket)
                new_list.append(ticket)
        tickets[key] = new_list 


def assign_criticality_level(types, tickets):
    return {types[i] : tickets[i] for i in range(1,6)}


delete_duplicate_tickets()
tickets_by_type = assign_criticality_level(types, tickets)
print(tickets_by_type)