from gnutools.utils import id_generator
import json

class DirNode:
    def __init__(self, node):
        self.node = node

    def save(self, d):
        output_file = f"{self.node}/x{id_generator()}.json"
        json.dump(d, open(output_file,"w"), indent=4)
        return output_file
