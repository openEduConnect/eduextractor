SELECT studentid,
       course_number,
       sectionid,
       grade,
       percent,
       excludefromgpa,
       gpa_addedvalue,
       'stored' AS source
FROM storedgrades
--take the storecodes from yaml
WHERE storecode IN ('Y1', 'T1', 'T2', 'T3', 'Q1', 'Q2', 'Q3', 'Q4')
  
UNION ALL
  
SELECT pg.studentid,
       sect.course_number,
       pg.sectionid,
       pg.grade,
       pg.percent,
       sect.excludefromgpa,
       c.add_to_gpa,
       'current' AS source
FROM pgfinalgrades pg
JOIN cc
  ON pg.studentid = cc.studentid
 AND pg.sectionid = cc.sectionid
 AND cc.dateenrolled <= TRUNC(SYSDATE)
 AND cc.dateleft >= TRUNC(SYSDATE)
JOIN sections sect
  ON cc.sectionid = sect.ID
JOIN courses c
  ON sect.course_number = c.course_number
WHERE pg.finalgradename IN ('Y1', 'T1', 'T2', 'T3', 'Q1', 'Q2', 'Q3', 'Q4')

