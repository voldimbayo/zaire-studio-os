"""Tests unitaires et d'intégration de la fondation d'outillage ZAÏRE STUDIO OS (v1.1.0)."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

from tools import WORKSPACE_ROOT, YamlParseError, extract_frontmatter, parse_simple_yaml, resolve_safe_path
from tools.check_dag_cycles import build_canonical_graph, check_all_dags, compute_topological_order
from tools.registry_data import CANONICAL_SKILLS, SKILLS_BY_ID
from tools.validate_registry import load_source_ids, validate_knowledge_base


class TestToolingFoundation(unittest.TestCase):
    def test_yaml_parser_and_frontmatter(self) -> None:
        sample = (
            "---\n"
            "name: dir-01-studio-orchestrator\n"
            'description: "Orchestrateur central du système ZAÏRE STUDIO OS."\n'
            "metadata:\n"
            "  id: DIR-01 # Commentaire inline\n"
            "  stratum: 0\n"
            '  inline_tags: ["a, b", "c"]\n'
            "  notes: |\n"
            "    Ligne 1\n"
            "    Ligne 2\n"
            "  inputs:\n"
            "    - user-request\n"
            "    - entities-registry.csv\n"
            "  upstream_dependencies: []\n"
            "---\n"
            "# Corps du Skill\n"
        )
        fm, body = extract_frontmatter(sample)
        self.assertEqual(fm["name"], "dir-01-studio-orchestrator")
        self.assertEqual(fm["metadata"]["id"], "DIR-01")
        self.assertEqual(fm["metadata"]["stratum"], 0)
        self.assertEqual(fm["metadata"]["inline_tags"], ["a, b", "c"])
        self.assertEqual(fm["metadata"]["notes"], "Ligne 1\nLigne 2")
        self.assertEqual(fm["metadata"]["inputs"], ["user-request", "entities-registry.csv"])
        self.assertEqual(fm["metadata"]["upstream_dependencies"], [])
        self.assertEqual(body, "# Corps du Skill")

    def test_yaml_rejects_tabs_and_missing_delimiter(self) -> None:
        with self.assertRaises(YamlParseError):
            parse_simple_yaml("key:\n\t- bad_indent")
        with self.assertRaises(YamlParseError):
            extract_frontmatter("name: missing_opening_delimiter\n---\n")

    def test_safe_path_blocks_traversal(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            base = Path(tmpdir)
            valid = resolve_safe_path(base, "references/guide.md")
            self.assertTrue(str(valid).startswith(str(base.resolve())))
            with self.assertRaises(ValueError):
                resolve_safe_path(base, "../../etc/passwd")

    def test_canonical_catalog_has_57_skills_and_zero_cycles(self) -> None:
        self.assertEqual(len(CANONICAL_SKILLS), 57)
        graph = build_canonical_graph()
        ordered, cycles = compute_topological_order(graph)
        self.assertEqual(cycles, [])
        self.assertEqual(len(ordered), 57)
        self.assertEqual(check_all_dags(WORKSPACE_ROOT), [])

    def test_eng04_precedes_ai03_and_wld05_precedes_art05(self) -> None:
        self.assertIn("ENG-04", SKILLS_BY_ID["AI-03"].upstream_ids)
        self.assertNotIn("AI-03", SKILLS_BY_ID["ENG-04"].upstream_ids)
        self.assertIn("WLD-05", SKILLS_BY_ID["ART-05"].upstream_ids)
        self.assertNotIn("ART-05", SKILLS_BY_ID["WLD-05"].upstream_ids)

    def test_dir01_build_dag_script_has_100_percent_parity_with_canonical_skills(self) -> None:
        script_path = (
            WORKSPACE_ROOT
            / "skills/00-direction/dir-01-studio-orchestrator/scripts/build_dag_plan.py"
        )
        self.assertTrue(script_path.exists())
        spec = importlib.util.spec_from_file_location("build_dag_plan", script_path)
        assert spec and spec.loader
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)

        expected_deps = {s.skill_id: list(s.upstream_ids) for s in CANONICAL_SKILLS}
        expected_strata = {s.skill_id: s.stratum for s in CANONICAL_SKILLS}
        self.assertEqual(mod.DEFAULT_DEPENDENCIES, expected_deps)
        self.assertEqual(mod.DEFAULT_STRATA, expected_strata)

    def test_cycle_detection_catches_circular_dependency(self) -> None:
        cyclic_graph = {
            "A": ["B"],
            "B": ["C"],
            "C": ["A"],
        }
        _, cycles = compute_topological_order(cyclic_graph)
        self.assertEqual(cycles, ["A", "B", "C"])

    def test_knowledge_base_and_source_registry_integrity(self) -> None:
        errors = validate_knowledge_base(WORKSPACE_ROOT)
        self.assertEqual(errors, [], f"Erreurs dans knowledge/: {errors}")
        sources = load_source_ids(WORKSPACE_ROOT)
        self.assertEqual(len(sources), 35)
        self.assertIn("SRC-021", sources)
        self.assertIn("SRC-031", sources)
        self.assertIn("SRC-035", sources)


if __name__ == "__main__":
    unittest.main()
