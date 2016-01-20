select distinct stu.local_student_id as studentid
	,cub.site_id as schoolid 
	,att.date as att_date 
	,attflag.character_code as att_code 
	,attflag.flag_text as presence_status_cd

from  matviews.ss_cube cub
join public.students stu on cub.student_id = stu.student_id 
join attendance.daily_records att on cub.student_id = att.student_id 
/*the table might change depending on the school*/
join attendance._flags_trac9569 attflag on  att.attendance_flag_id = attflag.attendance_flag_id

where cub.entry_date <= current_timestamp and cub.leave_date >= current_timestamp
/*change to new school year*/ and att.date > '2015-08-01'
