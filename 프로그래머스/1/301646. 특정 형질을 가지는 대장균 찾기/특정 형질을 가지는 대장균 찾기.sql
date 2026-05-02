-- 10 아니고 01이거나 11인경우만

select count(id)
from ECOLI_DATA 
where  !(GENOTYPE & 2) && GENOTYPE & 5;