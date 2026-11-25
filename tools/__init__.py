"""Utilitaires partagés et parseur YAML/Frontmatter déterministe durci pour ZAÏRE STUDIO OS (v1.1.0)."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent

# Sortie console en UTF-8 (accents, glyphes lingala) même sous cp1252 (Windows) pour tous les outils CLI.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")


class YamlParseError(ValueError):
    """Erreur levée lorsqu'un bloc YAML ou frontmatter SKILL.md est invalide."""


def resolve_safe_path(base_dir: Path, relative_target: str) -> Path:
    """Résout un chemin relatif en interdisant toute traversée hors de base_dir."""
    if not relative_target or "\x00" in relative_target:
        raise ValueError(f"Chemin cible invalide : {relative_target!r}")
    base_resolved = base_dir.resolve()
    candidate = (base_resolved / relative_target).resolve()
    try:
        candidate.relative_to(base_resolved)
    except ValueError as exc:
        raise ValueError(
            f"Violation de sécurité de chemin : {relative_target!r} sort de {base_resolved}"
        ) from exc
    return candidate


def _strip_inline_comment(raw_val: str) -> str:
    """Supprime un commentaire inline (# ...) hors guillemets simples ou doubles."""
    in_single = False
    in_double = False
    for idx, ch in enumerate(raw_val):
        if ch == "'" and not in_double:
            in_single = not in_single
        elif ch == '"' and not in_single:
            in_double = not in_double
        elif ch == "#" and not in_single and not in_double:
            if idx == 0 or raw_val[idx - 1].isspace():
                return raw_val[:idx].rstrip()
    return raw_val.strip()


def _split_inline_list(inner: str) -> list[str]:
    """Découpe une liste inline YAML [a, "b, c", d] en respectant les guillemets."""
    items: list[str] = []
    current: list[str] = []
    in_single = False
    in_double = False
    for ch in inner:
        if ch == "'" and not in_double:
            in_single = not in_single
            current.append(ch)
        elif ch == '"' and not in_single:
            in_double = not in_double
            current.append(ch)
        elif ch == "," and not in_single and not in_double:
            items.append("".join(current).strip())
            current = []
        else:
            current.append(ch)
    tail = "".join(current).strip()
    if tail:
        items.append(tail)
    return items


def _parse_scalar(raw_val: str) -> Any:
    """Convertit une valeur scalaire YAML en type Python natif."""
    val = _strip_inline_comment(raw_val.strip())
    if not val:
        return ""
    if (val.startswith('"') and val.endswith('"')) or (
        val.startswith("'") and val.endswith("'")
    ):
        return val[1:-1]
    if val.startswith("[") and val.endswith("]"):
        inner = val[1:-1].strip()
        if not inner:
            return []
        return [_parse_scalar(item) for item in _split_inline_list(inner)]
    lowered = val.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    if lowered in ("null", "none", "~"):
        return None
    if val.isdigit() or (val.startswith("-") and val[1:].isdigit()):
        return int(val)
    try:
        return float(val)
    except ValueError:
        return val


def parse_simple_yaml(yaml_text: str) -> dict[str, Any]:
    """Parse un sous-ensemble structuré de YAML (dictionnaires imbriqués, listes, scalaires, blocs | et >).

    Conçu sans dépendance externe pour valider les frontmatters SKILL.md de manière
    strictement déterministe dans tous les environnements Python 3.10+.
    """
    lines = yaml_text.splitlines()
    root: dict[str, Any] = {}
    stack: list[tuple[int, dict[str, Any] | list[Any]]] = [(-1, root)]

    idx = 0
    total_lines = len(lines)
    while idx < total_lines:
        raw_line = lines[idx]
        line_num = idx + 1
        if "\t" in raw_line:
            raise YamlParseError(f"Ligne {line_num}: les tabulations sont interdites en YAML.")
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            idx += 1
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        while len(stack) > 1 and indent <= stack[-1][0]:
            stack.pop()

        parent = stack[-1][1]

        if stripped.startswith("- "):
            item_text = stripped[2:].strip()
            if not isinstance(parent, list):
                raise YamlParseError(
                    f"Ligne {line_num}: élément de liste inattendu hors d'un conteneur liste."
                )
            parent.append(_parse_scalar(item_text))
            idx += 1
            continue

        if ":" not in stripped:
            raise YamlParseError(f"Ligne {line_num}: syntaxe clé:valeur attendue ({stripped!r}).")

        key_part, _, val_part = stripped.partition(":")
        key = key_part.strip()
        if not key:
            raise YamlParseError(f"Ligne {line_num}: clé YAML vide.")
        val_clean = val_part.strip()

        if not isinstance(parent, dict):
            raise YamlParseError(
                f"Ligne {line_num}: impossible d'affecter la clé {key!r} dans une liste."
            )

        if val_clean in ("|", ">", "|-", ">-"):
            fold = val_clean.startswith(">")
            block_lines: list[str] = []
            block_indent: int | None = None
            idx += 1
            while idx < total_lines:
                b_raw = lines[idx]
                b_strip = b_raw.strip()
                if not b_strip:
                    block_lines.append("")
                    idx += 1
                    continue
                b_ind = len(b_raw) - len(b_raw.lstrip(" "))
                if block_indent is None:
                    if b_ind <= indent:
                        break
                    block_indent = b_ind
                if b_ind < block_indent:
                    break
                block_lines.append(b_raw[block_indent:])
                idx += 1
            joiner = " " if fold else "\n"
            parent[key] = joiner.join(block_lines).strip()
            continue

        if not val_clean or val_clean.startswith("#"):
            next_container: dict[str, Any] | list[Any] = {}
            for lookahead in lines[idx + 1 :]:
                la_strip = lookahead.strip()
                if not la_strip or la_strip.startswith("#"):
                    continue
                la_indent = len(lookahead) - len(lookahead.lstrip(" "))
                if la_indent > indent and la_strip.startswith("- "):
                    next_container = []
                break
            parent[key] = next_container
            stack.append((indent, next_container))
        else:
            parent[key] = _parse_scalar(val_clean)

        idx += 1

    return root


def extract_frontmatter(markdown_text: str) -> tuple[dict[str, Any], str]:
    """Extrait et parse le frontmatter YAML délimité par --- en tête d'un fichier SKILL.md."""
    if not markdown_text.startswith("---\n") and not markdown_text.startswith("---\r\n"):
        raise YamlParseError("Le fichier SKILL.md doit commencer par un délimiteur '---'.")

    lines = markdown_text.splitlines()
    end_idx = -1
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_idx = idx
            break

    if end_idx == -1:
        raise YamlParseError("Délimiteur de fermeture '---' du frontmatter YAML introuvable.")

    yaml_block = "\n".join(lines[1:end_idx])
    body = "\n".join(lines[end_idx + 1 :]).strip()
    parsed = parse_simple_yaml(yaml_block)
    return parsed, body
