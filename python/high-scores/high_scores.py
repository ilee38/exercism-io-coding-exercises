def latest(scores):
    return scores[len(scores)-1]


def personal_best(scores):
    sorted_scores = sorted(scores)
    return sorted_scores[len(sorted_scores)-1]


def personal_top_three(scores):
    sorted_scores = sorted(scores)
    sorted_scores = sorted_scores[::-1]
    return sorted_scores if len(sorted_scores) <= 3 else sorted_scores[:3]
