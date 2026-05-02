-- 코드를 입력하세요
SELECT i.ANIMAL_ID, i.NAME
from Animal_ins i
join Animal_outs o on i.Animal_id = o.Animal_id
where i.datetime >  o.datetime
order by i.datetime;
        

-- 보호 시작일보다 입양일이 더 빠른 동물
-- Animal_ins.datetime > Animal_outs.datetime