def merge_ranges(meetings):

    meetings = sorted(meetings)
    print("sorted meetings: ", meetings)

    condensed_meetings = [meetings[0]]
    for current_meeting in meetings:
        last_merged_meeting = condensed_meetings[-1]

        if current_meeting[0] <= last_merged_meeting[1]:
            condensed_meetings[-1] = (
                last_merged_meeting[0],
                max(last_merged_meeting[1], current_meeting[1]),
            )
        else:
            condensed_meetings.append(current_meeting)

    return condensed_meetings


if __name__ == "__main__":
    condensed_meetings = merge_ranges([(5, 6), (2, 7), (2, 4), (5, 8)])
    print("condensed meetings: ", condensed_meetings)
