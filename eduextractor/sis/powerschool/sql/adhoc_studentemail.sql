SELECT ID AS personid,
       'emailaddress' AS key,
       ps_customfields.getStudentscf(id, 'StudentEmail') AS value
FROM students s
WHERE s.enroll_status = 0