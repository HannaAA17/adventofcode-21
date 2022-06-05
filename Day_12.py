from Day_0 import day_data


def day12(pairs, part2):
    NODES = {}

    def get_routs(route: list[str], nodes: list[str], part2):

        routs = []

        for node in nodes:

            if (node == 'start'):
                continue

            elif (node.islower() and (node in route)):
                if part2:
                    routs.extend(get_routs(route+[node], NODES[node], False))
                else:
                    continue

            elif node == 'end':
                routs.append(','.join(route + [node]))

            else:
                routs.extend(get_routs(route+[node], NODES[node], part2))

        return routs

    for pair in pairs:
        r1, r2 = pair.split('-')

        NODES[r1] = list(set(NODES.get(r1, []) + [r2]))
        NODES[r2] = list(set(NODES.get(r2, []) + [r1]))

    routs = get_routs(['start'], NODES['start'], part2)

    return len(routs)


data_in = day_data(12).splitlines()
print(day12(data_in, part2=True))
