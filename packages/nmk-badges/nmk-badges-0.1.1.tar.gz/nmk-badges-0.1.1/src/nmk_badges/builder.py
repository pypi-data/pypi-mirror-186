from typing import Dict, List

from nmk.model.builder import NmkTaskBuilder


class NmkBadgesBuilder(NmkTaskBuilder):
    def build(self, badges: List[Dict[str, str]], begin_pattern: str, end_pattern: str):
        # Read lines from target file
        with self.main_input.open() as f:
            all_lines = f.readlines()

        # Check for patterns
        begin_index, end_index = None, None
        for index, some_line in enumerate(all_lines):
            if begin_pattern in some_line and begin_index is None:
                begin_index = index
            elif end_pattern in some_line and begin_index is not None:
                end_index = index
                break

        # Index found?
        if begin_index is not None and end_index is not None and end_index > begin_index:
            # Insert badges
            new_lines = all_lines[: begin_index + 1]
            for badge in badges:
                new_lines.append(f"[![{badge['alt']}]({badge['img']})]({badge['url']})\n")
            new_lines.extend(all_lines[end_index:])

            # Write updated lines
            with self.main_input.open("w") as f:
                f.writelines(new_lines)

            # Touch the stamp file
            self.main_output.touch()
        else:
            self.logger.warning(f"Invalid or missing pattern in {self.main_input.name} file")
