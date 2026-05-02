-- 코드를 입력하세요
SELECT i.ANIMAL_ID,i.NAME 
from Animal_ins i
left join Animal_outs o
on i.Animal_id = o.Animal_id
where o.datetime is not null

order by datediff(o.datetime,i.datetime) desc
limit 2;