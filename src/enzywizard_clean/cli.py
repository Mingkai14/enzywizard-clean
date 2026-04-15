from __future__ import annotations

import argparse

from .commands.clean import add_clean_parser


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="enzywizard-clean",
        description="EnzyWizard-Clean: Clean an input protein structure file in CIF, PDB, and FASTA format."
    )
    add_clean_parser(parser)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)