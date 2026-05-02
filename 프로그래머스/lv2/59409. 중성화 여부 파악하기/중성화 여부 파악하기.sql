-- 코드를 입력하세요 
SELECT ANIMAL_ID, name,if(instr(SEX_UPON_INTAKE, 'intact'),'X','O') '중성화'
from ANIMAL_ins
order by Animal_id;