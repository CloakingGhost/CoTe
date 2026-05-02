select a.id, count(b.PARENT_ID) as CHILD_COUNT
from ECOLI_DATA a
left join ECOLI_DATA b
on a.id = b.PARENT_ID
group by a.id
order by a.id asc;