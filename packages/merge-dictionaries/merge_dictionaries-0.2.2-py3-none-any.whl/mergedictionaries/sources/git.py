#   -------------------------------------------------------------
#   Merge dictionaries :: Sources :: Git
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Fetch dictionaries from Git repository
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


import hashlib
import os
import shutil
import subprocess
import tempfile


#   -------------------------------------------------------------
#   Manipulate a dictionary sync repository
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class GitRepository:

    DICTIONARY_PATH = "dictionary.txt"

    def __init__(self, repository_remote, cached_repositories):
        self.remote = repository_remote
        self.cache = cached_repositories
        self.path = None

        self.prepare_repository()

    def get_cache_hash(self):
        return hashlib.md5(self.remote.encode("ascii")).hexdigest()

    def prepare_repository(self):
        cache_hash = self.get_cache_hash()

        try:
            self.path = self.cache[cache_hash]
        except KeyError:
            self.clone()
            self.cache[cache_hash] = self.path

    def get_dictionary_path(self):
        return os.path.join(self.path, self.DICTIONARY_PATH)

    def extract_words(self):
        return [word.strip() for word in open(self.get_dictionary_path())]

    def publish(self, tmp_dictionary_path):
        shutil.copy(tmp_dictionary_path, self.get_dictionary_path())

        if self.is_dirty():
            self.commit()
            self.push()

    #   -------------------------------------------------------------
    #   Git operations
    #   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def is_dirty(self):
        checks = [
            # Detect empty repository
            ["git", "show-ref", "HEAD"],
            # Detect index change
            ["git", "diff-index", "--quiet", "HEAD", "--"],
        ]

        for check_command in checks:
            process = subprocess.run(
                check_command,
                stderr=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                cwd=self.path,
            )

            if process.returncode > 0:
                return True

        return False

    @staticmethod
    def get_commit_message():
        return f"Sync personal dictionary\n\nSync application: merge-dictionaries\nSync hostname: {os.environ['HOSTNAME']}"

    def run(self, commands):
        for command in commands:
            subprocess.run(
                command,
                cwd=self.path,
            )

    def commit(self):
        self.run(
            [
                # Detect empty repository
                ["git", "add", self.DICTIONARY_PATH],
                # Detect index change
                ["git", "commit", "-m", self.get_commit_message()],
            ]
        )

    def push(self):
        self.run(
            [
                ["git", "push", "origin", self.get_branch()],
            ]
        )

    def clone(self):
        self.path = tempfile.mkdtemp(prefix="merge-dictionaries-")
        subprocess.run(["git", "clone", self.remote, self.path])

    def get_branch(self):
        return (
            subprocess.run(
                ["git", "symbolic-ref", "--short", "HEAD"],
                cwd=self.path,
                capture_output=True,
            )
            .stdout.decode()
            .strip()
        )


#   -------------------------------------------------------------
#   Wrapper to read Git repositories
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def extract_words_from_all_dictionaries(target_repos, cached_repos):
    return {
        word
        for repo in target_repos
        for word in GitRepository(repo, cached_repos).extract_words()
    }


#   -------------------------------------------------------------
#   Events
#     :: on_exit
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def on_exit(cached_repos):
    for _, repository_path in cached_repos.items():
        shutil.rmtree(repository_path)
