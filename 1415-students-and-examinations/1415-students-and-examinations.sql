# Write your MySQL query statement below
select st.student_id, st.student_name, sub.subject_name, COUNT(ex.student_id) as attended_exams
from Students as st
join Subjects sub
left join Examinations as ex
on st.student_id = ex.student_id and sub.subject_name = ex.subject_name
group by st.student_id, st.student_name, sub.subject_name
order by st.student_id, sub.subject_name
