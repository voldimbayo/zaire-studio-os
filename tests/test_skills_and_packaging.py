"""Tests d'intégration complets de ZAÏRE STUDIO OS (v1.1.0) :
- Validation des 57 SKILL.md, profondeur des références (>= 35 lignes) et des templates (>= 12 lignes).
- Contrôle de sécurité des chemins et de toutes les sources SRC-001..SRC-032.
- Exécution unitaire et sur fichiers réels (production/ et tests/fixtures/) des 9 scripts métier.
- Vérification de la génération effective des 19 artefacts de production par les 5 scénarios fonctionnels.
- Vérification de la structure d'importation Claude.ai des 57 archives ZIP individuelles (incluant
  references/entities-registry-snapshot.csv), des 9 archives départementales et de l'archive globale v1.1.0.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

from tools import WORKSPACE_ROOT
from tools.check_dag_cycles import build_disk_graph, check_all_dags, compute_topological_order
from tools.lint_skills import lint_skills_in_workspace
from tools.registry_data import CANONICAL_SKILLS
from tools.run_functional_scenarios import execute_all_five_scenarios


class TestZaireStudioOSSystem(unittest.TestCase):
    def test_all_57_skills_lint_depth_and_references(self) -> None:
        count, errors = lint_skills_in_workspace(WORKSPACE_ROOT, require_all_57=True)
        self.assertEqual(count, 57, f"Attendu 57 skills, trouvé {count}")
        self.assertEqual(errors, [], f"Erreurs de linting : {errors}")

    def test_disk_dag_has_57_nodes_and_zero_cycles(self) -> None:
        disk_graph = build_disk_graph(WORKSPACE_ROOT)
        self.assertEqual(len(disk_graph), 57)
        ordered, cycles = compute_topological_order(disk_graph)
        self.assertEqual(cycles, [])
        self.assertEqual(len(ordered), 57)
        self.assertEqual(check_all_dags(WORKSPACE_ROOT), [])

    def test_department_counts_match_architecture(self) -> None:
        expected_counts = {
            "00-direction": 7,
            "01-narrative": 6,
            "02-world-design": 6,
            "03-game-design": 7,
            "04-ai-simulation": 4,
            "05-art-animation": 9,
            "06-audio-localization": 4,
            "07-engineering": 8,
            "08-production-quality": 6,
        }
        skills_root = WORKSPACE_ROOT / "skills"
        for dept, expected in expected_counts.items():
            dept_dir = skills_root / dept
            self.assertTrue(dept_dir.exists(), f"Département manquant : {dept}")
            actual_dirs = [p for p in dept_dir.iterdir() if p.is_dir() and (p / "SKILL.md").exists()]
            self.assertEqual(
                len(actual_dirs),
                expected,
                f"Département {dept}: attendu {expected} skills, trouvé {len(actual_dirs)}",
            )

    def test_file_based_validation_accepts_valid_and_rejects_invalid_fixture(self) -> None:
        fixture_file = WORKSPACE_ROOT / "tests/fixtures/blockout_test_fixtures.json"
        self.assertTrue(fixture_file.exists())
        fixtures = json.loads(fixture_file.read_text(encoding="utf-8"))
        script_path = (
            WORKSPACE_ROOT
            / "skills/02-world-design/wld-05-level-designer/scripts/check_spatial_metrics.py"
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            valid_p = tmp / "valid.json"
            invalid_p = tmp / "invalid.json"
            valid_p.write_text(json.dumps(fixtures["valid_blockout"]), encoding="utf-8")
            invalid_p.write_text(json.dumps(fixtures["invalid_blockout"]), encoding="utf-8")

            ok_proc = subprocess.run(
                [sys.executable, str(script_path), "--file", str(valid_p)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(ok_proc.returncode, 0)

            bad_proc = subprocess.run(
                [sys.executable, str(script_path), "--file", str(invalid_p)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(bad_proc.returncode, 0)
            self.assertIn("[ERREUR]", bad_proc.stdout)

    def test_five_functional_scenarios_generate_real_files_and_pass(self) -> None:
        results = execute_all_five_scenarios(WORKSPACE_ROOT)
        self.assertEqual(len(results), 5)
        for key, payload in results.items():
            self.assertEqual(
                payload.get("classification"),
                "PASS",
                f"Le scénario {key} n'a pas obtenu PASS: {payload}",
            )
            gen_files = payload.get("generated_files", [])
            self.assertGreater(len(gen_files), 0, f"Aucun fichier généré pour {key}")
            for rel_f in gen_files:
                abs_f = WORKSPACE_ROOT / rel_f
                self.assertTrue(abs_f.exists(), f"Artefact de production manquant : {abs_f}")
                self.assertGreater(abs_f.stat().st_size, 100, f"Artefact trop petit : {abs_f}")

        # Verify ENG-04 executes strictly before AI-03 in Scenario 1 and Scenario 4
        self.assertIn("ENG-04 (Wave 10) -> AI-03 (Wave 11)", results["SCENARIO_1"]["eng04_wave_before_ai03_wave"])
        self.assertIn("ENG-04 (Wave 11) -> AI-03 (Wave 12)", results["SCENARIO_4"]["eng04_wave_before_ai03_wave"])

    def test_zip_releases_packaging_and_claude_ai_structure(self) -> None:
        skills_zip_dir = WORKSPACE_ROOT / "releases" / "skills"
        self.assertTrue(skills_zip_dir.exists())

        zip_files = sorted(skills_zip_dir.glob("*.zip"))
        self.assertEqual(len(zip_files), 57, f"Attendu 57 archives ZIP individuelles, trouvé {len(zip_files)}")

        for spec in CANONICAL_SKILLS:
            zpath = skills_zip_dir / f"{spec.slug}.zip"
            self.assertTrue(zpath.exists(), f"Archive ZIP manquante pour {spec.slug}")
            with zipfile.ZipFile(zpath, mode="r") as zf:
                self.assertIsNone(zf.testzip(), f"Archive ZIP corrompue : {zpath}")
                namelist = zf.namelist()
                root_prefixes = {name.split("/")[0] for name in namelist}
                self.assertEqual(
                    root_prefixes,
                    {spec.slug},
                    f"Claude.ai exige un dossier racine unique ({spec.slug}) dans le ZIP, trouvé {root_prefixes}",
                )
                self.assertIn(f"{spec.slug}/SKILL.md", namelist)
                self.assertIn(f"{spec.slug}/references/entities-registry-snapshot.csv", namelist)
                self.assertTrue(any(n.startswith(f"{spec.slug}/references/") for n in namelist))
                self.assertTrue(any(n.startswith(f"{spec.slug}/templates/") for n in namelist))
                self.assertTrue(any(n.startswith(f"{spec.slug}/examples/") for n in namelist))

        full_zip = WORKSPACE_ROOT / "releases" / "zaire-studio-os-v1.1.0-full.zip"
        self.assertTrue(full_zip.exists(), "Archive globale v1.1.0 du système manquante.")
        with zipfile.ZipFile(full_zip, mode="r") as zf:
            self.assertIsNone(zf.testzip(), "Archive globale corrompue.")
            names = set(zf.namelist())
            self.assertIn("zaire-studio-os/README.md", names)
            self.assertIn("zaire-studio-os/CLAUDE.md", names)
            self.assertIn("zaire-studio-os/knowledge/entities-registry.csv", names)
            self.assertIn("zaire-studio-os/docs/canonical-dependency-registry.md", names)
            self.assertIn(
                "zaire-studio-os/production/scenario-1-district-bandal/district-bandal-spec.md",
                names,
            )

        depts_zip_dir = WORKSPACE_ROOT / "releases" / "departments"
        self.assertTrue(depts_zip_dir.exists(), "Répertoire releases/departments manquant.")
        dept_zips = sorted(depts_zip_dir.glob("*.zip"))
        self.assertEqual(len(dept_zips), 9, f"Attendu 9 archives ZIP départementales, trouvé {len(dept_zips)}")
        for dz in dept_zips:
            with zipfile.ZipFile(dz, mode="r") as zf:
                self.assertIsNone(zf.testzip(), f"Archive départementale corrompue : {dz}")

    def test_plugin_zip_is_importable_by_claude(self) -> None:
        from tools.package_skills import package_plugin

        plugin_zip = package_plugin(WORKSPACE_ROOT)
        with zipfile.ZipFile(plugin_zip, mode="r") as zf:
            self.assertIsNone(zf.testzip(), "Archive plug-in corrompue.")
            names = zf.namelist()
            self.assertEqual(len(names), len(set(names)), "Entrées dupliquées dans l'archive plug-in.")
            self.assertIn(".claude-plugin/plugin.json", names)
            manifest = json.loads(zf.read(".claude-plugin/plugin.json").decode("utf-8"))
            self.assertEqual(manifest["name"], "zaire-studio-os")
            self.assertFalse(
                [n for n in names if n.lower().endswith(".zip")],
                "L'import Claude refuse les archives ZIP imbriquées.",
            )
            for spec in CANONICAL_SKILLS:
                self.assertIn(f"skills/{spec.slug}/SKILL.md", names)
            skill_mds = [n for n in names if n.startswith("skills/") and n.endswith("/SKILL.md")]
            self.assertTrue(all(n.count("/") == 2 for n in skill_mds), "Skills attendus à plat : skills/<slug>/SKILL.md")


if __name__ == "__main__":
    unittest.main()
