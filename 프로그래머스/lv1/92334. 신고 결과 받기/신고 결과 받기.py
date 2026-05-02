def solution(id_list, report, k):
    answer = [0] * len(id_list)
    id_dict, report_dict = {}, {}
    idx = 0
    for id in id_list:
        id_dict[id] = idx
        report_dict[id] = []
        idx += 1
        
    report_set = set(report)

    for r in report_set:
        reporter, reportee = r.split(" ")
        report_dict[reportee].append(reporter)

    for v_list in report_dict.values():
        if len(v_list) >= k:
            for v in v_list:
                answer[id_dict[v]] += 1
    return answer