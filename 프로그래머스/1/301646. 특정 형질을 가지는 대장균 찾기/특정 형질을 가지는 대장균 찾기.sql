-- 10 아니고 01이거나 11인경우만

select count(id)
from ECOLI_DATA 
where  not(GENOTYPE & 2) and (GENOTYPE & 1 or GENOTYPE & 4);