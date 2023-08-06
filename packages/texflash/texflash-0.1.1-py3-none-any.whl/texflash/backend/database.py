
import os
import json
import pickle
import hashlib
from pathlib import Path
from .source import Source


class Database:

    base_root = Path('__main__').resolve().parent / ".data"

    def __init__(self, root: str = None) -> None:
        self.root = root if root is not None else Database.base_root
        self.metadata = self.init()

    @property
    def metadata_path(self) -> Path:
        return self.root / "metadata.json"

    def init(self) -> dict:
        self.root.mkdir(exist_ok=True)
        if self.metadata_path.exists():
            with open(self.metadata_path) as file:
                metadata = json.load(file)
        else:
            metadata = dict(
                sources=dict(), removed=dict(),
                stats=dict(current_streak=0, previous_streak=0)
            )
        return metadata

    def source_filepath(self, title: str) -> Path:
        hash = self.metadata["sources"][title]["hash"]
        return (self.root / hash).with_suffix(".source")

    def write_metadata(self) -> None:
        with open(self.metadata_path, 'w') as json_file:
            json.dump(self.metadata, json_file, sort_keys=True, indent=4)

    def delete_source_file(self, title: str) -> None:
        os.remove(self.source_filepath(title))

    @staticmethod
    def generate_random_hash() -> str:
        return hashlib.md5(os.urandom(8)).hexdigest()

    def make_source_from_file(self, file) -> Source:
        lines = [line.decode("utf-8") for line in file.readlines()]
        return Source(lines)

    def copy_stats(self, new_source: Source) -> None:
        """ When updating a source, stats need to be copied. Acts on new Source inplace. """
        old_source = self.load_source(new_source.title)
        nodes = list(filter(lambda x: len(x.cards) > 0, old_source.tree.nodes))
        stats = {node.name: {card.title: card.stats for card in node.cards} for node in nodes}
        new_nodes = list(filter(lambda x: len(x.cards) > 0, new_source.tree.nodes))
        for node in new_nodes:
            if node.name in stats:
                for card in node.cards:
                    card.stats = stats[node.name][card.title]

    def add_source(self, source: Source) -> None:
        hash = Database.generate_random_hash()
        filepath = (self.root / hash).with_suffix(".source")
        if self.source_exists(source):
            self.copy_stats(source)
            self.delete_source_file(source.title)
        with open(filepath, "wb") as file:
            pickle.dump(source, file)
        self.metadata["sources"][source.title] = dict(hash=hash)
        self.write_metadata()

    def source_exists(self, source: Source) -> bool:
        titles = list(self.metadata["sources"].keys())
        return source.title in titles

    def remove_source(self, title: str) -> None:
        self.delete_source_file(title)
        removed_source = self.metadata["sources"].pop(title, None)
        self.metadata["removed"][title] = removed_source
        self.write_metadata()

    def load_source(self, title: str) -> Source:
        filepath = self.source_filepath(title)
        with open(filepath, "rb") as file:
            source = pickle.load(file)
        return source

    def save_source(self, source: Source) -> None:
        filepath = self.source_filepath(source.title)
        with open(filepath, "wb") as file:
            pickle.dump(source, file)
