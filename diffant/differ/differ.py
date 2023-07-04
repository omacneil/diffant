"""
Holds the implemention for comparing structured configuration files.
"""
from collections import defaultdict
from dataclasses import dataclass
from typing import Any, List, Tuple

from . import utils
from .types import ConfigData, DiffSummary, KeySummary, ValueSummary


@dataclass
class Differ:
    """
    This class calculates the diff between structured config files in a directory
    """

    def calc(self, *configs: ConfigData) -> DiffSummary:
        """Given an iterable of config dicts, calculate the diff between them.

        Args:
            *configs (Dict[str, Any]): An iterable of config dictionaries.
        """
        out = []
        for config in configs:
            keys, values = self._flatten_item(parent=[], data=config.data)
            out.append((keys, values, config))

        kv_to_filenames = defaultdict(set)
        for keys, values, config in out:
            for key, val in zip(keys, values):
                kv_to_filenames[tuple([tuple(key), val])].add(config.filename)

        keys_to_value_summaries = defaultdict(list)
        for keys, values, _ in out:
            for key, val in zip(keys, values):
                value_summary = ValueSummary(
                    value=val, filenames=kv_to_filenames[tuple([tuple(key), val])]
                )
                keys_to_value_summaries[tuple(key)].append(value_summary) # type: ignore [assignment]

        key_summaries = []
        for key, value_summaries in keys_to_value_summaries.items(): # type: ignore [assignment]
            key_summary = KeySummary(key_path=list(key), values=value_summaries)
            key_summaries.append(key_summary)

        return DiffSummary(
            keys=key_summaries, filenames=set(config.filename for config in configs)
        )

    def _flatten_item(
        self, parent: List[str], data: Any
    ) -> Tuple[List[List[str]], List[Any]]:
        """Flattens a potentially nested structure.

        Args:
            parent (str): Flattened/stringified version of the parent key
                          structure. Examples:
                - "" (empty string)
                - "root"
            data (Any): The data structure to flatten. It can be a string, integer,
                        float, list, dictionary, or None.

        Returns:
            Tuple[List[str], List[str]]: A tuple containing two unnested, (flat) lists:
                - keys: key paths.
                - values: Corresponding values for each key path.

        Examples:
            >>> _flatten_item(parent=[], data={'a': 1, 'b': 2})
            (['a', 'b'], ['1', '2'])
            >>> _flatten_item(parent=[], data={'a': {'b': 2}})
            ([['a', 'b']], ['2'])
            >>> _flatten_item(parent=[], data={'a': {'b': {'c': 3}}})
            ([['a', 'b', 'c']], ['3'])
        """

        if isinstance(data, (bool, float, int, str, type(None))):
            return [parent], [data]

        keys = []
        values = []

        if not parent:  # sort everything recursively only once
            data = utils.sort(data)

        if isinstance(data, dict):
            for key, value in data.items():
                nparent = parent + [key]
                nkeys, nvalues = self._flatten_item(parent=nparent, data=value)
                keys.extend(nkeys)
                values.extend(nvalues)

            values_sorted = values
            return (keys, values_sorted)

        if isinstance(data, list):
            for index, value in enumerate(data):
                nparent = parent + [str(index)]
                nkeys, nvalues = self._flatten_item(parent=nparent, data=value)
                keys.extend(nkeys)
                values.extend(nvalues)

            values_sorted = values
            return (keys, values_sorted)

        else:
            raise TypeError(f"Unsupported type: {type(data)}")
