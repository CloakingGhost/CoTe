-- 10 아니고 (01이거나 100인경우만) == 101

select count(id)
from ECOLI_DATA 
where  !(GENOTYPE & 2) && GENOTYPE & 5;