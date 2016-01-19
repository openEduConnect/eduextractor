select distinct sit.site_name as name
	,sit.site_long_name as abbreviation
	,sit.site_id as school_number
	,gll.short_name as low_grade
	,glh.short_name as high_grade
	

from matviews.ss_cube cub
join public.course_site_aff csa on csa.course_id = cub.course_id
join public.sites sit on sit.site_id = csa.site_id
join public.grade_levels gll on gll.grade_level_id = sit.start_grade_level_id 
join public.grade_levels glh on glh.grade_level_id = sit.end_grade_level_id

where cub.entry_date <= current_date
and cub.leave_date > current_date
and sit.site_id <> 9999999
