SELECT e.studentid,
       e.schoolid,
       e.grade_level,
       e.entrydate,
       e.exitdate
FROM ps_enrollment e
JOIN students s
  ON e.studentid = s.ID
 AND s.enroll_status = 0