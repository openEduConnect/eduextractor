SELECT a.studentid,
       a.schoolid,
	   a.att_date,
	   a.att_code,
	   a.presence_status_cd
FROM ps_attendance_daily a
JOIN students s
  ON a.studentid = s.id;alternatecolor]

<tr class="oddrow" >
	<td><font size="1.5">          ~(id;1)           </font>           </td>
	<td><font size="1.5">          ~(schoolid;t)    </font>           </td>
	<td><font size="1.5">          ~(att_date;t)    </font>           </td>
	<td><font size="1.5">          ~(att_code;t)    </font>           </td>
	<td><font size="1.5">          ~(presence_status_cd;t)    </font>           </td>
</tr>
[/tlist_sql]

