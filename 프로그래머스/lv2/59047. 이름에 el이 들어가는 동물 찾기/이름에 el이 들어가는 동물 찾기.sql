-- 코드를 입력하세요
SELECT Animal_id, name
from Animal_ins
where Animal_type = 'dog' and name like '%el%'
order by name;