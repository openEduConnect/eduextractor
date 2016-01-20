select distinct stu.local_student_id as studentid
	,sta.term_id as termid
	,cub.section_id  as sectionid
	,dep.department_name as course_number
	,cou.short_name as course_name 
	,cub.site_id as schoolid 
	,cub.user_id as teacherid
	,us.first_name as teacher_first
	,us.last_name as teacher_last
	,cub.entry_date as dateenrolled
	,cub.leave_date as dateleft 
from matviews.ss_cube cub
left join public.students stu on cub.student_id = stu.student_id 
left join public.section_term_aff sta  on cub.section_id = sta.section_id 
left join public.courses cou on cub.course_id = cou.course_id 
left join public.departments dep on cou.department_id = dep.department_id 
left join public.users us on cub.user_id = us.user_id 
where cub.entry_date <= current_timestamp and cub.leave_date >= current_timestamp
