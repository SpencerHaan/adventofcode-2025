import math

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

    circuits = compose_circuits(junction_boxes, shortest_count=1000)

    circuits = list(reversed(sorted(map(lambda c: len(flatten_node(c)), circuits))))[:3]
    print("Largest circuits product:", math.prod(circuits))


if __name__ == '__main__':
    run()
