def round_scores(student_scores):
    return [round(num) for num in student_scores]

def count_failed_students(student_scores):
    return sum(1 for num in student_scores if num <= 40)

def above_threshold(student_scores, threshold):
    return [num for num in student_scores if num >= threshold]

def letter_grades(highest):
    return [41 + round((highest - 41) / 4) * num for num in range(4)]

def  student_ranking (student_scores, student_names):
    return [f"{i}. {name}: {score}" for i, (name, score) in enumerate(zip(student_names, student_scores), start = 1)]
def  perfect_score (student_info):
    for info in student_info:
        if info[1] == 100:
            return info
    return []