SELECT cc.studentid,
       cc.termid,
	     cc.sectionid,
       sect.course_number,
       c.course_name,
       sect.schoolid,
       sect.teacher AS teacherid,
       t.first_name AS teacher_first,
       t.last_name AS teacher_last,
       cc.dateenrolled,
       cc.dateleft
FROM cc
JOIN students s
  ON cc.studentid = s.id
 AND s.enroll_status = 0
JOIN sections sect
  ON abs(cc.sectionid) = sect.ID
JOIN courses c
  ON sect.course_number = c.course_number
JOIN teachers t
  ON sect.teacher = t.id
  