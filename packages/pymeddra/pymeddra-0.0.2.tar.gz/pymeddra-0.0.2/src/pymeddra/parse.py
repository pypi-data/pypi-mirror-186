import os
import re
from pymeddra.tree import Node, Level


def _create_child_if_not_exists(parent: Node, child_id: str, child_term: str):
    parent_level = parent.level
    # get child level if still appropriate
    child_level = parent_level + 1
    if child_level is None:
        return None
    # get child if exists
    if child_id in parent.children:
        child = parent.children[child_id]
    # create child if not exists
    else:
        child = Node(id=child_id, term=child_term, level=child_level, parent=parent)
        parent.children.update({child_id: child})
    return child


def parse_mdhier(data_dir):
    file = os.path.join(data_dir, "mdhier.asc")
    if not os.path.isfile(file):
        raise FileNotFoundError(f"File {file} not found.")

    # get regex
    id_regex = r"\d{8}"
    term_regex = r"[^$]*"
    regex = rf"({id_regex})\$({id_regex})\$({id_regex})\$({id_regex})\$({term_regex})\$({term_regex})\$({term_regex})\$({term_regex})\$({term_regex})\$\$({id_regex})\$[YN]\$"
    regex = re.compile(regex)

    # get data
    lines = []
    with open(file, "r") as fp:
        lines = fp.readlines()
    text = "\n".join(lines)

    matches = regex.findall(text)

    print(f"Read {len(lines)} lines.")
    if len(lines) != len(matches):
        raise RuntimeError(
            f"Error parsing mdhier.asc. Expected number of matches to match number of lines."
        )

    # create ontology tree
    root = Node(id="root", term="root", level=Level.ROOT)
    for match in matches:
        (
            llt_id,
            hlt_id,
            hltg_id,
            soc_id,
            llt_term,
            hlt_term,
            hltg_term,
            soc_term_1,
            soc_term_2,
            _,
        ) = match
        # recursivelty add the nodes specified by this line
        soc_node = _create_child_if_not_exists(root, soc_id, soc_term_1)
        hltg_node = _create_child_if_not_exists(soc_node, hltg_id, hltg_term)
        hlt_node = _create_child_if_not_exists(hltg_node, hlt_id, hlt_term)
        llt_node = _create_child_if_not_exists(hlt_node, llt_id, llt_term)

    # print(llt_node.parent == hlt_node)
    # print(hlt_node.parent == hltg_node)
    # print(hltg_node.parent == soc_node)
    # print(soc_node.parent == root)

    # print(Level.SOC < Level.LLT)
    # print(Level.SOC > Level.LLT)
    # print(Level.SOC - Level.LLT)

    # print(soc_node.get_parent_at_level(Level.ROOT))
    # print(soc_node.get_parent_at_level(Level.SOC))
    # print(soc_node.get_parent_at_level(Level.LLT))
    # print(llt_node.get_parent_at_level(Level.SOC))

    # print(root.lookup_term("COVID-19 pneumonia"))
    # print(root.lookup_term("COVID-19 pneumonia")[0].parent)
    return root


if __name__ == "__main__":
    data_dir = (
        "/Users/kldooste/Documents/work/pymeddra/data/meddra_23_0_english/MedAscii"
    )
    print("hello parser")
    meddra = parse_mdhier(data_dir)
    print(meddra.lookup_term("COVID-19 pneumonia"))
    print(meddra.lookup_term("covid19 pneumonia"))
    meddra.set_lookup_tables(normalizer=lambda x: x.lower())

    print(meddra.lookup_term("COVID-19 pneumonia"))
    print(meddra.lookup_term("covid-19 pneumonia"))
