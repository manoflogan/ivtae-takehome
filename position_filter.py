# Position filter logic
# Don't forget to write tests (python nose is installed)
# Some code repetition is acceptable for the purpose of this evaluation
# Do not rename the 4 solution methods

import collections

def filter_solution_1(genome_data, filter_definition):
    # TODO fill this out for task #1
    genome_dict = dict()
    for (entry, base) in genome_data:
      genome_dict[entry] = base
    output = []
    for (start, end) in filter_definition:
      filter_solution = [[index, genome_dict[index]] for index in range(start, end) if index in genome_dict]
      output.extend(filter_solution)
    return output


def filter_solution_2(genome_data, filter_definition):
    genome_dict = dict()
    matched_keys = dict()
    for (entry, base) in genome_data:
        genome_dict[entry] = base
        index = 0
        matched_keys[entry] = None
        while index < len(base):
            matched_keys[entry + index] = entry
            index += 1
    output = []
    for (start, end) in filter_definition:
        for index in range(start, end):
            if index in genome_dict:
                output.append([index, genome_dict[index]])
            elif index in matched_keys:
                entry = matched_keys[index]
                output.append([entry, genome_dict[entry]])
    return output



def filter_solution_3(genome_data, filter_definition):
    genome_dict = dict()
    for (entry, base) in genome_data:
        index = 0
        while index < len(base):
            genome_dict[entry + index] = base[index]
            index += 1

    output = []
    for (start, end) in filter_definition:
        filtered_output = [[index, genome_dict[index]] for index in range(start, end) if index in genome_dict]
        output.extend(filtered_output)
    return output


def filter_solution_4(genome_data, filter_definition):
    # TODO fill this out for task
    #4
    genome_dict = collections.defaultdict(list)
    for (base, entry) in genome_data:
        index = 0
        while index < len(entry):
            genome_dict[base + index].append(entry[index])
            index += 1
    output = []
    for (start, end) in filter_definition:
        for index in range(start, end):
            if index not in genome_dict:
                continue
            base_list = genome_dict[index]
            filtered_output = [[index, key] for key in base_list]
            output.extend(filtered_output)
    return output


if __name__ == '__main__':
    genome_data = [[5, "GAT"], [15, "G"], [19, "TC"], [22, "T"]]
    filter_data = [[6, 7], [15, 20]]
    print (filter_solution_3(genome_data, filter_data))
