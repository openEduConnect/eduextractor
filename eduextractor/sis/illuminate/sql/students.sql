select distinct stu.local_student_id::bigint as "id"
	,stu.first_name
	,stu.middle_name
	,stu.last_name
	,stu.gender
	,stu.birth_date as "dob"
	
from matviews.ss_cube cub
join public.students stu on stu.student_id = cub.student_id

where cub.entry_date <= current_date
and cub.leave_date > current_date
