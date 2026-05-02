-- 코드를 입력하세요
SELECT  i.ANIMAL_ID,i.ANIMAL_TYPE,i.NAME
from Animal_ins i
join Animal_outs o
on i.Animal_id = o.Animal_id
where i.SEX_UPON_INTAKE like 'Intact%' and 
    (o.SEX_UPON_OUTCOME like 'Neutered%' or o.SEX_UPON_OUTCOME like 'Spayed%');