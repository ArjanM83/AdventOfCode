import graphviz


class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.edges_list = []
        for line in self.lines_list:
            node_from, node_to_string = line.split(': ')
            for node_to in node_to_string.split(' '):
                self.edges_list.append((node_from, node_to))
                self.edges_list.append((node_to, node_from))
        self.edges_list = list(set(self.edges_list))

        self.group_1_dict = {}
        self.group_2_dict = {}

    def solve_part_1(self):
        g = graphviz.Graph('G', filename='AoC_25_1.gv', format='svg', engine='neato')
        for node_from, node_to in self.edges_list:
            g.edge(node_from, node_to)
        g.view()

        # after viewing image:
        # cut edges example: hfx-pzl, bvb-cmg, nvd-jqt
        # cut edges input: thx-frl, lhg-llm, fvm-ccp

        # group 1
        new_node_found = self.edges_list[0][0]
        self.group_1_dict[new_node_found] = 1
        while new_node_found:
            new_node_found = False
            for node_from, node_to in self.edges_list:
                if node_from in self.group_1_dict:
                    if node_to not in self.group_1_dict:
                        new_node_found = True
                        self.group_1_dict[node_to] = 1

        # group 2
        for node_from, node_to in self.edges_list:
            if node_from not in self.group_1_dict:
                self.group_2_dict[node_from] = 1
                self.group_2_dict[node_to] = 1

        return len(self.group_1_dict) * len(self.group_2_dict)


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
