-- 코드를 작성해주세요

select 
    id,
    CASE 
        ntile(4) over(ORDER BY SIZE_OF_COLONY desc)
        when 1 then  'CRITICAL'
        when 2 then  'HIGH'
        when 3 then   'MEDIUM'
        else 'LOW' 
    end as COLONY_NAME
from ECOLI_DATA 
order by 1;