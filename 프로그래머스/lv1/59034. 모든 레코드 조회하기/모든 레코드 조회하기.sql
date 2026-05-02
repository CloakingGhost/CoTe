-- 코드를 입력하세요
SELECT * 
from ANIMAL_INs
where INTAKE_CONDITION = 'Normal'
and not SEX_UPON_INTAKE = 'Intact Male'
order by animal_id ASC;