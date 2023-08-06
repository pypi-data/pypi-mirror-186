from pathlib import Path

from printBuddies import ProgBar, clear, printInPlace


class TreeGenerator:
    """Generates a nested dictionary of arbitrary depth
    representing the subdirectories of a given directory."""

    def __init__(self, startingDirectory: str | Path):
        self.startingDir = Path(startingDirectory)
        self.paths = [self.startingDir]
        self._pipe = "|"
        self._tee = "|-"
        self._elbow = "|_"
        self.generate()

    def generate(self):
        self.paths.extend(self._crawl(self.startingDir))
        clear()
        self._dropParents()
        self._generateTree()
        self._generateTreeString()

    def _dropParents(self):
        self.paths = [
            Path(str(path)[str(path).find(self.startingDir.stem) :])
            for path in self.paths
        ]

    def __str__(self):
        return f"{self.treeString}"

    def _crawl(self, startDir: Path) -> list[Path]:
        """Generate recursive list of paths by crawling
        down every branch from the startingDir."""
        paths = []
        printInPlace(f"Crawling {startDir}...")
        for item in startDir.iterdir():
            if item.is_file():
                paths.append(item)
            elif item.is_dir():
                paths.extend(self._crawl(item))
                printInPlace(f"Crawling {startDir}...")
        return paths

    def _generateTree(self):
        """Generate nested dictionary of subdirectories."""
        self.tree = {}
        progBar = ProgBar(len(self.paths))
        progBar.display()
        for path in sorted(self.paths):
            if path.parts[0] not in self.tree:
                self.tree[path.parts[0]] = {}
            currentLayer = self.tree[path.parts[0]]
            branches = path.parts[1:]
            for branch in branches:
                if branch not in currentLayer:
                    currentLayer[branch] = {}
                currentLayer = currentLayer[branch]
            progBar.display()

    def _formatBranchName(self, branchName: str, index: int) -> str:
        if index == 0:
            return f"{branchName}\n"
        elif index == 1:
            return f'{self._pipe}{"  "*index}{self._tee}{branchName}\n'
        else:
            return (
                f'{self._pipe}{("  "+self._pipe)*(index-1)}  {self._tee}{branchName}\n'
            )

    def _convertBranchToString(self, branch: dict, branchName: str, index: int) -> str:
        """Iterates through a nested dictionary and returns a string representation."""
        output = self._formatBranchName(branchName, index)
        for i, leaf in enumerate(branch.keys()):
            if branch[leaf] == {}:
                output += f'{self._pipe}{("  "+self._pipe)*index}  '
                if i == len(branch.keys()) - 1:
                    output += f"{self._elbow}{leaf}\n"
                    output += f'{self._pipe}{("  "+self._pipe)*index}\n'
                else:
                    output += f"{self._tee}{leaf}\n"
            else:
                output += self._convertBranchToString(branch[leaf], leaf, index + 1)
        return output

    def _trimTree(self):
        tree = self.treeString.splitlines()
        self.treeString = ""
        for i, line in enumerate(tree[:-1]):
            if (
                all(ch in f"{self._pipe} " for ch in line)
                and i < len(tree) - 2
                and self._tee in tree[i + 1]
            ):
                self.treeString += f"{line[:tree[i+1].find(self._tee)+1]}\n"
            else:
                self.treeString += f"{line}\n"

    def _generateTreeString(self):
        """Generates formatted string representation of
        the directory tree."""
        self.treeString = ""
        for root in self.tree.keys():
            self.treeString += self._convertBranchToString(self.tree[root], root, 0)
        self._trimTree()


class UrlTreeGenerator(TreeGenerator):
    """Generates a tree representation of a given list of urls."""

    def __init__(self, urls: list[str]):
        self.paths = [Path(url) for url in urls]
        self._pipe = "|"
        self._tee = "|-"
        self._elbow = "|_"

    def generate(self):
        self._generateTree()
        self._generateTreeString()
