class ArtifactNotFound(Exception):
    ...


class CorruptedArtifact(Exception):
    ...


class CorruptedMetadata(Exception):
    ...


class CorruptedONNXModel(Exception):
    ...


class NoSuchModel(Exception):
    ...


class SelectModelRequired(Exception):
    ...


class KeysMismatchError(Exception):
    ...
