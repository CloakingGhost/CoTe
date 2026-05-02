-- 코드를 입력하세요
SELECT i.name, i.datetime
from Animal_ins i
left join Animal_outs o
on i.Animal_id = o.Animal_id
where o.datetime is null
order by i.datetime
limit 3;