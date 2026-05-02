-- 코드를 입력하세요
SELECT Animal_type, ifnull(name,'No name'), SEX_UPON_INTAKE
from Animal_ins
order by Animal_id;