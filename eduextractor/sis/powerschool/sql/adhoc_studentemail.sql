SELECT ID AS personid,
       'emailaddress' AS key,
       ps_customfields.getStudentscf(id, 'StudentEmail') AS value
FROM students s
;alternatecolor]

<tr class="oddrow" >
	<td><font size="1.5">          ~(id;1)           </font>           </td>
	<td><font size="1.5">          ~(personid;t)    </font>           </td>
	<td><font size="1.5">          ~(value;t)    </font>           </td>
</tr>
[/tlist_sql]

