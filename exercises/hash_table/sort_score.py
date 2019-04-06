def add_score(score_count, score):
    if score in score_count:
        score_count[score] += 1
    else:
        score_count[score] = 1


def sort_scores(scores, top_score):
    score_count = dict()
    sorted_scores = []

    for score in scores:
        add_score(score_count, score)

    for possible_score in range(top_score, 0, -1):
        if possible_score in score_count:
            sorted_scores.extend(score_count[possible_score] * [possible_score])

    return sorted_scores

