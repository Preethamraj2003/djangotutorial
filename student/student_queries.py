# 1)Give student details of sem 1 
students = Student.objects.filter(current_sem='1')



# 2. Semesters student have attended
semesters = Result.objects.filter(student__usn='CS101').values('sem').distinct()
semester_ids = [semester['sem'] for semester in semesters]
print(f"Semesters attended by student with USN 'CS101': {', '.join(map(str, semester_ids))}")


# 3. print every student every sem average_marks

from django.db.models import Avg
from student.models import Result, student, semester

average_marks = Result.objects.values('student_id', 'sem_id') \
                               .annotate(average_marks=Avg('marks')) \
                               .order_by('student', 'sem')

for entry in average_marks:
    student_instance = student.objects.get(id=entry['student_id'])
    semester_instance = semester.objects.get(id=entry['sem_id'])
    print(f"Student: {student_instance.name}, Semester: {semester_instance.id}, Average Marks: {entry['average_marks']}")


student = student.objects.filter(usn=usn).first()  # Use `first()` to get the student, or `None` if not found
    
if student:
        # Filter the results based on the student's ID and the given semester
        results = Result.objects.filter(student=student, sem_id=semester)

        # Get the marks for each subject and calculate the average
        avg_marks = results.aggregate(Avg('marks'))['marks__avg']  # Calculate average marks for that semester
        
        # Fetching the marks and subject ids for that semester
        subject_marks = results.values('subject_id', 'marks')

        print(subject_marks, avg_marks)
else:
    print("NONE")