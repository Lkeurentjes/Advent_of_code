from collections import defaultdict, deque

def is_update_valid(update, rules):
    # Loop over update, to check that reversed numbers are not in update
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if (update[j], update[i]) in rules:
                return False

    return True

def find_middle_page(update):
    # return the middle number at the middle index
    mid_index = len(update) // 2
    return update[mid_index]

def order_rules(rules):
    directed_graph = defaultdict(list) # graph with all the rules
    connection_counter = defaultdict(int) # number of connected edges per part of "node"
    nodes = set() # set of all the nodes

    # add the nodes to the graph and connection counter
    for a, b in rules:
        directed_graph[a].append(b)
        connection_counter[b] += 1
        nodes.update([a, b])

    # add the node with none connections also to connection counter
    for node in nodes:
        connection_counter.setdefault(node, 0)

    # start with no connection rules
    queue = deque([node for node in nodes if connection_counter[node] == 0])
    ordered_list = []
    while queue:
        current = queue.popleft()
        ordered_list.append(current)

        for neighbor in directed_graph[current]:
            # work up by dismissing the nodes which are already in the list
            connection_counter[neighbor] -= 1
            if connection_counter[neighbor] == 0:
                queue.append(neighbor)

    return ordered_list



def reorder_update(update, rules):
    rules_to_order = []
    for a, b in rules:
        if a in update and b in update:
            rules_to_order.append((a, b))
    return order_rules(rules_to_order)



with open('2024-05-Print_Queue.txt') as f:
    lines = f.read().splitlines()
    rules = [tuple(map(int, line.split('|'))) for line in lines[:lines.index('')]]
    updates = [list(map(int, line.split(','))) for line in lines[lines.index('') + 1:]]

    result ,result_incorrect  = 0, 0
    for update in updates:
        if is_update_valid(update, rules):
            result += find_middle_page(update)
        else:
            result_incorrect += find_middle_page(reorder_update(update, rules))

    print("Part 1, the result of the middle indexes",result)
    print("Part 2, the result of the middle indexes",result_incorrect)
