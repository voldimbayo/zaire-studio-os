"""Détecteur de cycles et validateur d'ordre topologique (DAG) pour ZAÏRE STUDIO OS.

Vérifie :
1. Que le graphe des 57 skills (`CANONICAL_SKILLS`) est un Graphe Orienté Acyclique (DAG) strict.
2. Que tous les fichiers `SKILL.md` présents sur le disque déclarent des `upstream_dependencies`
   exemptes de cycles et conformes au catalogue architectural.
"""

from __future__ import annotations

import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import WORKSPACE_ROOT, extract_frontmatter
from tools.registry_data import CANONICAL_SKILLS, SKILLS_BY_ID


def compute_topological_order(graph: dict[str, list[str]]) -> tuple[list[str], list[str]]:
    """Algorithme de Kahn pour le tri topologique et la détection de cycles.

    `graph` associe chaque `node_id` à la liste de ses dépendances amont (`upstream_ids`).
    Retourne `(ordered_nodes, cycle_nodes)`.
    """
    in_degree: dict[str, int] = {node: 0 for node in graph}
    downstream_map: dict[str, list[str]] = {node: [] for node in graph}

    for node, upstreams in graph.items():
        for up in upstreams:
            if up not in graph:
                raise KeyError(f"Le noeud {node!r} référence une dépendance inconnue {up!r}.")
            downstream_map[up].append(node)
            in_degree[node] += 1

    queue: list[str] = sorted([node for node, deg in in_degree.items() if deg == 0])
    ordered: list[str] = []

    while queue:
        current = queue.pop(0)
        ordered.append(current)
        for neighbor in sorted(downstream_map[current]):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                queue.sort()

    cycle_nodes = sorted([node for node, deg in in_degree.items() if deg > 0])
    return ordered, cycle_nodes


def build_canonical_graph() -> dict[str, list[str]]:
    """Construit le graphe des dépendances à partir des spécifications canoniques."""
    return {spec.skill_id: list(spec.upstream_ids) for spec in CANONICAL_SKILLS}


def build_disk_graph(workspace: Path = WORKSPACE_ROOT) -> dict[str, list[str]]:
    """Construit le graphe des dépendances directement depuis les fichiers SKILL.md implémentés."""
    skills_dir = workspace / "skills"
    graph: dict[str, list[str]] = {}
    if not skills_dir.exists():
        return graph

    for skill_md in sorted(skills_dir.glob("*/*/SKILL.md")):
        frontmatter, _ = extract_frontmatter(skill_md.read_text(encoding="utf-8"))
        metadata = frontmatter.get("metadata") or {}
        skill_id = str(metadata.get("id", "")).strip()
        upstreams = [str(x).strip() for x in (metadata.get("upstream_dependencies") or [])]
        if skill_id:
            graph[skill_id] = upstreams
    return graph


def check_all_dags(workspace: Path = WORKSPACE_ROOT) -> list[str]:
    """Vérifie l'absence de cycles dans le graphe canonique et dans les skills sur disque."""
    errors: list[str] = []

    canonical_graph = build_canonical_graph()
    try:
        ordered, cycles = compute_topological_order(canonical_graph)
        if cycles:
            errors.append(f"Cycle détecté dans le graphe canonique : {cycles}")
        elif len(ordered) != len(CANONICAL_SKILLS):
            errors.append("Tri topologique canonique incomplet.")
    except KeyError as exc:
        errors.append(str(exc))

    disk_graph = build_disk_graph(workspace)
    if disk_graph:
        for node, upstreams in disk_graph.items():
            if node not in SKILLS_BY_ID:
                errors.append(f"Skill sur disque avec ID inconnu : {node}")
            for up in upstreams:
                if up not in SKILLS_BY_ID:
                    errors.append(f"Skill {node} déclare une dépendance inconnue : {up}")
        filtered_graph = {
            node: [u for u in ups if u in disk_graph] for node, ups in disk_graph.items()
        }
        _, disk_cycles = compute_topological_order(filtered_graph)
        if disk_cycles:
            errors.append(f"Cycle détecté dans les fichiers SKILL.md sur disque : {disk_cycles}")

    return errors


def main() -> int:
    errors = check_all_dags(WORKSPACE_ROOT)
    if errors:
        print("[ERREUR] Validation DAG échouée :")
        for err in errors:
            print(f"  - {err}")
        return 1
    ordered, _ = compute_topological_order(build_canonical_graph())
    print(
        f"[OK] Graphe DAG validé (0 cycle sur {len(ordered)} skills). "
        f"Ordre d'amorçage : {', '.join(ordered[:8])}..."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
