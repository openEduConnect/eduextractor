SELECT a.studentid,
       a.schoolid,
	   a.att_date,
	   a.att_code,
	   a.presence_status_cd
FROM ps_attendance_daily a
JOIN students s
  ON a.studentid = s.id
