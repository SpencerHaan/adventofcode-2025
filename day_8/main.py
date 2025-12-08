# import math

import puzzles
from puzzles import Node, Point3D


def junction_box_pairs_by_distance(junction_boxes):
    junction_box_distances = dict()
    for i, left in enumerate(junction_boxes):
        for right in junction_boxes[i + 1:]:
            distance = left.get_value().distance_to(right.get_value())
            junction_box_distances[distance] = (left, right)
    return junction_box_distances


def compose_circuits(junction_boxes, shortest_count = 10):
    junction_box_pairs = junction_box_pairs_by_distance(junction_boxes)

    circuits = set()
    for distance in sorted(junction_box_pairs)[:shortest_count]:
        left, right = junction_box_pairs[distance]

        left = left.get_root()
        right = right.get_root()

        if left == right:
            continue

        left.add_child(right)
        circuits.add(left)

        if right in circuits:
            circuits.remove(right)

    return circuits

def last_disconnected_pair(junction_boxes):
    junction_box_pairs = junction_box_pairs_by_distance(junction_boxes)

    last_connected_pair = None
    circuits = set()
    for distance in sorted(junction_box_pairs):
        left, right = junction_box_pairs[distance]

        left_root = left.get_root()
        right_root = right.get_root()

        if left_root == right_root:
            continue

        left_root.add_child(right_root)
        circuits.add(left_root)

        if right_root in circuits:
            circuits.remove(right_root)

        last_connected_pair = (left, right)

    return last_connected_pair


def flatten_node(root):
    flattened = {Node(root.get_value())}
    for child in root:
        flattened.update(flatten_node(child))
    return flattened


def run():
    junction_boxes = []
    for junction_box in puzzles.lines("day_8"):
        x, y, z = map(int, junction_box.split(","))
        junction_boxes.append(Node(Point3D(x, y, z)))

    # Part 1
    # circuits = compose_circuits(junction_boxes, shortest_count=1000)
    #
    # circuits = list(reversed(sorted(map(lambda c: len(flatten_node(c)), circuits))))[:3]
    # print("Largest circuits product:", math.prod(circuits))

    # Part 2
    left, right = last_disconnected_pair(junction_boxes)
    print("X coord product:", left.get_value().x * right.get_value().x)


if __name__ == '__main__':
    run()
