SELECT distinct stu.local_student_id as studentid 
	,dep.department_name as course_number
	,sgpa.section_id as sectionid 
	,academic.grade as grade 
	,NULL as percent 
	,academic.count_towards_gpa
	,academic.gpa_points as gpa_addedvalue 
	,sgpa.is_published
	,gp.grading_period_end_date
FROM public.student_grades sg
JOIN public.students stu on sg.student_id = stu.student_id 
JOIN public.grades academic ON academic.grade_id = sg.grade_id
JOIN public.section_grading_period_aff sgpa on sg.sgpa_id = sgpa.sgpa_id
JOIN public.grading_periods gp USING (grading_period_id)
JOIN public.term_info ti USING (term_id)
JOIN public.section_course_aff secc on sgpa.section_id = secc.section_id
JOIN public.courses cou on secc.course_id = cou.course_id 
JOIN public.departments dep on cou.department_id = dep.department_id 
LEFT JOIN matviews.ss_cube cub on cub.section_id = secc.section_id 
LEFT JOIN public.users us on cub.user_id = us.user_id 
WHERE 1=1 and cub.entry_date <= CURRENT_TIMESTAMP and cub.leave_date >= CURRENT_TIMESTAMP 
