-- 코드를 입력하세요
SELECT Animal_id,name, date_format(datetime,'%Y-%m-%d')
from Animal_ins
order by Animal_id;