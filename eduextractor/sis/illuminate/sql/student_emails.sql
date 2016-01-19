select distinct stu.local_student_id::bigint as "id"
	,stu.email as "student_web_id"
	
from matviews.ss_cube cub
join public.students stu on stu.student_id = cub.student_id

where cub.entry_date <= current_date
and cub.leave_date > current_date
