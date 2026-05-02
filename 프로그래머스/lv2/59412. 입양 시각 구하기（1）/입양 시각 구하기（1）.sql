-- 코드를 입력하세요
SELECT hour(DATETIME),count(hour(DATETIME))
from ANIMAL_OUTS
where hour(DATETIME) between 9 and 19
group by hour(DATETIME)
order by hour(DATETIME);