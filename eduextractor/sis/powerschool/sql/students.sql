SELECT s.id, 
       s.first_name,
       s.middle_name,
       s.last_name,
       s.gender,
       s.dob
FROM students s
--0 indicates currently enrolled students in PowerSchool
WHERE s.enroll_status = 0;alternatecolor]

<tr class="oddrow" >
	<td><font size="1.5">          ~(id;1)           </font>           </td>
	<td><font size="1.5">          ~(first_name;t)    </font>           </td>
	<td><font size="1.5">          ~(middle_name;t)    </font>           </td>
	<td><font size="1.5">          ~(last_name;t)    </font>           </td>
	<td><font size="1.5">          ~(gender;t)    </font>           </td>
	<td><font size="1.5">          ~(dob;t)    </font>           </td>
</tr>
[/tlist_sql]



