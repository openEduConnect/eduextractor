select distinct usr.first_name
	,usr.last_name
	,usr.email1 as "email_addr"
	,usr.user_id as "id"
	
from matviews.ss_cube cub
join public.users usr on usr.user_id = cub.user_id

where cub.entry_date <= current_date
and cub.leave_date > current_date
