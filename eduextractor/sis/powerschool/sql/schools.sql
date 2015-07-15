SELECT ds.name, 
       ds.abbreviation,
       ds.school_number,
       ds.low_grade,
       ds.high_grade
FROM districtschoolview ds;alternatecolor]

<tr class="oddrow" >
	<td><font size="1.5">          ~(ds.name;1)           </font>           </td>
	<td><font size="1.5">          ~(ds.abbreviation;t)    </font>           </td>
	<td><font size="1.5">          ~(ds.school_number;t)    </font>           </td>
	<td><font size="1.5">          ~(ds.low_grade;t)    </font>           </td>
	<td><font size="1.5">          ~(ds.high_grade;t)    </font>           </td>
</tr>
[/tlist_sql]



