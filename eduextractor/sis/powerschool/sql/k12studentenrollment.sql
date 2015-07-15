SELECT e.studentid,
       e.schoolid,
       e.grade_level,
       e.entrydate,
       e.exitdate
FROM ps_enrollment e
JOIN students s
  ON e.studentid = s.ID
 AND s.enroll_status = 0;alternatecolor]

<tr class="oddrow" >
	<td><font size="1.5">          ~(studentid;1)           </font>           </td>
	<td><font size="1.5">          ~(schoolid;t)    </font>           </td>
	<td><font size="1.5">          ~(grade_level;t)    </font>           </td>
	<td><font size="1.5">          ~(entrydate;t)    </font>           </td>
	<td><font size="1.5">          ~(exitdate;t)    </font>           </td>
</tr>
[/tlist_sql]



