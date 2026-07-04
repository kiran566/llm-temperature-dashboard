import time
import difflib


def calculate_latency(start_time, end_time):
    return round(end_time - start_time, 2)


def word_count(text):
    return len(text.split())


def consistency_score(reference, output):
    """
    Returns similarity percentage between two outputs.
    """
    similarity = difflib.SequenceMatcher(
        None,
        reference,
        output
    ).ratio()

    return round(similarity * 100, 2)