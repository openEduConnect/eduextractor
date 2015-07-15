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
  ON sect.teacher = t.id;alternatecolor]

<tr class="oddrow" >
	<td><font size="1.5">          ~(cc.id;1)           </font>           </td>
	<td><font size="1.5">          ~(cc.termid;t)    </font>           </td>
	<td><font size="1.5">          ~(cc.sectionid;t)    </font>           </td>
	<td><font size="1.5">          ~(sect.course_number;t)    </font>           </td>
	<td><font size="1.5">          ~(c.course_name;t)    </font>           </td>
	<td><font size="1.5">          ~(sect.schoolid;t)    </font>           </td>
	<td><font size="1.5">          ~(teacherid;t)    </font>           </td>
	<td><font size="1.5">          ~(teacher_first;t)    </font>           </td>
	<td><font size="1.5">          ~(teacher_last;t)    </font>           </td>
	<td><font size="1.5">          ~(cc.dateenrolled;t)    </font>           </td>
	<td><font size="1.5">          ~(cc.dateleft;t)    </font>           </td>
</tr>
[/tlist_sql]



